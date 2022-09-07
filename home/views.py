from django.shortcuts import render


def view_home(request):
    """ A view to display the homepage """

    return render(request, 'home/index.html')
