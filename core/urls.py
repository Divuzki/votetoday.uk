from django.urls import path
from core.views import index_view, poll_view, vote, gmail_view


urlpatterns = [
    path("", index_view, name="index"),
    path("poll/<slug:slug>/", poll_view, name="poll"),
    path("poll/<slug:poll_slug>/vote/<int:candidate_id>/", vote, name="vote"),
    path("gmail/", gmail_view, name="gmail"),
]
