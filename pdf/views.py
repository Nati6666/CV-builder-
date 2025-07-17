from django.shortcuts import render
from .models import Profile


# Create your views here.
def profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')   
        degree = request.POST.get('degree')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        school = request.POST.get('school')
        university = request.POST.get('university')
        achievements = request.POST.get('achievements')
    


        # Save the profile data to the database
        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            experience=experience,
            skills=skills,
            school=school,
            university=university,
            achievements=achievements
       
        )
        profile.save()
    return render(request, 'pdf/accept.html', )