from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Experience
from .forms import ExperienceForm


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


@login_required
def add_experience(request):
    """ A view to add an experience item to the website """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            experience = form.save()
            messages.success(request, f'Well done! Your new experience "{ experience.name }" has been added.')
            return redirect(reverse('experience_details', args=[experience.id]))
        else:
            messages.error(request, 'Oops! Something went wrong. Please ensure the form is valid.')
    else:
        form = ExperienceForm()

    template = 'experiences/add_experience.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
