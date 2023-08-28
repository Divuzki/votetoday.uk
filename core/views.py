from django.shortcuts import render
from .models import Poll, Candidate


def index_view(request):
    polls = Poll.objects.all()
    return render(request, "pages/index.html", {"polls": polls})


def poll_view(request, slug):
    poll = Poll.objects.get(slug=slug)
    poll_candidates = Candidate.objects.filter(poll=poll)
    return render(
        request, "pages/poll.html", {"poll": poll, "candidates": poll_candidates}
    )

def vote(request, poll_slug, candidate_id):
    poll = Poll.objects.get(slug=poll_slug)
    candidate = Candidate.objects.get(id=candidate_id)
    user = request.user
    if user.is_authenticated:
        candidate.voters.add(user)
    return render(request, "pages/thanks.html", {"poll": poll, "candidate": candidate})