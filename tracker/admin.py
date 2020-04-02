from django.contrib import admin
from tracker.models import Wallet,Expense,Income

admin.site.register([Wallet,Expense,Income])
# Register your models here.
