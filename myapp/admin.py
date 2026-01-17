from django.contrib import admin
from .models import *
# Register your models here.
class showuser(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(register,showuser)

class showadmission(admin.ModelAdmin):
    list_display = ['formno','usersname','dob','course','mobile','doa','batch_time','admin_photo']
admin.site.register(admission,showadmission)


class showcourse(admin.ModelAdmin):
    list_display = ['name']

class showdetailcourse(admin.ModelAdmin):
    list_display = ['program','name','duration','detail']



class showcerti2(admin.ModelAdmin):
    list_display = ['regno','name','course','enroll','grade','duration','date','admin_photo']

admin.site.register(certificate2,showcerti2)
admin.site.register(mcourse,showcourse)
admin.site.register(detailcourse,showdetailcourse)
admin.site.register(fees)
admin.site.register(paid_log)
admin.site.register(Course)
