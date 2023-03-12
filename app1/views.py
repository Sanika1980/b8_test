from django.shortcuts import render,HttpResponse

# Create your views here.
# views-Function based view
  #     - Classbased view

# from .models import Student
# def welcome(request):     #reserved keyword
#     # studs = Student.objects.get(id=1)
#     print(request.method)
#     print(request.user)
#     print(request.GET)  # query parameters
#     studs = list(Student.objects.values("name"))
#     final_studs = list(map(lambda x:x["name"],studs))

#     return HttpResponse(f"Welcome to  the Django application...!!, {final_studs}")
    

def welcome(request):
     return render(request,"home.html")
