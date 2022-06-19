from django.urls import path

from . import views

app_name = 'classifier_interface'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('config/', views.SetupEnvironmentView.as_view(), name='setup'),
    path('download/', views.SetupDownload.as_view(), name='download'),
]
