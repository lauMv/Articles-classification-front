from django.urls import path, reverse_lazy

from . import views

app_name = 'classifier_interface'

urlpatterns = [
    path('classifier_interface/', views.IndexView.as_view(), name='index'),
    path('classifier_interface/<int:id>/', views.ArticleDetailView.as_view(), name='detail'),
    path('config/', views.ClassifierView.as_view(), name='setup')
]