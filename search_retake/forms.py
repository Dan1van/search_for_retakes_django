from django import forms

from .models import Group


class SearchForRetakeForm(forms.Form):
    course_choices = empty_choice = [('None', '---------'), ]
    course_choices += Group.COURSE_CHOICES

    courses = forms.ChoiceField(choices=course_choices)
    groups = forms.ModelChoiceField(queryset=Group.objects.all().filter(course=0))

    def __init__(self, course_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        groups = forms.ModelChoiceField(queryset=Group.objects.all().filter(course=course_id))
