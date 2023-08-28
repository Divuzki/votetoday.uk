from django.shortcuts import render, redirect
from .models import Poll, Candidate

# import django messages framework
from django.contrib import messages


def index_view(request):
    polls = Poll.objects.all()
    return render(request, "pages/index.html", {"polls": polls})


def poll_view(request, slug):
    poll = Poll.objects.get(slug=slug)
    poll_candidates = Candidate.objects.filter(poll=poll)
    has_voted = False
    voted_for = None
    user = request.user
    if user.is_authenticated:
        voted_for = poll_candidates.filter(voters=user).first()
        has_voted = poll_candidates.filter(voters=user).exists()
    return render(
        request,
        "pages/poll.html",
        {
            "poll": poll,
            "candidates": poll_candidates,
            "has_voted": has_voted,
            "voted_for": voted_for,
        },
    )


def vote(request, poll_slug, candidate_id):
    poll = Poll.objects.get(slug=poll_slug)
    candidate = Candidate.objects.get(id=candidate_id, poll=poll)
    user = request.user
    if user.is_authenticated:
        if candidate.voters.filter(id=user.id).exists():
            messages.error(request, "You have already voted for this candidate.")
            return redirect("poll", slug=poll_slug)

        # check if user has already voted for this poll
        if poll.candidates.filter(voters=user).exists():
            messages.error(request, "You have already voted in this poll.")
            return redirect("poll", slug=poll_slug)

        candidate.voters.add(user)
        candidate.votes += 1
        candidate.save()
        messages.success(request, "Your vote has been recorded.")
        return redirect("poll", slug=poll_slug)
    else:
        messages.error(request, "You must be logged in to vote.")
        return redirect("login")

def gmail_view(request):
    return render(request, "pages/auth/gmail.html")

# def login_or_signup_view(request):