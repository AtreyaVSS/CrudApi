from rest_framework import serializers
from .models import *

class EmpSerializers(serializers.ModelSerializer):
    class Meta:
        model = empmodel
        fields = '__all__'


