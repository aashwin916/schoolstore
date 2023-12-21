from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

from myapp.models import Registration


def school(request):
    return render(request, 'school.html', )

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def reg(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        cpassword = request.POST['Password2']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return  redirect('reg')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,"email taken")
            #     return  redirect('reg')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')

            # messages.info(request,'User created')

        else:
            messages.info(request,"password not matching")
            return redirect('reg')
        return redirect('/')

    return render(request, 'register.html')

def reg_form(request):
    return render(request, 'order.html')

def process_reg(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.getlist('materials')
        registration = Registration(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            department=department,
            course=course,
            purpose=purpose,
            materials=', '.join(materials),
        )
        registration.save()



    messages.success(request, 'Order Confirmed')

    return render(request, 'reg_result.html')



def logout(request):
    auth.logout(request)
    return redirect('/')