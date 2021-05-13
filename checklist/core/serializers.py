from rest_framework import serializers
from .models import CheckList, CheckListItem

class CheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CheckListItem
        fields='__all__'

class CheckListSerializer(serializers.ModelSerializer):
    items= CheckListItemSerializer(source='checklistitem_set',many=True,read_only=True)
    class Meta:
        model=CheckList
        fields='__all__'
    # title=serializers.CharField()
    # is_deleted=serializers.BooleanField()
    # is_archived=serializers.BooleanField()
    # created_on=serializers.DateTimeField()
    # updated_on=serializers.DateTimeField()
