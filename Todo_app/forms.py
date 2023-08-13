from django import forms
from Todo_app.models import Todo


class Todo_form(forms.ModelForm):
    class Meta:
        model = Todo

        fields = ('title', 'description', 'deadline', 'created_at', 'updated_at', 'user_id')
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'created_at': forms.HiddenInput(attrs={'required': False}),
            'updated_at': forms.HiddenInput(attrs={'required': False}),
            'user_id': forms.HiddenInput(attrs={'required': False})
        }
