from rest_framework import serializers
from .models import Retake


class RetakeSerializers(serializers.ModelSerializer):
    discipline = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()
    group = serializers.StringRelatedField()
    date = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

    class Meta:
        model = Retake
        fields = ('id', 'discipline', 'teacher', 'group', 'audience', 'date')
