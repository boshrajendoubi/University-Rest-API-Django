from django.db import models
from datetime import date
from django.utils import timezone

#Enumeration :
#1 ere methode en utilisant une liste : python list of tuples
StudyLevel =[
    ('F_Class', 'first class'),
    ('S_Class', 'second class'),
    ('T_Class', 'third class'),
]

StateLevel=[
    ('Run', 'Running'),
    ('Achive', 'Achieved'),
    ('Cancel', 'Canceled'),
    ('Delay', 'Delayed')
]

Type=[
    ('nrml', 'Normal'),
    ('catchup', 'Catching-up'),
    ('support', 'Support'),
    ('train', 'Training')
]

ModuleType =[
    ('O_Module', 'optional module'),
    ('R_Module', 'required module'),
]

# Create your models here.

class Person(models.Model): #existe au niveau Orienté Objet : elle n'est pas une table au niveau de la BD / elle est de type models.Model car la class teacher et student vont hérité et donc ils sont des modeles
    name = models.CharField(max_length = 100, null = False , blank = False)
    familyName = models.CharField(max_length = 100, null = False , blank = False)
    birthDate = models.DateField(default = date(2004,1,1))
    email = models.EmailField(verbose_name = "email ", max_length=60)
    
    def __str__(self):
        return "name = %s, family name = %s " %(self.name, self.familyName)
    class Meta: 
        abstract = True 
        ordering = ['name', 'familyName']
# la classe student et teacher vont herité de la classe person qui n'est pas une table dans la BD

class Group(models.Model):
    #number = models.AutoField() #créer une clée primaire de type entier autogenerée
    name = models.CharField(max_length = 100, unique = True, null = False, blank = False)
    email = models.EmailField(max_length = 60, unique=True)
    students_number = models.PositiveIntegerField(default = 0)
    level = models.CharField(max_length = 10, choices = StudyLevel, default = StudyLevel[0][0])
    class Meta:
        db_table='Group'

class Absence(models.Model):
    date = models.DateField(default = timezone.now())
    motif = models.CharField(null = True , blank=True, max_length=100)
    justification = models.CharField(null = True , blank=True, max_length=100) 
    class Meta:
        db_table='Abscence'    

class Teacher(Person):
    grade = models.CharField(max_length = 200, null = False, blank = False, default = 0)
    emailWork = models.EmailField(max_length = 60)
    due = models.FloatField(default=0)
    photo = models.ImageField(upload_to = 'photos/Teacher', max_length = 200)
    class Meta:
        db_table='Teacher' 

    def __str__(self):
        return 'name = %s, family Name = %s' %(self.name, self.familyName)

class Module(models.Model):
    #number = models.AutoField()
    name = models.CharField(max_length = 100, null = False, blank = False,unique = True)
    level = models.CharField(max_length = 10, choices = StudyLevel, default = StudyLevel[0][0])
    typeModule = models.CharField(max_length = 10, choices = ModuleType, default = ModuleType[0][0])
    teacher = models.ManyToManyField(Teacher, through='TeachModule', through_fields=('module','teacher'))
    group = models.ManyToManyField(Group)
    class Meta:
        db_table='Module'

    def __str__(self):
        return 'name = %s, level = %s' %(self.name,self.level)

class TeachModule(models.Model):
    teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    numberHoursTeach = models.PositiveIntegerField(default = 1)
    year = models.PositiveIntegerField(default = timezone.now().year)

class Address(models.Model):
    """
    student = models.OneToOneField(
        Student,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    """
    number = models.PositiveIntegerField(default = 1)
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    PostalCode = models.CharField(max_length = 100)
    class Meta:
        db_table = 'Adress'

    def __str__(self):
        return 'street = %s, city = %s, PostalCode = %s' %(self.street, self.city, self.PostalCode)

class Student(Person):
    #Definir une clée primaire personalisée
    #inscriptionNumber = models.CharField(max_length = 20, primary_key = True)
    photo = models.ImageField(upload_to = 'photos/students', max_length = 200)
    state = models.CharField(max_length = 50)
    situation = models.CharField(max_length = 50)
    group = models.ForeignKey(Group, on_delete = models.CASCADE, null = True, blank = True)
    address = models.OneToOneField(Address, on_delete = models.CASCADE, null = True, blank = True)
    class Meta:
        db_table='Student'

    def __str__(self):
        return 'name = %s, family Name = %s' %(self.name, self.familyName)

class Session(models.Model):
    startTime = models.TimeField()
    endTime = models.TimeField()
    classrommNumber = models.IntegerField()
    goal = models.CharField(max_length = 100 , blank = False, null = False)
    summary = models.CharField(max_length = 100 , blank = False, null = False)
    listTools = models.CharField(max_length = 50 , null = False , blank = False)
    state = models.CharField(max_length = 50 , choices = StateLevel, default = StateLevel[0][0])
    type = models.CharField(max_length = 50 , choices = Type, default = Type[0][0])
    module = models.ForeignKey(Module, on_delete = models.CASCADE, null = True)
    class Meta:
        db_table = 'Session'
