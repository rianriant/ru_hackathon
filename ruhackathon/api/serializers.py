from rest_framework import serializers
from main.models import Ivent

class IventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ivent
    fields = '__all__'
    ordering = ['-date_posted']