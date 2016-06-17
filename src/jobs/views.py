from django.shortcuts import render
from django.views.generic import View


class JobIndex(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'jobs/index.html')
