from django.shortcuts import render
from .models import Poll, Candidate


def index_view(request):
    polls = Poll.objects.all()
    return render(request, "pages/index.html", {"polls": polls})
