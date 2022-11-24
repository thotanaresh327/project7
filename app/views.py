from django.shortcuts import render

# Create your views here.
def naresh(request):
    d={'a':10}
    return render(request,'naresh.html',context=d)