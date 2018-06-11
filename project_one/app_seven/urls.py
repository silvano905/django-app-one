from django.conf.urls import url
from . import views


# template tagging
app_name = 'app_seven'   # global name, is = to the actual app name

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),  # domain.com/relative
    url(r'^other/$', views.other, name='other')    # domain.com/other
]
