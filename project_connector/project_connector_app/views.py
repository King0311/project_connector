from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "index.html")

def registor(request):
    return render(request , "Registor.html")

def login(request):
    return render(request , "login.html")

def guide(request):
    return render(request , "guide.html")

def guide_assign(request):
    return render(request , "guide_assign.html")

def guide_updates(request):
    return render(request , "guide_updates.html")

def student_chat(request):
    return render(request , "student_chat.html")

def student_work(request):
    return render(request , "student_work.html")

def student_updates(request):
    return render(request , "student_updates.html")
