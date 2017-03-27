from django.conf.urls import url
from . import views

app_name = 'quiz'

urlpatterns = [
	url(r'home/$', views.home, name='home'),
	url(r'^(?P<quiz_id>[0-9]+)/$', views.show_quiz, name='show_quiz')
]
