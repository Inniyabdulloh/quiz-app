from django.urls import path
from .views import CreateQuizView
app_name = 'quiz'



urlpatterns = [
    path('create/', CreateQuizView.as_view(), name='create-quiz'),
]