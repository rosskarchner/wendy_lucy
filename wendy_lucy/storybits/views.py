from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .models import Scene, PointOfInterest
# Create your views here.

class SceneView(DetailView):
    model = Scene

class PoiView(DetailView):
    model = PointOfInterest

    def get_object(self, queryset=None):
        kwargs = resolver_match = self.request.resolver_match.kwargs
        # I don't know if this is neccesary
        if not queryset:
            queryset = self.get_queryset()

        return get_object_or_404(queryset,tag=kwargs['tag'])


    def get_queryset(self):
        kwargs = resolver_match = self.request.resolver_match.kwargs
        scene = Scene.objects.get(pk=kwargs['scene_pk'])
        return scene.pointofinterest_set.all()
