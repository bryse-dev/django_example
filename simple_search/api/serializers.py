from rest_framework import serializers
from simple_search.api.models import Search, MATCHER_ENUM


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('name', 'matcher', 'status', 'percent_complete')
        read_only_fields = ('status', 'percent_complete',)
