from django.shortcuts import render

# Create your views here.


def homepage_view(request):
    context = {

    }
    return render(request=request, template_name='dropzone/index.html', context=context)
