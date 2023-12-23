from django.contrib import admin
from home.models import Article
from ckeditor.widgets import CKEditorWidget
from django.db import models


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.register(Article, ArticleAdmin)
