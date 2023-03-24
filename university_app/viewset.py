from rest_framework import viewsets
from university_app.models import Student, Group, Address
from university_app.serializers import StudentSerializer , GroupSerializer , AdressSerializer, ModuleSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    http_method_name = ['GET','POST','PUT','DELETE']

class GroupViewset(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    http_method_name = ['GET','POST','PUT','DELETE']

class AddressViewset(viewsets.ModelViewSet):
    queryset=Address.objects.all()
    serializer_class=AdressSerializer
    http_method_name = ['GET','POST','PUT','DELETE']

class ModuleViewSet(viewsets.ModelViewSet):
    queryset=Address.objects.all()
    serializer_class=ModuleSerializer
    http_method_name = ['GET','POST','PUT','DELETE']