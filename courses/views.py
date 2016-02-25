from django.shortcuts import render
from courses.models import Course, Lesson
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Course.objects.all

class DetailView(generic.DetailView):
    model = Lesson
    template_name = 'courses/detail.html'

