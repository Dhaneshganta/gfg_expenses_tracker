from django.shortcuts import render,redirect
from expenses.models import TrackingHistory,CurrentBalance
# Create your views here.

def index(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        description = request.POST.get("description")

        currentBalance,status = CurrentBalance.objects.get_or_create(id=1)

        expense_type = 'CREDIT'
        if int(amount) < 0:
            expense_type = 'DEBIT'
        trackingHistory = TrackingHistory.objects.create(
            amount = amount,
            description = description,
            expense_type = expense_type,
            current_balance = currentBalance
        )
        currentBalance.current_balance += float(trackingHistory.amount)
        currentBalance.save()
        print(amount,description)
        return redirect('/')

    trackingHistory = TrackingHistory.objects.all()
    expense = 0
    income = 0
    for tarack in trackingHistory:
        if tarack.expense_type == 'DEBIT':
            expense += tarack.amount
        else:
            income += tarack.amount


    currentBalance = CurrentBalance.objects.get(id=1)
    totalbalnce = currentBalance.current_balance
    contex={'totalbalnce':totalbalnce,'income':income,'expense':expense,'history':trackingHistory}

    return render(request,'index.html',contex)

def delete_transaction(request ,id):
    delete_history =TrackingHistory.objects.filter(id = id)
    currentBalance = CurrentBalance.objects.get(id=1)

    if delete_history.exists() :
        delete_data = delete_history[0]
        if delete_data.expense_type == 'DEBIT':
            current_total = currentBalance.current_balance
            current_total += delete_data.amount
            currentBalance.current_balance = current_total
            currentBalance.save()
        else:
            current_total = currentBalance.current_balance
            current_total -= delete_data.amount
            currentBalance.current_balance = current_total
            currentBalance.save()

        delete_history.delete()
    return redirect('/')

