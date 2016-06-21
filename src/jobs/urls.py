from django.conf.urls import url

from .views import JobIndex, JobAdd, JobDetails, JobOutput

urlpatterns = [
    url(r'^$', JobIndex.as_view(), name='index'),
    url(r'^add$', JobAdd.as_view(), name='add'),
    url(r'^(?P<pk>[0-9\w-]+)/detail$', JobDetails.as_view(), name='details'),
    url(r'^(?P<pk>[0-9\w-]+)/output.json$', JobOutput.as_view(), name='output'),
]
