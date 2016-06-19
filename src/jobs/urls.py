from django.conf.urls import url

from .views import JobIndex, JobAdd

urlpatterns = [
    url(r'^$', JobIndex.as_view(), name='index'),
    url(r'^add$', JobAdd.as_view(), name='add'),
]
