from distutils.archive_util import make_zipfile
from rest_framework import serializers


class TestCrudSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=100)
    phone = serializers.CharField(max_length=10)
    gender = serializers.CharField(max_length=10)
    date_of_birth = serializers.DateField()
    
class UpdateCrudSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
   