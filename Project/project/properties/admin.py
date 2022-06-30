

# Register your models here.
from django.contrib.auth.models import User
from django.contrib import admin
from.models import Property, property_type, UploadedProb, PropImage

# Register your models here.

admin.site.register(property_type)
admin.site.register(UploadedProb)


class PropImageAdmin(admin.StackedInline):
    model = PropImage


class UploadProp(admin.StackedInline):
    model = Property


@admin.register(Property)
class PropAdmin(admin.ModelAdmin):
    inlines = [PropImageAdmin]

    class Meta:
        model = Property


class Useradmin(admin.ModelAdmin):
    inlines = [UploadProp]

    class Meta:
        model = User


@admin.register(PropImage)
class PropImageAdmin(admin.ModelAdmin):
    pass


class UserpropAdmin(admin.ModelAdmin):
    pass
