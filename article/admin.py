from django.contrib import admin
from .models import Article, Rubric


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]

    prepopulated_fields = {'slug':('title',)} 

    class Meta:
        model = Article