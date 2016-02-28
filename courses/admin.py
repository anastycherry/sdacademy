from django.contrib import admin
from courses.models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'short_description']

class LessonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['subject']}),
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
