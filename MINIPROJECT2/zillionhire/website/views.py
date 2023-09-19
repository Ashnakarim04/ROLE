from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages, auth
from django.http import HttpResponse,HttpResponseRedirect
from .models import Jobs, CompanyProfile
from .models import Students
from .models import CustomUser
# from .forms import StudentForm
from django.shortcuts import render, get_object_or_404, redirect
# from .models import  CustomUser

# from django.contrib.auth import get_user_model

  
 
# from django.contrib.auth import get_user_model
# Create your views here.

# def sample(request):
#     return render(request, 'sample.html')
# def loginn(request):
#     return render(request, 'login.html')
# def reg(request):
#     return render(request, 'registration.html')
# User=get_user_model()
def index(request):
    return render(request, 'index.html')
def jobs(request):
    return render(request, 'jobs.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def cjob(request):
    return render(request, 'cjob.html')
def blog(request):
    return render(request, 'blog.html')
def postjob(request):
    return render(request, 'postjob.html')
# def admin_index(request):
#     return render(request, 'admin/index.html')
def admin_index2(request):
    return render(request, 'admin/index-2.html')
def admin_profile(request):
    return render(request, 'admin/profile.html')
def admin_editprofile(request):
    return render(request, 'admin/edit-profile.html')
# def admin_students(request):
#     return render(request, 'admin/students.html')
def admin_company(request):
    return render(request, 'admin/company.html')
# def admin_addstudent(request):
#     return render(request, 'admin/addstudent.html')
def admin_studentadd(request):
    return render(request,'admin/student_add.html')
def ad_cprofile(request):
    return render(request, 'admin/ad_cprofile.html')

# def addjob(request):
#     return render(request, 'addjob.html')


# def loginn(request):
#     if request.method == "POST":
#         username=request.POST['email']
#         # email = request.POST['email']
#         password=request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.is_superuser:
#                 return redirect('admin_index2')
#             elif user.is_staff:
#                 return redirect('sindex')
#             else:
#                 return redirect('cindex')
#         else:
#             messages.info(request, "Invalid Login")
#             return redirect('loginn')
#     else:
#         return render(request, 'login.html') 

from django.shortcuts import render
from django.contrib.auth import authenticate, login
# def loginn(request):
#     if request.method == 'POST':
#          username=request.POST['email']
#          password=request.POST['password']
         
        #  if username  and password:
        #       user = authenticate(request, username=username, password=password)
        #       if user is not None:
        #            login(request, user)
                   
        #            if request.user.role == CustomUser.ADMIN:
                       
        #                 return redirect(reverse('admin_index2'))
                   
        #            elif request.user.role == CustomUser.STUDENT:
                       
        #                 return redirect(reverse('sindex'))
        #            elif request.user.role == CustomUser.COMPANY:
                       
        #                 return redirect(reverse('cindex')) 
#               else:
#                    messages.info(request,"Invalid User")
#                    return redirect('login')
#                 #    error_message = "Invalid login credentials."
#                 #    return render(request, 'login.html', {'error_message': error_message})
        
#     return render(request,'login.html')


# def loginn(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email)  # Print the email for debugging
#         print(password)  # Print the password for debugging
#         if email and password:
#             user = authenticate(request, email=email, password=password)
#             print("Authenticated user:", user)  # Print the user for debugging
#             if user is not None:
#                 login(request, user)
#                 print("User authenticated:", user.email, user.role)
#                 # return redirect('sindex')
#                 return redirect('http://127.0.0.1:8000/')
#             else:
#                 error_message = "Invalid login credentials."
#                 return render(request, 'login.html', {'error_message': error_message})
#         else:
#             error_message = "Please fill out all fields."
#             return render(request, 'login.html', {'error_message': error_message})
def reg(request):
    if request.method == "POST":
        companyname = request.POST['companyname']
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        headquarter = request.POST['headquarter']
        ceo = request.POST['ceo']
        phoneNumber = request.POST['phoneNumber']
        # role=User.COMPANY
        
        
        if password == confirmPassword:
            # if User.objects.filter(companyname=companyname).exists():
            #     return render(request, 'registration.html', {'companyname_exists': True})
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email already exists') 
                return redirect('reg')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                company = CompanyProfile(user=user, companyname=companyname, headquarter=headquarter, ceo=ceo, contact=phoneNumber) 
                user.save()
                company.save()
                messages.success(request, 'Registration successful! You can Login now..')
                return redirect('loginn')
        else:
            messages.error(request, 'Password confirmation does not match')
            return redirect('reg')
    else:
        return render(request, 'registration.html')
    
def loggout(request):
    print('Logged Out')
    auth.logout(request)
    return redirect('/')

def sample2(request):
    return render(request, 'sample2.html')
def cindex(request):
   if request.user.is_authenticated:
        companyprofile = request.user.companyprofile
        return render(request, 'cindex.html', {'companyprofile': companyprofile})
def aboutuser(request):
    return render(request, 'aboutuser.html')
def contactuser(request):
    return render(request, 'contactuser.html')
def cprofile(request, companyprofile_id):
    companyprofile=CompanyProfile.objects.get(id=companyprofile_id)
    
    if request.method == "POST":
         addressline1 = request.POST.get('addressline1')
        #  contact2 = request.POST.get('contact2')
         website = request.POST.get('website')
         city = request.POST.get('city')
         state = request.POST.get('state')
         district = request.POST.get('district')
         country = request.POST.get('country')
         pincode = request.POST.get('pincode')
         companydp=request.FILES['companydp'] if 'companydp' in request.FILES else None
 
         companyprofile.addressline1 = addressline1
         companyprofile.website= website
         companyprofile.city=city
         companyprofile.district=district
         companyprofile.state=state
         companyprofile.country=country
         companyprofile.pincode=pincode 
         companyprofile.companydp=companydp

        
         companyprofile.save()
         
         messages.success(request, 'Profile updated successfully.')
         return redirect('cindex')
    else:
         print("NO")
    context={
        'companyprofile': companyprofile
    }
    return render(request, 'cprofile.html', context)

# def postjob(request, companyprofile_id):
#     # Use get_object_or_404 to get the CompanyProfile instance or raise a 404 error if not found
#     companyprofile = get_object_or_404(CompanyProfile, id=companyprofile_id)

#     if request.method == "POST":
#         website = request.POST.get('website')
#         companyprofile.website = website
#         companyprofile.save()
#         return redirect('cindex')
#     else:
#         print("NO")
#     context={
#         'companyprofile': companyprofile
#     }
#     job = Jobs.objects.all()
#     return render(request, 'postjob.html', {'job': job, 'companyprofile': companyprofile}, context)

def sindex(request):
    return render(request, 'sindex.html')
def studentloginn(request):
    if request.method == "POST":
        username=request.POST['email']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid Login")
            return redirect('studentloginn')
    else:
        return render(request, 'studentlogin.html') 


def addjob(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        jname = request.POST.get('jname') 
        salary = request.POST.get('salary')
        email = request.POST.get('email')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        link = request.POST.get('link')
        criteria=request.FILES['criteria'] if 'criteria' in request.FILES else None

        obj = Jobs()
        obj.cname = cname
        obj.jname = jname
        obj.salary = salary
        obj.email = email
        obj.sdate = sdate
        obj.edate = edate
        obj.link = link
        obj.criteria=criteria
        
        obj.save()
        messages.success(request, 'Job added successfully!')

       # Redirect to the doctors page
        return redirect('postjob')  # Redirect to the doctors page URL name
    
    return render(request, 'addjob.html')
def postjob(request):
    job = Jobs.objects.all()
    return render(request, 'postjob.html', {'job': job})




# edit_job

from django.shortcuts import render, get_object_or_404, redirect
from .models import Jobs

def edit_job(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    
    if request.method == 'POST':
        job.cname = request.POST.get('cname')
        job.jname = request.POST.get('jname')
        job.salary = request.POST.get('salary')
        job.email = request.POST.get('email')
        job.sdate = request.POST.get('sdate')
        job.edate = request.POST.get('edate')
        job.link = request.POST.get('link')
        job.save()
        # Redirect to a success page or back to the job listing page
        return redirect('postjob')  # Change 'job_listing' to the appropriate URL name
        
    return render(request, 'editjob.html', {'job': job})

# deletejob
from django.shortcuts import render, redirect
from .models import Jobs

# def delete_job(request, job_id):
#     try:
#         job = Jobs.objects.get(id=job_id)
#         job.delete()
#         # Redirect to a different page (e.g., job list or any other appropriate page)
#         return redirect('postjob')  # Replace 'job_list' with the appropriate URL name
#     except Jobs.DoesNotExist:
#         # Handle the case where the job does not exist (you can show an error message or redirect to an error page)
#         return redirect('postjob')  # Redirect to the job list page or an error page as needed
from django.shortcuts import render, get_object_or_404, redirect
from .models import Jobs

def delete_job(request, job_id):
    # Get the job object by id
    job = get_object_or_404(Jobs, id=job_id)
    
    if request.method == 'POST':
        # Set the is_active field to False
        job.is_active = False
        job.save()  # Save the updated job object with is_active=False
        return redirect('postjob')  # Redirect to a suitable page after deletion

    return render(request, 'delete_job.html', {'job': job})

def CRegistration(request):
    return render(request, 'registration.html')


def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_index')  # Redirect to admin dashboard
        else:
            # Invalid credentials, handle error or show message
            pass
    
    return render(request, 'admin/admin_login.html')



#jobs_table_view 
from django.shortcuts import render
from .models import Jobs  # Import your Jobs model here


def jobslist(request):
    job_list= Jobs.objects.all()
    context = {'job_list': job_list}
    return render(request, 'admin/admin_jobtable.html', context)

# def job_list(request):
#     # Retrieve data from the Jobs model
#     joblist = Jobs.objects.all()
    
#     # Pass the data to the template
#     return render(request, 'job_list.html', {'joblist': joblist})

from django.shortcuts import render
from .models import CompanyProfile

def companyprofilelist(request):
    company_profiles = CompanyProfile.objects.all()
    return render(request, 'admin/companyprofilelist.html', {'company_profiles': company_profiles})


def addstudents(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        email = request.POST.get('email')
        # passw = request.POST.get('passw')
        # password=request.POST.get('password')
        course = request.POST.get('course')
        department = request.POST.get('department')
        semester = request.POST.get('semester')

        obj = Students()
        obj.sname = sname
        obj.email = email
        # obj.passw = passw
        # obj.password = password
        obj.course = course
        obj.department = department
        obj.semester = semester
        
        
        obj.save()
        messages.success(request, 'Student added successfully!')

       # Redirect to the doctors page
        return redirect('admin_poststudent')  # Redirect to the doctors page URL name
    
    return render(request, 'admin/student_add.html')












def admin_poststudent(request):
    stus=Students.objects.all()
    return render(request,'admin/admin_poststudent.html',{'stus': stus})

def search_company(request):
    if 'companyname' in request.GET:
        companyname = request.GET['companyname']
        # Perform the company name search, for example:
        company_profiles = CompanyProfile.objects.filter(companyname__icontains=companyname)
    else:
        company_profiles = CompanyProfile.objects.all()  # Display all company profiles if no search query

    return render(request, 'admin/companyprofilelist.html', {'company_profiles': company_profiles})

def search_student(request):
    studentname = request.GET.get('studentname', '')
    
    # Filter students based on the search query
    students = Students.objects.filter(sname__icontains=studentname)
    
    return render(request, 'admin/admin_poststudent.html', {'stus': students})


def edit_student(request):
    return render(request, 'edit_student.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Students

def edit_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    
    if request.method == 'POST':
        # Update student data based on form input
        student.sname = request.POST.get('sname')
        student.email = request.POST.get('email')
        student.password = request.POST.get('password')
        student.course = request.POST.get('course')
        student.department = request.POST.get('department')
        student.semester = request.POST.get('semester')
        student.save()
        return redirect('admin_poststudent')
    return render(request, 'admin/edit_student.html', {'student': student})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Students

def delete_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)

    # Mark the student as inactive
    student.is_active = False
    student.save()

    # Redirect to admin_poststudent view
    return redirect('admin_poststudent')

import os
from django.http import FileResponse
def download_criteria(request, job_id):
    # Get the job and retrieve the criteria file path
    job = get_object_or_404(Jobs, pk=job_id)
    criteria_path = job.criteria.path

    # Open the file for reading
    with open(criteria_path, 'rb') as file:
        response = FileResponse(file)
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(criteria_path)}"'
        return response
    

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        company_name = request.POST.get('company_name', None)
        headquarter = request.POST.get('headquarter', None)
        ceo = request.POST.get('ceo', None)
        contact = request.POST.get('contact', None)
        password = request.POST.get('password', None)
        confirmpassword = request.POST.get('confirmpassword',None)
        role = User.STUDENT

        if username and company_name  and email and contact and role:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('/signup')
            elif User.objects.filter(company_name=company_name).exists():
                messages.info(request, "Company name already exists")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('/signup')
            elif User.objects.filter(contact=contact).exists():
                messages.info(request, "Phone number already taken")
                return redirect('/signup')
            else:
                user = User(username=username, company_name=company_name, email=email, contact=contact, role=role)
                user.set_password(password)
                user.save()
    else:
        return render(request, 'registration.html')
    
    from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser  # Import your CustomUser model

def loginn(request):
    if request.method == "POST":
        username = request.POST['email']  # Assuming username is the role type
        password = request.POST['password']

        # Authenticate using your CustomUser model
        if username  and password:
              user = authenticate(request, username=username, password=password)
              if user is not None:
                   login(request, user)
                   
                   if request.user.role == CustomUser.ADMIN:
                       
                        return redirect('admin_index2')
                   
                   elif request.user.role == CustomUser.STUDENT:
                       
                        return redirect('sindex')
                   elif request.user.role == CustomUser.COMPANY:
                       
                        return redirect('cindex')
        else:
            messages.error(request, "Invalid login")
            return redirect('loginn')
    else:
        return render(request, 'login.html')


