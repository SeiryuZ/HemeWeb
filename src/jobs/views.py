from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import AddJobForm


class JobIndex(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'jobs/index.html')


class JobAdd(View):

    def get(self, request, *args, **kwargs):
        form = AddJobForm()
        return render(request, 'jobs/add.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = AddJobForm(data=request.POST or None,
                          files=request.FILES or None)

        if form.is_valid():
            form.save(commit=True)
            return redirect('jobs:index')

        return render(request, 'jobs/add.html', context={'form': form})
