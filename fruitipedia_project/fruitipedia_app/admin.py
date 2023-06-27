from django.contrib import admin

from fruitipedia_project.fruitipedia_app.models import ProfileModel, FruitModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    pass


@admin.register(FruitModel)
class FruitModelAdmin(admin.ModelAdmin):
    pass
