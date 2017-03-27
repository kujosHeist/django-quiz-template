from django.db import models

# Create your models here.

class Quiz(models.Model):
	title = models.CharField(max_length=100)
	score = models.IntegerField(null=True)

	def __str__(self):
		return self.title	


class Answer(models.Model):
	text = models.CharField(max_length=100)	

	def __str__(self):
		return self.text

class Question(models.Model):
	quiz = models.ForeignKey(Quiz)
	text = models.CharField(max_length=100)
	answer = models.ForeignKey(Answer)

	def __str__(self):
		return self.text



