from django.contrib import admin
from .models import Claim

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('claimant', 'policy_number', 'status', 'submission_date')
    list_filter = ('status',)
    search_fields = ('claimant__username', 'policy_number')

    actions = ['approve_claim', 'reject_claim']

    # Action to approve claims
    def approve_claim(self, request, queryset):
        queryset.update(status='Approved')
        self.message_user(request, "Selected claims have been approved.")
    
    # Action to reject claims
    def reject_claim(self, request, queryset):
        queryset.update(status='Rejected')
        self.message_user(request, "Selected claims have been rejected.")

    approve_claim.short_description = "Approve selected claims"
    reject_claim.short_description = "Reject selected claims"
