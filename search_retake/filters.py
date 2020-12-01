import django_filters

from .models import Retake


class RetakeFilter(django_filters.FilterSet):

    class Meta:
        model = Retake
        fields = ('discipline', 'teacher', 'group', 'audience', 'date')