from django.shortcuts import render
from .models import Experience


def view_experiences(request):
    """
    A view to display the company's 
    on-the-premises experiences.
    """

    experiences = Experience.objects.all()

    context = {
        'experiences': experiences
    }

    return render(request, 'experiences/experiences.html', context)
