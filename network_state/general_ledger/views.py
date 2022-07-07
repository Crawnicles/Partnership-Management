from django.shortcuts import render


from .models import Transaction


# Create your views here.
def index(request):
    return render(request, "general_ledger/index.html", {
        "general_ledger": Transaction.objects.all()
    })

def transaction(request, transaction_id):
    transaction = Transaction.objects.get(pk=transaction_id)
    return render(request, "general_ledger/transaction.html",{
        "transaction": transaction
    })

#def book(request, transaction_id):
#    if request.method == "POST":
#        transaction = Transaction.objects.get(pk=transaction_id)
#        int(request.POST["transaction"]
# stopped at SQL - CS50w lecture 4 ~1hr30min into video

