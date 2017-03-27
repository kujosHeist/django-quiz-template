from django.conf.urls import url
from . import views

app_name = 'quiz'

urlpatterns = [
	url(r'^submit$', views.submit, name='submit')
	url(r'^results$', views.results, name='results')
]
