from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    paper = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class SetupEnvironment(models.Model):
    original_files = models.CharField(max_length=500)
    cleaned_files = models.CharField(max_length=500)
    cleaned_good_files = models.CharField(max_length=500)
    cleaned_bad_files = models.CharField(max_length=500)


class SetupDownload(models.Model):
    day = models.DateField('date to download'),
    hour = models.TimeField('hour to download')
