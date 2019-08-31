from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FlashInfoForm, ArticleForm, UserLocationForm
from zad_mobile.settings import DEFAULT_LONGITUDE, DEFAULT_LATITUDE
@login_required
def dashboard(request):
        return render(request, 'administration/dashboard.html')

@login_required
def flash(request):
        form_sent = False
        form = FlashInfoForm(request.POST or None)
        if form.is_valid():
                flash_info = form.save(commit=False)
                flash_info.author = request.user
                flash_info.save()
                form_sent = True
        return render(request, 'administration/flash.html', {'form_sent': form_sent})

@login_required
def article(request):
        form_sent = False
        form = ArticleForm(request.POST or None)
        if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                form_sent = True
        return render(request, 'administration/article.html', {'form_sent': form_sent})

@login_required
def reset_location(request):
        request.user.latitude = None
        request.user.longitude = None
        request.user.save()
        return redirect('position')

@login_required
def position(request):
        form_sent = False
        form = UserLocationForm(data = request.POST or None, instance=request.user)
        if form.is_valid():
                form.save()
                form_sent = True
        longitude = request.user.longitude or DEFAULT_LONGITUDE
        latitude = request.user.latitude or DEFAULT_LATITUDE
        placeholder_longitude = request.user.longitude or "aucune"
        placeholder_latitude = request.user.latitude or "aucune"

        return render(request, 'administration/position.html', {'long': longitude, 'lat': latitude,'placeholder_long': placeholder_longitude, 'placeholder_lat': placeholder_latitude})