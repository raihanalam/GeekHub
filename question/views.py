from django.shortcuts import render
from django.contrib import messages
from . models import Question
import datetime

# Create your views here.
def askquestion(request):
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
        messages.success(request, 'Succesfully send to our developer commiunity!')

    return render(request,'Question/askquestion.html')