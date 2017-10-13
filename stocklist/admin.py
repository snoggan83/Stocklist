from django.contrib import admin
from .models import Stocklist, Stock

# Register model on admin page
admin.site.register(Stocklist)
admin.site.register(Stock)
