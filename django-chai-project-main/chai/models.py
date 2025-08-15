from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVarity(models.Model):
   CHAI_TYPE_CHOICE = [
      ('BL', 'Black Tea'),
      ('ML', 'Masala Chai'),
      ('GR', 'Green Tea'),
      ('EL', 'Elaichi Chai'),
      ('AD', 'Adrak Chai'),
   ]
   name = models.CharField(max_length=100)
   image = models.ImageField(upload_to='chai/')
   data_added = models.DateTimeField(default=timezone.now)
   type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)