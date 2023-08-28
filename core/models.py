from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    _type = models.CharField(max_length=100, null=True, blank=True)
    


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
    voters = models.ManyToManyField(
        Account, related_name="votes", blank=True, editable=False
    )
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-votes"]
