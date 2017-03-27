from django.conf.urls import url
from . import views

app_name = 'quiz'

urlpatterns = [
	url(r'^home$', views.home, name='home')
]
