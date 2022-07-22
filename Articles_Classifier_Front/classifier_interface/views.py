import json
from django.views import generic
from .dtos import Article
from .services import get_all_articles, get_article


def convert_article(response):
    article_list = []
    article_data = json.loads(response)
    article_data = sorted(article_data, key=lambda d: d['extraction_date'], reverse=True)
    for article in article_data:
        a = Article(**article)
        article_list.append(a)
    return article_list


def convert_one(response, id):
    article_data = json.loads(response)
    for art in article_data:
        if art['id'] == id:
            article = {
                'id': art['id'],
                'filename': art['filename'],
                'extraction_date': art['extraction_date'],
                'paper': art['paper'],
                'user_classification': art['user_classification'],
                'model_classification': art['model_classification'],
                'article_content': art['article_content'],
            }
    return article


class IndexView(generic.ListView):
    template_name = 'classifier_interface/index.html'
    context_object_name = 'articles_data'

    def get_queryset(self):
        article_list = get_all_articles()
        article_data = convert_article(article_list)
        return article_data


class ArticleDetailView(generic.TemplateView):
    model = Article
    template_name = 'classifier_interface/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        data = super(ArticleDetailView, self).get_context_data(**kwargs)
        id = data['id']
        article = get_article(id)
        article = convert_one(article, id)
        return {'article': article}

    def get_user_classification(self):
        fields = ['user_classification']


class ClassifierView(generic.ListView):
    template_name = 'classifier_interface/setup.html'

