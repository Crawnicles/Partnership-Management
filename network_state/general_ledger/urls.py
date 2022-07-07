from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:transaction_id>", views.transaction, name="transaction"),
    path("<int:transaction_id/book", views.book, name="book")
]