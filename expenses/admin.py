from django.contrib import admin
from expenses.models import *


admin.site.register(CurrentBalance)
# admin.site.register(TrackingHistory)

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "current_balance",
        "amount",
        "expense_type",
        ]

admin.site.register(TrackingHistory,TrackingHistoryAdmin)