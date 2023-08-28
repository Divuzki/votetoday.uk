from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="candidates")

    def __str__(self):
        return self.name
