from django.db import models

# Create your models here.
# ORM-object relational mapper
class ActivePersons(models.Manager):  # Custom model manager
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)   # model.objects.all()

class InactivePersons(models.Manager):
    def get_queryset(self) :
        return super().get_queryset().filter(is_active=False)       


class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField(auto_now=True,null=True)
    date_updated = models.DateTimeField(auto_now_add=True,null=True)
    is_active = models.BooleanField(default=True)
    activep = ActivePersons()
    inactivep = InactivePersons()
    objects = models.Manager()


    class Meta:
        db_table = "person"

    def __str__(self):
        return f"{self.name} --- {self.age} ------ {self.address}"   

    def show_details(self):
        print(f""" --------------------------------------------------
        Person Name:- {self.name}
        Person Age:- {self.age}
        Person Mobile number:- {self.mobile_num}
        Person Address:- {self.address}   
        """)
    @classmethod
    def get_data_above_age(cls):
       return cls.objects.filter(age__gte=25)   # gt,gte,lt,lte,startswith,endswith

    @classmethod
    def get_avg_age(cls):
        data = cls.objects.all().values("id", "name", "age")
        lst = list(map(lambda x : x['age'],list(data)))
        return (sum(lst)//len(lst))  

    @classmethod
    def get_active_data(cls):
       return cls.objects.filter(is_active=True)   

    @classmethod
    def get_inactive_data(cls):
        return cls.objects.filter(is_active=False)  




class CommonClass(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta():
        abstract = True



class College(CommonClass):
    adr = models.CharField(max_length=500)
    est_date = models.DateField(auto_now=True)

    class Meta():
        db_table = "college"


class Principal(CommonClass):
       
    exp = models.FloatField()
    qual = models.CharField(max_length=50)
    college = models.OneToOneField(College, on_delete=models.CASCADE)
    class Meta():
        db_table = "principal"


class Department(CommonClass):
    dept_str = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    class Meta():
        db_table = "dept"



class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)

    class Meta():
        db_table = "student"


class Subject(CommonClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    class Meta():
        db_table = "subject"


# get models from database--- inspectdb
# ERD---Entity relationship diagram
#-------------------------------------------------------------------------------
from django.db import models

class FuelType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarModel(models.Model) :
    name = models.CharField(max_length=200)
    fueltype = models.ManyToManyField(FuelType,related_name="carmodels")   

    def __str__(self):
        return self.name


