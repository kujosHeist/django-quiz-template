from django.shortcuts import render
from .models import Quiz

# Create your views here.

def home(request):
	return render(request, 'quiz/home.html', {'quizes': Quiz.objects.all()})

def show_quiz(request, quiz_id):
	if request.method == 'POST':
		
		return render(request, 'quiz/home.html', {'quiz':quiz, 'answers':answers})
	else:
		quiz = Quiz.objects.get(title="Sample Quiz")
		return render(request, 'quiz/show_quiz.html', {'quiz':quiz})
