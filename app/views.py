from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    t=datetime.datetime.now()
    d={'data':'hai filters how are u','t':t,'c':1}



    return render(request, 'filters.html',d)