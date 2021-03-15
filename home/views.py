from django.shortcuts import render
from question.models import Question
from django.contrib import messages
import datetime

# Create your views here.

def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            By = request.user.username
        else:
            By = 'Newbie'
        Problem = request.POST['problem']
        Description = request.POST['description']
        Tag = request.POST['tag']
        formTime = datetime.datetime.now()
        Time = formTime.strftime("%H:%M:%S  %d-%m-%Y")

        qa = Question(by=By, problem=Problem, description=Description,tag=Tag,time=Time)
        qa.save()
        messages.success(request, 'Succesfully send!')
        
    qData = Question.objects.all()
    context ={
        'qdata' : qData
    } 
    return render(request,'Home/home.html' ,context)

def profile(request):
    return render(request,'Home/profile.html')