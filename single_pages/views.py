from django.shortcuts import render

def landing(req):
    return render(
        req,
        'single_pages/landing.html',
    )

def about_me(req):
    return render(
        req,
        'single_pages/about_me.html',
    )