from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

# from imagekit.processors import ResizeToFit
# from imagekit.models import ProcessedImageField

# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager

# from django.contrib.auth.models import AbstractUser
# # Create your models here.

# from .manager import UserManager

class UserManager(BaseUserManager):
    # ... (existing methods)
    
    def create_user(self, email, password=None, role=None, company_name=None, ceo=None, headquarters=None, contact=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
            company_name=company_name,
            ceo=ceo,
            headquarters=headquarters,
            contact=contact,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, company_name=None, ceo=None, headquarters=None, contact=None, role=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            company_name=company_name,
            ceo=ceo,
            headquarters=headquarters,
            contact=contact,
            role=role
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.role=4
        user.save(using=self._db)
        return user
    

# class CustomUser(AbstractUser):
#     COMPANY = 1
#     STUDENT = 2
#     ADMIN = 3

#     ROLE_CHOICE = (
#         (COMPANY, 'COMPANY'),
#         (STUDENT, 'STUDENT'),
#         (ADMIN, 'ADMIN'),
#     )

    # username = None
    # first_name = None
    # last_name = None
    # USERNAME_FIELD = 'email'
    # email = models.EmailField(max_length=100, unique=True)
    # password = models.CharField(max_length=128)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True, default=STUDENT)
    # company_name = models.CharField(max_length=100, blank=True, null=True)
    # ceo = models.CharField(max_length=100, blank=True, null=True)
    # headquarters = models.CharField(max_length=100, blank=True, null=True)
    # contact = models.CharField(max_length=15, blank=True, null=True)

#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superadmin = models.BooleanField(default=False)

#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True


class CustomUser(AbstractUser):
    STUDENT = 1
    COMPANY = 2
    ALUMNI = 3
    ADMIN = 4
    

    ROLE_CHOICE = (
        (STUDENT, 'student'),
        (COMPANY, 'company'),
        (ALUMNI, 'alumni'),
        (ADMIN , 'admin'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True,default='1')
    # role = models.CharField(max_length=20, choices=ROLE_CHOICE, default=STUDENT)
    username = models.CharField(max_length=100,unique=True)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirmpassword  = models.CharField(max_length=128)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    ceo = models.CharField(max_length=100, blank=True, null=True)
    headquarters = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    


    object = UserManager() 
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','company_name','headquarter','ceo','password','confirmpassword','contact','role']

    class Meta:
        # This will change the table name from "auth_user" to "website_customuser"
        db_table = 'website_customuser'

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_groups', related_query_name='customuser_group')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_permissions',
        related_query_name='customuser_permission'
    )
    def str(self):
        return self.name 



class Jobs(models.Model): 
    
    cname = models.CharField(max_length=100)
    jname = models.CharField(max_length=100)
    salary = models.IntegerField()
    email = models.EmailField(max_length=100)
    sdate = models.CharField(max_length=100)
    edate = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    criteria= models.ImageField(upload_to='images/',blank= True,null=True)

    def __str__(self):
        return self.email 



class CompanyProfile(models.Model): 
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=100, default="default")
    headquarter = models.CharField(max_length=100, default="default")
    ceo = models.CharField(max_length=100, default="default")
    contact = models.CharField(max_length=15,default="default")
    addressline1 = models.CharField(max_length=100, blank=True)
   
    website = models.CharField(max_length=100,default="www.example.com")
    city = models.CharField(max_length=100,default=" eg: Kochi")
    district= models.CharField(max_length=100,default=" eg:Ernakulam")
    state = models.CharField(max_length=100,default=" eg:Kerala ")
    country = models.CharField(max_length=100,default=" eg: India")
    pincode = models.CharField(max_length=15,default=" eg:686403")
    companydp=models.ImageField(upload_to='images/',blank= True,null=True)
    
    def __str__(self):
        return self.ceo
    
    # password = models.CharField(max_length=50)

    # def set_password(self, password):
    #      # Hash and set the password
    #      self.admin_set_password = make_password(password, default=make_password('default_password'))
class Students(models.Model): 
    
    sname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    # passw = models.CharField(max_length=100)
    # password = models.EmailField(max_length=100)
    course = models.CharField(max_length=50, choices=[('B.Tech', 'B.Tech'), ('MCA', 'MCA')])
    department = models.CharField(max_length=100, choices=[('ECE', 'ECE'), ('CSE', 'CSE'),('Integrated MCA', 'Integrated MCA'),('Regular MCA', 'Regular MCA')])
    semester = models.CharField(max_length=100, choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8'), ('Semester 9', 'Semester 9'), ('Semester 10', 'Semester 10')])
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.email 
 

 

   
   

 
 



     