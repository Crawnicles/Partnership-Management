from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

expenses = []

class NewExpenseForm(forms.Form):
    expense = forms.CharField(label="New Expense")

# Create your views here.
def index(request):
    return render(request, "expenses/index.html", {
        "expenses": expenses
    })

def add(request):
    if request.method == "POST":
        form = NewExpenseForm(request.POST)
        if form.is_valid():
            expense = form.cleaned_data["expense"]
            expenses.append(expense)
            return HttpResponseRedirect(reverse("expenses:index"))
        else:
            return render(request, "expenses/add.html",{
                "form": form
            })

    return render(request, "expenses/add.html", {
        "form": NewExpenseForm()
    })