from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    desc = models.TextField()
    has_ended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def candidates(self):
        candidates = Candidate.objects.filter(poll=self)
        return candidates


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="candidates")
    voters = models.ManyToManyField("auth.User", related_name="votes", blank=True)

    def __str__(self):
        return self.name
