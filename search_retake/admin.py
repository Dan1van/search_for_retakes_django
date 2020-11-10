from django.contrib import admin

from .models import Teacher, Group, Discipline, Retake


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'course',)
    list_filter = ('course',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'fathers_name', 'display_discipline',)
    list_filter = ('disciplines',)


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'semester', 'exam_type', 'display_teacher',)
    list_filter = ('name', 'semester', 'exam_type',)


@admin.register(Retake)
class RetakeAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'teacher', 'group', 'audience', 'date',)
    list_filter = ('discipline', 'teacher', 'group', 'audience', 'date',)
