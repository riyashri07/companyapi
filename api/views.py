from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company
from api.serializers import CompanySerializer
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
 queryset=Company.objects.all()  # All instances of the Company model
 serializer_class=CompanySerializer

 #In Django, a QuerySet is a collection of database queries
 # that can be used to retrieve data from the database. 
 #The objects attribute is the default manager provided by Django
 # for database-related operations on the model.

#Company.objects.all() is a QuerySet that retrieves all instances of the
 # Company model from the database. 
 # The all() method is used to get all records in the table associated with the Company model.