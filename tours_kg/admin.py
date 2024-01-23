from django.contrib import admin
from .models import *


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("reg_name",)


@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    list_display = ("sight_name", "province", "price")


@admin.register(BookNow)
class BookNowAdmin(admin.ModelAdmin):
    list_display = ("name", "sightseeing", "date")
    readonly_fields = ("name", "surname", "email", "sightseeing")


@admin.register(JoinUs)
class JoinUsAdmin(admin.ModelAdmin):
    list_display = ("email",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "sight", "rating")


admin.site.register(Image)
