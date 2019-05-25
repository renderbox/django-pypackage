from django.contrib import admin

# Register your models here.
from pypackage.models import Package, Version

def recreate_slug(modeladmin, request, queryset):
    '''
    This uses the save() instead of update() since the AutoSlugField is only generated on save().
    '''
    for item in queryset.all():
        item.slug = ""
        item.save()

recreate_slug.short_description = "Regenerate the Slug Field"


class PackageAdmin(admin.ModelAdmin):
    readonly_fields=('slug',)
    actions = [recreate_slug]


class VersionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Package, PackageAdmin)
admin.site.register(Version, VersionAdmin)
