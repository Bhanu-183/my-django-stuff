from django.contrib import admin

from firstapp.models import *
# Register your models here.

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Users)
admin.site.register(UserProfileInfor)



admin.site.register(School)
admin.site.register(Student)