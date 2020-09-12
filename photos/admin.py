from django.contrib import admin

# Register your models here.

from .models import Data, UserInfo, Profile, Announcement, Year, StudentInfo, Group
from import_export.admin import ImportExportModelAdmin

admin.site.register(Data)
admin.site.register(UserInfo)
admin.site.register(Profile)
admin.site.register(Announcement)
admin.site.register(Year)
admin.site.register(StudentInfo)
admin.site.register(Group)
