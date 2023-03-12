from app1.models import *
from django.contrib.auth.models import User

#exec(open(r"D:\Code_Files\B8_django\first_project\db_shell.py").read())
# to get all data
# objs = Person.objects.all()
# print(list(objs))

# for person in objs:
#     print(person.__dict__)

# to get first record

# first_record = Person.objects.first()
# print(first_record)

# to get record by id
# obj = Person.objects.get(id=4)
# print(obj)


# if id is not present handle this error with try and except

# try:
#     obj = Person.objects.get(id=5)
# except Person.DoesNotExist:
#     print("Record does not exist")    

# to get multiple record by passing fieldname

# obj = Person.objects.filter(age=25)
# print(obj)

# obj = Person.objects.filter(age=25, address="Banglore") , means AND
# print(obj.query)
#p1 = Person.objects.get(id=16)
# print(p1.__dict__)
# print(p1.mobile_num)
# p1.mobile_num = 9820456672
# print(p1.__dict__)
# p1.save()
#p1.delete()

#1st way to save data
# p1 = Person(name="Anagha", age=32, mobile_num=9823415039, address="Nanded")
# p1.save()

# 2 nd way to save data
# Person.objects.create(name="Archana", age=23, mobile_num=9433213455, address="Amravati")

# bulk create

# p1 = Person(name="P", age=21, mobile_num=22, address="Thane")
# p2 = Person(name="Q",age=22, mobile_num=44, address="Chennai")
# p3 = Person(name="R", age=33, mobile_num=55, address="Mumbai")
# p4 = Person(name="S", age=43, mobile_num=66, address="Pune" )

# Person.objects.bulk_create([p1,p2,p3,p4])

# to delete all records
# Person.objects.all().delete()

#to delete multiple records

# Person.objects.filter(age=25).delete()
# print(Person.objects.filter(name__startswith="A"))

# print(Person.objects.filter(name__endswith="i"))


# print(Person.objects.exclude(name__startswith="A"))


# print(Person.objects.filter(name="Apurva").exists())

# print(Person.objects.all().order_by("id"))  # id - ASC, -id- DESC

# print(Person.objects.all().order_by("name"))


#Person.objects.get(id=1).show_details()


# for per_obj in Person.objects.all():
#     per_obj.show_details()
    

# print(Person.objects.count() )   

# print(Person.objects.all())
# print(Person.objects.filter(name__contains="S"))
# data = Person.objects.all().values()
# data = Person.objects.all().values("id", "name", "age")
# print(data)
# name_list = []
# for i in data:
#     name_list.append(i["name"])

# print(name_list)    

#print(list(data))
# lst = list(map(lambda x:x["age"],list(data)))
# print(sum(lst)//len(lst))


# data = Person.objects.all().values_list("name","age","address") # list of tuples containing values only
# print(list(data))




# database changed to mysql
# User.objects.create_user(username="Poonam",password="python@123")   # always use create user

# print(Person.objects.all() )

# delete- soft delete and hard delete

# data = Person.objects.filter(id__in=[3,5]).update(is_active=False)
# print(data)

# print(Person.get_active_data())
# print(Person.get_inactive_data())
# print(Person.get_avg_age())

# print(Person.activep.all())
# print(Person.inactivep.all())
# exec(open(r"D:\Code_Files\B8_django\first_project\db_shell.py").read())


#clgs = College.objects.all()
# prnc = Principal.objects.all() 
# depts = Department.objects.all()
# studs = Student.objects.all()
# subs = Subject.objects.all()

# print(clgs)
# print(prnc)
# print(depts)
# print(studs)
# print(subs)

# for dept in depts:
#     print(dept.__dict__)

#clg = clgs[0] 
# print(clg.__dict__)   
# print(clg.principal)


#print(clg.department_set.first())

# obj = Principal.objects.first()
# print(obj.college)
# dept = Department.objects.first()
# print(dept.college)
# print(dept.student_set.all()) 
# s1 = Student.objects.first()
# print(s1.dept)
# s2 = Student.objects.get(id=8)
# print(s2.dept)

# all_depts = Department.objects.all()
# for dept in all_depts:
#     print(f"Department name is {dept.name}, Studs:{dept.student_set.all()}")

# studs = Student.objects.all()
# print(studs)
# for stud in studs:
#     print(f"Student name:{stud}  and student department:{stud.dept}")
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept.name

# print(stud_dept_dict)

# print(clg.depts.all())

# dept = Department.objects.get(id=2)
# print(dept)
# print(dept.subs.all())

# dept = Department.objects.get(id=3)
# print(dept.subs.all())

# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subs.all())


# clg = College.objects.get(id=1)
# print(clg.depts.all()[1].studs.all())
# print(clg.depts.all()[2].studs.all())

# all_depts = clg.depts.all()
# for dept in all_depts:
#     print(dept.studs.all())

# all_depts = clg.depts.all()


# studs_list = []
# for dept in all_depts:
#     studs_list.extend(dept.studs.all())

# print(studs_list)    

# s1 = Student.objects.get(id=4)
# print(s1.dept.college)

# Addition of college

#College.objects.create(name="MIT", adr="Pune")
# c1 = College.objects.get(id=3)
# p1 = Principal(name="ABC",exp=20,qual="PHD",college=c1)   # pass object of college
#p1 = Principal(name="ABC",exp=20,qual="PHD",college_id=3)  # pass college id
#p1.save()
#Department.objects.create(name="Production",dept_str=80,college_id=3)

# Student.objects.create(name="A",marks=65,age=18)
# Student.objects.create(name="B",marks=45,age=19)
# Student.objects.create(name="c",marks=78,age=20)
# s1, s2, s3 = Student.objects.filter(id__gt=9)
# prod_dept = Department.objects.get(id=4)
# prod_dept.studs.add(s1,s2,s3)

# Subject.objects.create(name="TOM",is_practical=True,dept_id=4)
# Subject.objects.create(name="Mechanics",is_practical=True,dept_id=4)
# Subject.objects.create(name="TOS",is_practical=True,dept_id=4)
#prod_dept.studs.remove(s1)
# prod_dept.studs.add(s1)


# studs = Student.objects.all()
# print(studs)
# for stud in studs:
#     print(stud)

# studs = Student.objects.select_related("dept")
# for stud in studs:
#     print(stud.dept)    

# many to many 

# c180 = CarModel.objects.create(name="C180")
# c200 = CarModel.objects.create(name="C200")
# print(CarModel.objects.all())

# gas = FuelType.objects.create(name="Gas")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")
# print(FuelType.objects.all()) 
# c180 = CarModel.objects.get(name="C180")
# c200 = CarModel.objects.get(name="C200")
# gas = FuelType.objects.get(name="Gas")
# diesel = FuelType.objects.get(name="Diesel")
# hybrid = FuelType.objects.get(name="Hybrid")
#c180.fueltype.add(gas,diesel,hybrid)
# print(CarModel.objects.all())
# print(c180.fueltype.all())
#c200.fueltype.add(gas,diesel,hybrid)
#print(c200.fueltype.all())
# c200.fueltype.create(name="Bio Diesel")#  fueltype creation and assign to carmodel
# print(c200.fueltype.all())
#biodiesel = FuelType.objects.get(name="Bio Diesel")

# print(biodiesel.carmodel_set.all())
#print(gas.carmodels.all())

#print(CarModel.objects.filter(fueltype__name__startswith="B"))
# c180.fueltype.clear()
# print(c180.fueltype.all())
# print(Student.objects.filter(dept__name="IT"))
# print(Student.objects.filter(dept__college__id=3))
# print(Student.objects.filter(dept__college__name__in=["MIT","D Y Patil"]))

#---------------------------------------------------------------------------

# s1 = Student.objects.create(name="XYZ",marks=77,age=22)
# s2 = Student.objects.create(name="PQR",marks=66,age=24)
# sub1 = Subject.objects.create(name="DE",is_practical=True,dept_id=1)
# sub2 = Subject.objects.create(name="AE",is_practical=True,dept_id=1)
# print(Student.objects.all())

# subject1 = Subject.objects.get(name="AE")
# print(subject1)
# subject2 = Subject.objects.get(name="DE")
# s1,s2 = Student.objects.filter(id__gt=12)
# print(s1,s2)


# subject1.student.add(s1,s2)
# subject2.student.add(s1,s2)


# raw sql
# from django.db import connection

# # 1 st way
# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM STUDENT''')
# data = cursor.fetchall()
# print(data)

# data = cursor.fetchmany(3)
# print(data)


# 2 nd way
# data = Student.objects.raw('SELECT * FROM STUDENT')
# for i in data:
    # print(i)

#-------------------------------------------------------------------
# Multiple databases   multitenant app 
# MySQL,SQLite
# exec(open(r"D:\Code_Files\B8_django\first_project\db_shell.py").read())

SECOND_DATABASE = "second_db"
data = Student.objects.using(SECOND_DATABASE).all()
# print(data)
# c2 = College.objects.using(SECOND_DATABASE).create(name="MIT",adr="Pune")
# d2 = Department.objects.using(SECOND_DATABASE).create(name="MECH",dept_str=80,college=c2)
# s3 = Student.objects.using(SECOND_DATABASE).create(name="SS",marks=78,age=21,dept=d2)
# sub2 = Subject.objects.using(SECOND_DATABASE).create(name="TOS",is_practical=True,dept=d2)
sub = Subject.objects.using(SECOND_DATABASE).get(id=2)
s3 = Student.objects.using(SECOND_DATABASE).get(id=3)
sub.student.add(s3)
# c1 = College.objects.using(SECOND_DATABASE).create(name="COEP",adr="Pune")
# d1 = Department.objects.using(SECOND_DATABASE).create(name="EXTC",dept_str=60,college=c1)
# s1 = Student.objects.using(SECOND_DATABASE).create(name="XYZ",marks=89,age=22,dept=d1)
# s2 = Student.objects.using(SECOND_DATABASE).create(name="PQR",marks=90,age=21,dept=d1)
# sub1 = Subject.objects.using(SECOND_DATABASE).create(name="DSP",is_practical=True,dept=d1)
# subject = Subject.objects.using(SECOND_DATABASE).get(id=1)
# print(subject)
# s1,s2 = Student.objects.using(SECOND_DATABASE).filter(id__lt=3)
# print(s1,s2)
# subject.student.add(s1,s2)
#-----------------------------------------------------------------------
#exec(open(r"D:\Code_Files\B8_django\first_project\db_shell.py").read())
clgs = College.objects.all()
princ = Principal.objects.all()
studs = Student.objects.all()
subs = Subject.objects.all()
# print(clgs)
# print(princ)
# print(studs)
# print(subs)
dept = Department.objects.all()
# print(dept)
clg = clgs[0]
# print(clg.principal)
# obj = Principal.objects.first()
# print(obj.college)


# one to many
# print(dir(clg))

#print(clg.department_set.all())
# dept = Department.objects.first()
#print(dept.college)
# print(dept.student_set.all())
# student_obj = Student.objects.first()
# print(student_obj.dept)

# dept = Department.objects.get(id=3)
# print(dept.student_set.all())

# depts = Department.objects.all()
# for dept in depts:
#     print(f"{dept.name}  {dept.student_set.all()}")

# studs = Student.objects.all()
# for stud in studs:
#     print(f"student name: {stud.name}  ,department: {stud.dept}")


# depts = Department.objects.all()
# for dept in depts:
#     print(f"department name: {dept.name} ,subjects: {dept.subject_set.all()}")


# subs = Subject.objects.all()
# for sub in subs:
#     print(f"Subject: {sub.name} ,Deparment:  {sub.dept}")


# clg = College.objects.get(id=1)
# all_depts = clg.department_set.all()
# for dept in all_depts:
#     print(f"{dept.name}  {dept.student_set.all()}")

# s1 = Student.objects.get(id=5)
# print(s1.dept.college)
# studs = Student.objects.all()
# for stud in studs:
#     print(f"student name: {stud.name},subjects: {stud.subject_set.all()}")

# subs = Subject.objects.all()
# for sub in subs:
#     print(f"{sub.name}  {sub.student.all()}")    

# s1 = Student.objects.get(name="A")
# s2 = Student.objects.get(name="B")
# s3 = Student.objects.get(name="C")
# sub = Subject.objects.get(name="TOS")
# sub.student.add(s1,s2,s3)



print(User.objects.all())
# User.objects.create_user(username="Soham",password='python@123',email="soham@gmail.com")