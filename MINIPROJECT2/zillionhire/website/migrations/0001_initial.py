# Generated by Django 4.2.4 on 2023-09-16 16:12

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('jname', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('sdate', models.CharField(max_length=100)),
                ('edate', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('criteria', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('course', models.CharField(choices=[('B.Tech', 'B.Tech'), ('MCA', 'MCA')], max_length=50)),
                ('department', models.CharField(choices=[('ECE', 'ECE'), ('CSE', 'CSE'), ('Integrated MCA', 'Integrated MCA'), ('Regular MCA', 'Regular MCA')], max_length=100)),
                ('semester', models.CharField(choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8'), ('Semester 9', 'Semester 9'), ('Semester 10', 'Semester 10')], max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('confirmpassword', models.CharField(max_length=128)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ceo', models.CharField(blank=True, max_length=100, null=True)),
                ('headquarters', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=15, null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'student'), (2, 'company'), (3, 'alumni'), (4, 'admin')], default='1', null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_groups', related_query_name='customuser_group', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_permissions', related_query_name='customuser_permission', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'website_customuser',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(default='default', max_length=100)),
                ('headquarter', models.CharField(default='default', max_length=100)),
                ('ceo', models.CharField(default='default', max_length=100)),
                ('contact', models.CharField(default='default', max_length=15)),
                ('addressline1', models.CharField(blank=True, max_length=100)),
                ('website', models.CharField(default='www.example.com', max_length=100)),
                ('city', models.CharField(default=' eg: Kochi', max_length=100)),
                ('district', models.CharField(default=' eg:Ernakulam', max_length=100)),
                ('state', models.CharField(default=' eg:Kerala ', max_length=100)),
                ('country', models.CharField(default=' eg: India', max_length=100)),
                ('pincode', models.CharField(default=' eg:686403', max_length=15)),
                ('companydp', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
