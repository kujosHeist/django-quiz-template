from django.shortcuts import render
from .models import Quiz

# Create your views here.

def home(request):
	if request.method == 'POST':
		print("Process quiz answers")


		return render(request, 'quiz/home.html', {'results':results})
	else:
		return render(request, 'quiz/home.html')
