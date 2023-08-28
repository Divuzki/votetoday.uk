from django.contrib import admin
from .models import Poll, Candidate


class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1


class PollAdmin(admin.ModelAdmin):
    inlines = [CandidateInline]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Poll, PollAdmin)
admin.site.register(Candidate)
