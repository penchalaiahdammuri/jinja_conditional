from django.shortcuts import render

# Create your views here.
# if condition
def jinja_conditional(request):
    return render(request,'jinja_conditional.html',context={'a':101,'b':200,'c':50})
