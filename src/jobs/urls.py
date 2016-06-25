from django.conf.urls import url

from .views import (JobIndex, JobAdd, JobDetails, JobOutput, JobConfiguration1,
                    JobConfiguration2, JobOverview)

urlpatterns = [
    url(r'^$', JobIndex.as_view(), name='index'),
    url(r'^add$', JobAdd.as_view(), name='add'),
    url(r'^(?P<pk>[0-9\w-]+)/detail$', JobDetails.as_view(), name='details'),
    url(r'^(?P<pk>[0-9\w-]+)/configure_1$', JobConfiguration1.as_view(), name='configure1'),
    url(r'^(?P<pk>[0-9\w-]+)/configure_2$', JobConfiguration2.as_view(), name='configure2'),
    url(r'^(?P<pk>[0-9\w-]+)/overview$', JobOverview.as_view(), name='overview'),
    url(r'^(?P<pk>[0-9\w-]+)/output.json$', JobOutput.as_view(), name='output'),
]
