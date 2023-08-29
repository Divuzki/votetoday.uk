from django.contrib import admin
from .models import Poll, Candidate, Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("__str__", "ip_address", "country", "city", "state")
    search_fields = ("identifier", "username", "phone_number")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = (
        "region",
        "country",
        "_type",
    )
    fieldsets = ()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(is_staff=True)

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1


class PollAdmin(admin.ModelAdmin):
    inlines = [CandidateInline]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Account, AccountAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Candidate)
