from rest_framework import serializers
from .models import save_data
class hash_serializer(serializers.ModelSerializer):    #create api for add hashes

    class Meta:
        model = save_data
        fields = ['word']