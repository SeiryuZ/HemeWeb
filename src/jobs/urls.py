from django.conf.urls import url

from .views import JobIndex

urlpatterns = [
    url(r'^$', JobIndex.as_view(), name='index'),
]
