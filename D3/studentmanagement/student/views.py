# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, EnrollmentForm

# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'
# ordering = ['last_name', 'first_name']

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['enrollments'] = Enrollment.objects.filter(student=self.object)
    return context

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy