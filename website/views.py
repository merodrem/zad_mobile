from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import FlashInfo, Article, User
# Create your views here.

def home(request):
    one_week_ago = datetime.now() - timedelta(days=7)
    users = list(User.objects.all().values())
    flash_infos = FlashInfo.objects.filter(date__gt=one_week_ago)
    last_articles = Article.objects.all()[:5]
    return render(request, 'website/home.html', {'flash_infos': flash_infos, 'last_articles': last_articles, 'users': json.dumps(users, cls=DjangoJSONEncoder)})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'website/login.html')

def logout_view(request):
    logout(request)
    previous_page = request.META['HTTP_REFERER']
    if "administration" in previous_page:
        return redirect("home")
    else:
        return redirect(request.META['HTTP_REFERER'])

def article(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'website/article.html', {'article': article})
    
def news(request):
    articles = Article.objects.values('id', 'title', 'date', 'author__username')
    orderedArticles = {}
    for article in articles:
        if not article['date'] in orderedArticles:
            orderedArticles[article['date']] = [] 
        orderedArticles[article['date']].append(article)
    one_week_ago = datetime.now() - timedelta(days=7)
    flash_infos = FlashInfo.objects.filter(date__gt=one_week_ago)
    return render(request, 'website/news.html', {'orderedArticles': orderedArticles, 'flash_infos': flash_infos})