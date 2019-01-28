from django.shortcuts import render, redirect

# Create your views here.

GITHUB_URL = "https://github.com/dongkwan-kim/fb-news-stat-api"
README_PATH = "/blob/master/README.md"

def code(request):
    return redirect(GITHUB_URL)

def docs(request):
    return redirect(GITHUB_URL + README_PATH)
