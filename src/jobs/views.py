import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import AddJobForm
from .models import Job


class JobIndex(ListView):

    model = Job
    template_name = 'jobs/index.html'
    paginate_by = 20


class JobDetails(DetailView):
    model = Job
    template_name = 'jobs/details.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetails, self).get_context_data(**kwargs)
        context['stdout'] = self.object.get_output('stdout')
        context['stderr'] = self.object.get_output('stderr')
        context['hemelb'] = self.object.get_output('hemelb')
        return context


class JobOutput(View):

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id=self.kwargs['pk'])
        output = {}
        output['stdout'] = job.get_output('stdout')
        output['stderr'] = job.get_output('stderr')
        output['hemelb'] = job.get_output('hemelb')

        return HttpResponse(json.dumps(output), content_type='application/json')


class JobAdd(View):

    def get(self, request, *args, **kwargs):
        form = AddJobForm()
        return render(request, 'jobs/add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = AddJobForm(data=request.POST or None,
                          files=request.FILES or None)

        if form.is_valid():
            job = form.save()

            job.prepare_directories()
            job.status = job.QUEUED
            job.save(update_fields=['status'])

            job.enqueue_job()

            return redirect(job)

        return render(request, 'jobs/add.html', context={'form': form})
