from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Teacher, ActiveStudent, New, Direction, EducationDirect, Leader, Application


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'name', 'lastname', 'get_image', 'job_title', 'description', 'direction')

    def get_image(self, obj):
        if obj.image:
            res = mark_safe(f"<img style='width: 60px' src='{obj.image.url}'/>")
        else:
            res = "Rasm topilmadi"
        return res

    get_image.short_description = "Rasmi"


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'direction_name', 'direction_title')


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'name', 'lastname', 'get_image', 'job_title', 'description']

    def get_image(self, obj):
        if obj.image:
            res = mark_safe(f"<img style='width: 60px' src='{obj.image.url}'/>")
        else:
            res = "Rasm topilmadi"
        return res

    get_image.short_description = "Rasmi"


@admin.register(EducationDirect)
class EducationDirectAdmin(admin.ModelAdmin):
    list_display = ['id', 'edu_name', 'get_image', 'edu_place', 'edu_title']

    def get_image(self, obj):
        if obj.edu_image:
            res = mark_safe(f"<img style='width: 60px' src='{obj.edu_image.url}'/>")
        else:
            res = "Rasm topilmadi"
        return res

    get_image.short_description = "Rasmi"


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_image', 'news_title', 'news_description']

    def get_image(self, obj):
        if obj.new_image:
            res = mark_safe(f"<img style='width: 60px' src='{obj.new_image.url}'/>")
        else:
            res = "Rasm topilmadi"
        return res

    get_image.short_description = "Rasmi"


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'name', 'lastname', 'email_address', 'address', 'phone_number']


@admin.register(ActiveStudent)
class ActiveStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_name', 'group_image', 'group_title', 'group_result']
