from apps.search.models import Search
from rest_framework import serializers
"""
未使用
"""

class SearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Search
        fields = ('uid', 'type', 'created_at', 'updated_at')

