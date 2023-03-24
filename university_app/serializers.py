from rest_framework import serializers
from django.db import models
from django.db.models import fields
from university_app.models import Student
from university_app.models import Group
from university_app.models import Address

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        #fields=('name','familyname','birthdate')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'
        #fields=('name','familyname','birthdate')

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model= Address
        fields='__all__'
        #fields=('name','familyname','birthdate')

class ModuleSerializer(serializers.ModelSerializer) :
    studies=GroupSerializer(many=True, read_only=True, required=False)  
    class Meta:
        model=ModuleNotFoundErrorfields='__all__' #serializers all fields 
        
        
