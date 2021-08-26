from django.shortcuts import render
from article.models import Article, Rubric
from django.views.generic.detail import DetailView


def article(request):
    model = Article
    article = Article.objects.all()
    rubrics = Rubric.objects.all()
    context = {'articles': article, 'rubrics': rubrics}
    return render(request,'article/index.html',context)



def by_rubric(request,rubric_id):
	ArticleList = Article.objects.filter(rubric = rubric_id)
	rubrics = Rubric.objects.all()
	current_rubric = Rubric.objects.get(pk = rubric_id)
	context = {'articles' : ArticleList,'rubrics' : rubrics,'current_rubric ': current_rubric }
	return render(request,'article/by_rubric.html',context)


def article_detail(request, article_id):
    article = Article.objects.get(id = article_id)
    context = {'article': article}
    return render(request, 'article/article_detail.html', context)