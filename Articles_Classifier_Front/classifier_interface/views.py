from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from .models import Article, SetupEnvironment, SetupDownload


class IndexView(generic.ListView):
    template_name = 'classifier_interface/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.all()


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'classifier_interface/article_detail.html'


class SetupEnvironmentView(generic.ListView):
    model = SetupEnvironment
    template_name = 'classifier_interface/setup.html'


class SetupDownload(generic.ListView):
    model = SetupDownload
    template_name = 'classifier_interface/set_download.html'