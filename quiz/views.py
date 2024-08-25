from django.shortcuts import render
from django.views.generic import CreateView
from .forms import QuizForm
from quiz.models import Quiz


# Create your views here.
class CreateQuizView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = 'quiz/create-quiz.html'