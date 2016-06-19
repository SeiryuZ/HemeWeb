from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView

from .forms import AddJobForm
from .models import Job


class JobIndex(ListView):

    model = Job
    template_name = 'jobs/index.html'
    paginate_by = 20


class JobAdd(View):

    def get(self, request, *args, **kwargs):
        form = AddJobForm()
        return render(request, 'jobs/add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = AddJobForm(data=request.POST or None,
                          files=request.FILES or None)

        if form.is_valid():
            job = form.save(commit=True)

            job.prepare_directories()
            job.status = job.QUEUED
            job.save(update_fields=['status'])

            job.enqueue_job()

            return redirect('jobs:index')

        return render(request, 'jobs/add.html', context={'form': form})
