from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    is_completed=models.BooleanField()
    assign_date=models.DateTimeField(auto_now_add=True)
    category=models.ManyToManyField(CategoryModel)
    def __str__(self):
        return self.title