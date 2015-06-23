from django.contrib import admin

# Register your models here.
from .models import Payment
from .models import Income

admin.site.register(Payment)
admin.site.register(Income)
