from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Read a new book!",
    "may": "Practice meditation daily!",
    "june": "Write in a journal every day!",
    "july": "Take a photo every day!",
    "august": "Try a new recipe every week!",
    "september": "Learn a new language!",
    "october": "Go hiking every weekend!",
    "november": "Volunteer for a local charity!",
    "december": None
}

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_num(request, month):
    if(month < 1 or month > 12):
        return HttpResponseNotFound("This month is not supported")
    
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse("month-name", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": text
        })
    except:
        raise Http404()
    