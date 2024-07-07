# wework/acaunt/forms.py
from django import forms
from .models import masseges
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = masseges
        fields = ['recipient', 'text']
        widgets = {
            'recipient': forms.Select(),
            'text': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['recipient'].queryset = User.objects.exclude(id=self.user.id)
        else:
            self.fields['recipient'].queryset = User.objects.none()
