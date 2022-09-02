from rest_framework import serializers


class CategorySerializer(serializers.Serializer):

    pk = serializers.IntegerField()
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField()
