from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=50, default='None')


    def __str__(self):
        return self.category_name