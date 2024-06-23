from django.contrib import admin
from .models import Coffee

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')  # Ensure 'quantity' is included

admin.site.register(Coffee, CoffeeAdmin)