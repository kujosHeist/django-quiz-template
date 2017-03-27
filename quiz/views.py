from django.shortcuts import render
from .models import Quiz

# Create your views here.

def home(request):
	return render(request, 'quiz/home.html', {'quizes': Quiz.objects.all()})

def show_quiz(request, quiz_id):
	print("posted data")
	if request.method == 'POST':
		
		quiz = Quiz.objects.get(id=quiz_id)
		answers = []
		for question in quiz.question_set.all():
			user_answer_id = request.POST[str(question.id)]
			user_answer = question.answer_set.get(id=user_answer_id)
			correct_answer = question.correct_answer
			if user_answer == correct_answer:
				answers.append(user_answer)

		return render(request, 'quiz/show_quiz.html', {'quiz':quiz, 'answers':answers})
	else:
		quiz = Quiz.objects.get(id=quiz_id)
		return render(request, 'quiz/show_quiz.html', {'quiz':quiz})
