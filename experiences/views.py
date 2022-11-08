from django.shortcuts import render, get_object_or_404
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


def view_experience_details(request, experience_id):
    """
    A view to display full details for each experience.
    """

    experience = get_object_or_404(Experience, pk=experience_id)

    context = {
        'experience': experience
    }

    return render(request, 'experiences/experience_details.html', context)
