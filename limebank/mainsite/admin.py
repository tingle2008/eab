from models import PersonalProfile
from models import JobInformation
from models import RelativeInformation
from models import Attachments

from django.contrib import admin

class PersonalProfileAdmin(admin.ModelAdmin):
    """ Client Profile Admin
    """
    pass

class JobInformationAdmin(admin.ModelAdmin):
    pass

class RelativeInformationAdmin(admin.ModelAdmin):
    pass

class AttachmentsAdmin(admin.ModelAdmin):
    pass

        


# Register your models here.
admin.site.register(PersonalProfile, PersonalProfileAdmin)
admin.site.register(JobInformation, JobInformationAdmin)
admin.site.register(RelativeInformation, RelativeInformationAdmin)
admin.site.register(Attachments, AttachmentsAdmin)
