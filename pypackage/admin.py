from django.contrib import admin

# Register your models here.
from pypackage.models import Package, Version


class PackageAdmin(admin.ModelAdmin):
    pass


class VersionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Package, PackageAdmin)
admin.site.register(Version, VersionAdmin)
