from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import SceneView, PoiView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/1')),
    url(r'^(?P<pk>\d+)/$', SceneView.as_view(), name='detail'),
    url(r'^(?P<scene_pk>\d+)/(?P<tag>.+)/$', PoiView.as_view(), name='poi'),
] 
