from django import forms

from .models import Teacher


class RetakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RetakeForm, self).__init__(*args, **kwargs)
        print('\n\n\n', self.instance.pk)
        self.fields['teacher'].queryset = Teacher.objects.filter(disciplines__id=self.instance.pk)
