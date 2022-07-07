from django.contrib import admin

from .models import Transaction, People, New_Members

# Register your models here.
admin.site.register(Transaction)
admin.site.register(People)
admin.site.register(New_Members)