from django.contrib import admin


from .models import Scene, Choice, PointOfInterest
# Register your models here.


class PoiInline(admin.StackedInline):
    model = PointOfInterest


class ChoiceInline(admin.TabularInline):
    model = Choice
    fk_name = 'scene'

class ChoiceInline(admin.TabularInline):
    model = Choice
    fk_name = 'scene'


class SceneAdmin(admin.ModelAdmin):
    inlines = [PoiInline, ChoiceInline]


admin.site.register(Scene, SceneAdmin)
