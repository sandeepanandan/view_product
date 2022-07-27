from django.contrib import admin
from productapp.models import Products
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Products)
admin.register(User)
