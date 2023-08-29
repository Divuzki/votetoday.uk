from django.contrib import admin
from .models import Poll, Candidate, Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("__str__", "ip_address", "country", "city", "state")
    search_fields = ("email", "username", "phone_number")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = (
        "region",
        "country",
        "_type",
    )
    fieldsets = ()

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1


class PollAdmin(admin.ModelAdmin):
    inlines = [CandidateInline]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Account, AccountAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Candidate)
