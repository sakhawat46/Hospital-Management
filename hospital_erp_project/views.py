from django.shortcuts import render, redirect, HttpResponse
from hospital_app.email_backend import EmailBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from hospital_app.models import CustomUser, Patient

from django.contrib import messages

def base(request):
    return render(request, 'base.html')


def login_user(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'),)
    if user != None:
        login(request, user)
        user_type = user.user_type
        if user_type == '1':
            return redirect('hod_home')
        elif user_type == '2':
            return HttpResponse("This is STAFF Panel")
        elif user_type == '3':
            return HttpResponse("This is DOCTOR Panel")
        else:
            messages.error(request, 'Email and password are invalid!')
            return redirect('login_user')
    else:
        messages.error(request, 'Email and password are invalid!')
        return redirect('login_user')



def dologout(request):
    logout(request)
    return redirect('login_user')


@login_required(login_url='/')
def profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {'user': user, }
    return render(request, 'profile.html', context)


@login_required(login_url='/')
def profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic)

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            
            # customuser.profile_pic = profile_pic

            # print(profile_pic)

            if password != None and password != "":
                customuser.set_password(password)

            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            
            customuser.save()
            messages.success(request, "Your Profile Update Successfully.")
            return redirect('profile')

        except:
            messages.error(request, "Your Profile Update Failed.")


    return render(request, 'profile.html')


@login_required(login_url='/')
def patient_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        form = Patient(
            name = name,
            mobile_number = mobile_number,
            age = age,
            gender = gender,
            address = address
        )

        form.save()

        messages.success(request, "Your Profile Update Successfully.")
        return redirect('patient_add')

    return render(request, 'hod/patient_registration.html')