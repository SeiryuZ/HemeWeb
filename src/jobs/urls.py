from django.conf.urls import url

from .views import JobIndex, JobAdd, JobDetails

urlpatterns = [
    url(r'^$', JobIndex.as_view(), name='index'),
    url(r'^add$', JobAdd.as_view(), name='add'),
    url(r'^(?P<pk>[0-9\w-]+)/detail$', JobDetails.as_view(), name='details'),
]
