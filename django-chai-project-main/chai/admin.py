from django.contrib import admin
from .models import ChaiVarity

# Register your models here.
admin.site.register(ChaiVarity)

def __str__(self):
    return self.name