from django.shortcuts import render, HttpResponse
from .models import Article
# Create your views here.


def home(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        sum = Article.objects.all().count()
        tags = Article.objects.all().values_list("tag", flat=True).distinct()
        canva = []
        for tag in tags:
            canva.append({"name": tag, "num": Article.objects.filter(tag=tag).count() / sum * 100})
        canva = sorted(canva, key=lambda x: x["num"], reverse=True)
    return render(request, 'home.html', context={"articles": articles, "canva_top1_name": canva[0]["name"], "canva_top1_num": canva[0]["num"],
                                                 "canva_top2_name": canva[1]["name"], "canva_top2_num": canva[1]["num"], "canva_top3_name": canva[2]["name"],
                                                 "canva_top3_num": canva[2]["num"], "canva_top4_name": canva[3]["name"], "canva_top4_num": canva[3]["num"]})


def project(request, id):
    article = Article.objects.filter(id=id).first()
    return render(request, 'project.html', context={"article": article})


