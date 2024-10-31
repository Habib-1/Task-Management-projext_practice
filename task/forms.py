from django import forms
from task.models import TaskModel
class task_form(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'


