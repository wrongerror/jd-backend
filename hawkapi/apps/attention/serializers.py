from apps.attention.models import Attention
from rest_framework import serializers


class AttentionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Attention
        fields = ('report_id', 'type','details', 'created_at')

