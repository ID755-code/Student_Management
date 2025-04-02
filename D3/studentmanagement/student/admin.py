from django.contrib import admin
from student.models import Student, Course, Enrollment


# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)