from django.contrib import admin
from students.models import Student, Course

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'email']
    list_display = ['full_name', 'email', 'skype']
    list_filter = ['courses']


admin.site.register(Student, StudentAdmin)
