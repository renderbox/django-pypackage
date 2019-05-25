import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from autoslug import AutoSlugField

################
# FILE HANDLERS
################

def package_local_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user/<id>/profile/avatar/<filename>
    # Need to figure out good strategy on where to move it after upload and processing.
    return 'packages/{0}/{1}'.format(instance.package.slug, filename)


############
# PACKAGE
############

class Package(models.Model):
    '''
    Which Location is this at?
    '''
    name = models.CharField(max_length=32)
    slug = AutoSlugField(populate_from='name')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


############
# VERSION
############

class Version(models.Model):
    '''
    Which Location is this at?
    '''
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="versions")
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    checksum = models.CharField(max_length=128)
    checksum_type = models.CharField(max_length=8)
    local_file = models.FileField(upload_to=package_local_path, blank=True)
    mirror_path = models.CharField(max_length=256, blank=True)                              # IF THIS IS MIRRORED...
    mirrored = models.BooleanField()
    archive_format = models.CharField(max_length=8)
    requires_python = models.CharField(max_length=64, blank=True)
    
    def get_absolute_url(self):
        # https://files.pythonhosted.org/packages/8f/1f/74aa91b56dea5847b62e11ce6737db82c6446561bddc20ca80fa5df025cc/Django-1.1.3.tar.gz#sha256=0e5034cf8046ba77c62e95a45d776d2c59998b26f181ceaf5cec516115e3f85a
        
        if self.local_file:
            path = settings.MEDIA_URL + self.local_file.name
        else:
            path = self.mirror_path

        return path + "#" + self.checksum_type + "=" + self.checksum
    
    def file_name(self):
        if self.local_file:
            return self.local_file.name.split("/")[-1]
        return self.mirror_path.split("#")[0].split("/")[-1]

    def __str__(self):
        return self.package.name + " -> " + self.file_name()
