from django.contrib import admin
from .models import Client

# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
    list_display = [
        'accountName',
        'lastName',
        'firstName',
        'middleName',
        'suffix',
        'birthdate',
        'sex',
        'civilStatus',
        'weight',
        'height',
        'monthlyIncome',
        'profession',
        'mailingAddress1',
        'mailingAddress2',
        'sameMailingAddress',
        'clientPhoto',
        'clientSignature'
    ]
    
    
    
admin.site.register(Client, ClientsAdmin)