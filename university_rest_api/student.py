from django.db import models
from datetime import date
from django.utils import timeZone
#enumeration
#premiere methode: using python List of tuples
StudyLevel=[
    ('F_Class','first class'),
    ('S_Class','Second class'),
    ('T_Class','third class'),
]

class Person(models.Model):
    name=models.CharField(max_length=100)
    familyName=models.ChartField(max_length=100)
    birthDate=models.DateField(default=date(2004,1,1))
    email=models.EmailField(verbose_name="student's mail",max_length=60)
    photo=models.ImageField(upload_to='photos/students',max_length=200)
    class Meta:
        abstract=True
    




class Group(models):
    
    """Model definition for MODELNAME."""
    name=models.CharField(max_length=100,unique=True,blanck=False,null=False)
    email=models.EmailField(max_length=60,unique=True)
    student_numebr=models.PositiveIntegerFields(default=0)
    level=models.CharField(max_length=10,choices=StudyLevel,default=StudyLevel[0][0])
    
class Adress(models.Model):
    number=models.PositiveInteger(default=1)
    street=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    postalCode=models.PositiveInteger(default=1)
       
  
class Student(Person):
    #define a  primary key
    InsciptionNumber=models.CharField(max_length=20,primary_key=True)
    state=models.CharField(max_length=100)
    situation=models.CharField(max_length=100)
    adress=models.OneToOneField(Adress,on_delete=models.CASCADE,null=True,blank=True)
    group=models.OneToOneField(Group,on_delete=models.CASCADE,null=True,blank=True)
    
class Teacher (Person):
    email_work=models.EmailField(max_length=60,unique=True)
    due=models.CharField(max_length=100)   
    grade=models.CharField(max_length=100)    
    
class Module(models.Model):
    
     name=models.CharField(max_length=100)
     study=models.ManytoManyField(Group)
     teacher_mdoules=models.ManyToManyField(Teacher,through='TeacherModule',through_Fields=('Teacher','Module'))
     def __str__(self):
        return 'name=%s, familyNAme=%s'%(self.name, self.familyName)
     class Meta:
        db_table='module'
        verbose_name='Module'
        verbose_name_pluriel="gpmodules"
        
       
        



    
class TeacherModule(models.Model):
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True,blank=True)
    module=models.ForeignKey(Module, on_delete=models.CASCADE,null=True,blank=True)
    year=models.PositiveInteger()
    default=timeZone.now(year)



    