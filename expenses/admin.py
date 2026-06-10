from django.contrib import admin
from expenses.models import *


admin.site.register(CurrentBalance)
# admin.site.register(TrackingHistory)

@admin.action(description="make type as  creadit for everyone ")
def credit_make(modeladmin, request, queryset):

    for q in queryset:
        obj = TrackingHistory.objects.get(id=q.id)
        if obj.amount  < 0:
            obj.amount = obj.amount * -1
            obj.save()

    queryset.update(expense_type="CREDIT")

@admin.action(description="make type as debit for everyone")
def debit_make(modeladmin,request,queryset):

    for q in queryset:
        obj = TrackingHistory.objects.get(id=q.id)
        if obj.amount  > 0:
            obj.amount = obj.amount * -1
            obj.save()
    queryset.update(expense_type="DEBIT")


class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "current_balance",
        "amount",
        "expense_type",
        'description',
        'display_age',
        ]


    def display_age(self,obj):
        if obj.amount > 0:
            return "positiove"
        else:
            return "negitive"

    search_filter = ['expense_type','amount']
    list_filter = ['expense_type']
    ordering = ['-amount']
    actions = [credit_make,debit_make]
admin.site.disable_action("delete_selected")


admin.site.register(TrackingHistory,TrackingHistoryAdmin)