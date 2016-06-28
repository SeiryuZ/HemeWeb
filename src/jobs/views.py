import json
import os

from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import AddPreviousJobForm, AddNewJobForm, ConfigureJobForm, RunJobSetupForm
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
        context['view'] = 'detail'
        return context


class JobOutput(View):

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id=self.kwargs['pk'])
        output = {}
        output['stdout'] = job.get_output('stdout')
        output['stderr'] = job.get_output('stderr')
        output['hemelb'] = job.get_output('hemelb')

        return HttpResponse(json.dumps(output), content_type='application/json')


class JobConfiguration1(View):

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id=self.kwargs['pk'])
        context = {
            'config_file': job.configuration_file.read(),
            'job': job,
            'view': 'configure1',
        }
        return render(request, 'jobs/configure_1.html', context=context)

    def post(self, request, *args, **kwargs):
        job = Job.objects.get(id=self.kwargs['pk'])
        filename = os.path.basename(job.configuration_file.name)
        job.configuration_file.delete()
        job.configuration_file.save(filename, ContentFile(request.POST['content']))

        output = {"content": job.configuration_file.read()}
        return HttpResponse(json.dumps(output), content_type='application/json')


class JobConfiguration2(View):

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id=self.kwargs['pk'])
        form = ConfigureJobForm(
            instance=job,
            initial={
                'instance_type': job.instance_type,
                'container_image': job.container_image
            }
        )
        context = {
            'job': job,
            'form': form,
            'view': 'configure2',
        }
        return render(request, 'jobs/configure_2.html', context=context)

    def post(self, request, *args, **kwargs):
        job = Job.objects.get(id=self.kwargs['pk'])
        form = ConfigureJobForm(instance=job, data=request.POST)

        if form.is_valid():
            job = form.save()
            return redirect('jobs:overview', str(job.id))

        context = {
            'job': job,
            'form': form,
            'view': 'configure2',
        }
        return render(request, 'jobs/configure_2.html', context=context)


class JobOverview(View):

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(id=self.kwargs['pk'])
        context = {
            'job': job,
            'config_file': job.configuration_file.read(),
            'view': 'overview',
        }
        return render(request, 'jobs/overview.html', context=context)

    def post(self, request, *args, **kwargs):
        job = Job.objects.get(id=self.kwargs['pk'])
        job.enqueue_job()
        job.status = job.QUEUED
        job.save(update_fields=['status'])
        return redirect(job)


class JobAdd(View):

    def get(self, request, *args, **kwargs):
        form = AddNewJobForm()
        previous_job_form = AddPreviousJobForm()
        preprocess_form = RunJobSetupForm()

        context = {
            'new_job_form': form,
            'previous_job_form': previous_job_form,
            'preprocess_form': preprocess_form
        }
        return render(request, 'jobs/new_add.html', context=context)

    def post(self, request, *args, **kwargs):
        form = AddNewJobForm(data=request.POST or None,
                             files=request.FILES or None)

        previous_job_form = AddPreviousJobForm(data=request.POST or None)
        preprocess_form = RunJobSetupForm(data=request.POST or None,
                                          files=request.FILES or None)

        if form.is_valid():
            job = form.save()
            return redirect(job.get_next_step_url())

        if previous_job_form.is_valid():
            # Copy all necessary files from previous jobs
            job = previous_job_form.copy_previous_job_config()
            return redirect(job.get_next_step_url())

        if preprocess_form.is_valid():
            job = form.save()
            return redirect(job.get_next_step_url())

        context = {
            'new_job_form': form,
            'previous_job_form': previous_job_form
        }
        return render(request, 'jobs/new_add.html', context=context)
