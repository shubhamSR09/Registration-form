from django.shortcuts import render
from .form import SingUp

# Create your views here.
def sing_up(request):
    fm =''
    if request.method == 'POST':
        fm=SingUp(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            fm=SingUp()
    return render(request, 'enroll/sing_up.html',{'form':fm})