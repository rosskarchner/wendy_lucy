from __future__ import unicode_literals

from django.db import models


class Scene(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __unicode__(self):
        return self.title


class Choice(models.Model):
    scene = models.ForeignKey(Scene)
    prompt = models.CharField(max_length=1000)
    destination = models.ForeignKey(Scene, related_name='destination')


class PointOfInterest(models.Model):
    scene = models.ForeignKey(Scene)
    tag = models.CharField(max_length=255)
    description = models.TextField()
