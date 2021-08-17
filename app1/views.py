from django.shortcuts import render

# Create your views here.
def app1_fir(request):
    return render(request, 'app1/app1_first.html')