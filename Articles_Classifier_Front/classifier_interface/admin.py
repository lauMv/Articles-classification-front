from django.contrib import admin

from .models import Article, SetupEnvironment

admin.site.register(Article)

class SetupEnvironmentAdmin(admin.ModelAdmin):
    fields = ['original_files', 'cleaned_files', 'cleaned_good_files', 'cleaned_bad_files']


admin.site.register(SetupEnvironment, SetupEnvironmentAdmin)

