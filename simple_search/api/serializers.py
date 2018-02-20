from rest_framework import serializers
from simple_search.api.models import Search, MATCHER_ENUM


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('name', 'matcher')
    # name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # matcher = serializers.ChoiceField(choices=MATCHER_ENUM, required=True)

    # def create(self, validated_data):
    #     """
    #     Create and return a Search object using parsed data
    #     """
    #     return Search.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return a Search objects
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.matcher = validated_data.get('matcher', instance.matcher)
    #     return instance
