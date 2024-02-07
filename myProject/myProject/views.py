from django.shortcuts import render,redirect
from myProject.forms import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

def signupPage(request):

    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('loginPage')
    else:
        form = CustomUserCreationForm()

    return render(request,'signupPage.html',{'form': form})


def loginPage(request):
    
    if request.method == 'POST':
        
        form = CustomAuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                login(request, user)
                
                return redirect('dashBoardPage')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'loginPage.html', {'form': form})


def dashBoardPage(request):


    return render(request,'dashBoardPage.html')


def logoutPage(request):

    logout(request)

    return redirect('loginPage')


def addJobPage(request):

    if request.method=='POST':
        form=addJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewJobPage")
    else:
        form=addJobForm()

    return render(request,'addJobPage.html',{'form':form})

def viewJobPage(request):

    jobs = addJobModel.objects.all()

    return render(request,'viewJobPage.html',{'jobs': jobs})


def jobapplyPage(request, myid):
    job = addJobModel.objects.get(id=myid)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('job_list')  
    else:
        form = JobApplicationForm()

    return render(request, 'jobapplyPage.html', {'form': form, 'job': job})