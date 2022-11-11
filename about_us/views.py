from django.shortcuts import render


def view_about_us_page(request):
    """ A view to display the 'About us' page """

    return render(request, 'about_us/about_us.html')
