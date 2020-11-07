from django.contrib import admin

from .models import Teacher, Group, Discipline, Retake
from .forms import RetakeForm


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'fathers_name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'exam_type')


@admin.register(Retake)
class RetakeAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'teacher':
            pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # form = RetakeForm
    list_display = ('discipline', 'group', 'audience', 'date')
