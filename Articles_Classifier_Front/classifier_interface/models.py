# from datetime import datetime
# from django.db import models
#
#
# class Article(models.Model):
#     filename = models.CharField(max_length=200)
#     extraction_date = models.DateField(default= datetime.now().strftime('%Y %m %d'))
#     paper = models.CharField(max_length=50)
#     user_classification = models.CharField(max_length=10)
#     model_classification = models.BooleanField()
#     content = models.TextField()
#
#     class Meta:
#         verbose_name_plural = 'articles_list'
#
#     def __str__(self):
#         return self.filename
#
#
# class Classifier(models.Model):
#     classifier_creation_date = models.DateField(default= datetime.now().strftime('%Y %m %d'))
#     day = models.DateField('date to download')
#     hour = models.TimeField('hour to download')
#     words = models.ExpressionList('word-list')
#     feedback_status = models.BooleanField('status')
#     feedback = models.IntegerField('min articles')
#     root_file = models.CharField(max_length=200)
#     precision_score = models.CharField(max_length=5)
#     accuracy_score = models.CharField(max_length=5)
#     recall_score = models.CharField(max_length=5)
#     f1_score = models.CharField(max_length=5)
#
