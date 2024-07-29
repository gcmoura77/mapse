
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

@login_required
def dashboard(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

@login_required
def billing(request):
    return render(request, 'pages/billing.html', { 'segment': 'billing' })

@login_required
def tables(request):
    return render(request, 'pages/tables.html', { 'segment': 'tables' })

@login_required
def notification(request):
    return render(request, 'pages/notifications.html', { 'segment': 'notification' })

@login_required
def typography(request):
    return render(request, 'pages/typography.html', { 'segment': 'typography' })

@login_required
def profile(request):
    return render(request, 'pages/profile.html', { 'segment': 'profile' })

@login_required
def index(request):
    return render(request, 'pages/index.html', { 'segment': 'index' })

