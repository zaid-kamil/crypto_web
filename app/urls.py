from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('about/',TemplateView.as_view(template_name='about.html'), name='about'),
    path('terms/',TemplateView.as_view(template_name='term_n_condition.html'),name='tnc')
]