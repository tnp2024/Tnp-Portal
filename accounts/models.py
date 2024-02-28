from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('coordinator', 'Coordinator'),
        ('tnpoffice', 'TnpOffice'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')

class TNPAdmin(AbstractUser):
    T_ID = models.CharField(max_length=20, unique=True)
    T_PH_NO = models.PositiveIntegerField()
    T_profilepicture = models.ImageField(upload_to='tnp_admin_profile_pics/', null=True, blank=True)

    class Meta:
        unique_together = ['username']  # Example of enforcing uniqueness

    # Adding unique related_name for user_permissions and groups
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='tnpadmin_user_permissions',
        related_query_name='tnpadmin_user_permission',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='tnpadmin_groups',
        related_query_name='tnpadmin_group',
    )

class Coordinator(CustomUser):
    C_ID = models.CharField(max_length=20, unique=True)
    C_PH_NO = models.PositiveIntegerField()
    C_profilepicture = models.ImageField(upload_to='coordinator_profile_pics/', null=True, blank=True)

    class Meta:
        unique_together = ['username']  # Example of enforcing uniqueness

    # Adding unique related_name for user_permissions and groups
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='coordinator_user_permissions',
        related_query_name='coordinator_user_permission',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='coordinator_groups',
        related_query_name='coordinator_group',
    )

class Student(AbstractUser):
    S_PRN = models.IntegerField(unique=True)
    S_DOB = models.DateField()
    S_GENDER = models.CharField(max_length=10)
    S_AGE = models.IntegerField()
    S_EMAIL = models.EmailField()
    S_MOBILE_NO = models.IntegerField()
    S_ALT_MOBILE_NO = models.IntegerField()
    S_LOCAL_ADDRESS = models.CharField(max_length=255)
    S_PERMANENT_ADDRESS = models.CharField(max_length=255)
    S_NATIVE_PLACE = models.CharField(max_length=255)
    X_PERCENTAGE = models.IntegerField()
    X_YEAR_OF_PASSING = models.IntegerField()
    X_BOARD = models.CharField(max_length=255)
    XII_PERCENTAGE = models.IntegerField()
    XII_YEAR_OF_PASSING = models.IntegerField()
    XII_BOARD = models.CharField(max_length=255)
    Diploma_percentage = models.IntegerField()
    Diploma_year_of_passing = models.IntegerField()
    Diploma_college = models.CharField(max_length=255)
    Diploma_branch = models.CharField(max_length=255)
    Admission_Type = models.CharField(max_length=255)
    Engg_year_of_passing = models.IntegerField()
    SEM_1_sgpa = models.IntegerField()
    SEM_1_sgpa_marksheet = models.ImageField(upload_to='sgpa_marksheets/', null=True, blank=True)
    SEM_2_sgpa = models.IntegerField()
    SEM_2_sgpa_marksheet = models.ImageField(upload_to='sgpa_marksheets/', null=True, blank=True)
    SEM_3_sgpa = models.IntegerField()
    SEM_3_sgpa_marksheet = models.ImageField(upload_to='sgpa_marksheets/', null=True, blank=True)
    SEM_4_sgpa = models.IntegerField()
    SEM_4_sgpa_marksheet = models.ImageField(upload_to='sgpa_marksheets/', null=True, blank=True)
    SEM_5_sgpa = models.IntegerField()
    SEM_5_sgpa_marksheet = models.ImageField(upload_to='sgpa_marksheets/', null=True, blank=True)
    SEM_6_sgpa = models.IntegerField()
    SEM_6_sgpa_marksheet = models.ImageField(upload_to='sgpa_marksheets/', null=True, blank=True)
    SEM_7_sgpa = models.IntegerField()
    SEM_7_sgpa_marksheet = models.ImageField(upload_to='sgpa_marksheets/', null=True, blank=True)
    SEM_8_sgpa = models.IntegerField()
    SEM_8_sgpa_marksheet = models.ImageField(upload_to='sgpa_marksheets/', null=True, blank=True)
    AVG_TILL_SEM_cgpa = models.IntegerField()
    AVG_TILL_SEM_percentage = models.IntegerField()
    Live_backlogs = models.IntegerField()
    Dead_backlogs = models.CharField(max_length=255)
    Year_gap = models.CharField(max_length=255)
    Preference_1 = models.CharField(max_length=255)
    Preference_2 = models.CharField(max_length=255)
    Preference_3 = models.CharField(max_length=255)
    Placed = models.CharField(max_length=255)
    S_profilepicture = models.ImageField(upload_to='students_profile_pics/', null=True, blank=True)

    def calculate_average_and_percentage(self):
        # Create a list of SGPA values for the semesters
        sem_sgpa_fields = [self.SEM_1_sgpa, self.SEM_2_sgpa, self.SEM_3_sgpa, self.SEM_4_sgpa, self.SEM_5_sgpa, self.SEM_6_sgpa, self.SEM_7_sgpa, self.SEM_8_sgpa]

        # Filter out None values and then calculate the average
        valid_sgpa_values = [sgpa for sgpa in sem_sgpa_fields if sgpa is not None]
        
        if valid_sgpa_values:
            avg_cgpa = sum(valid_sgpa_values) / len(valid_sgpa_values)
            self.AVG_TILL_SEM_cgpa = round(avg_cgpa, 2)
            
            # Calculate percentage (assuming 10 is the maximum SGPA)
            max_sgpa = 10
            percentage = (avg_cgpa / max_sgpa) * 100
            self.AVG_TILL_SEM_percentage = round(percentage, 2)

    def save(self, *args, **kwargs):
        self.calculate_average_and_percentage()  # Calculate before saving
        super(Student, self).save(*args, **kwargs)

    # Adding unique related_name for user_permissions and groups
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='student_user_permissions',
        related_query_name='student_user_permission',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='student_groups',
        related_query_name='student_group',
    )

    department = models.OneToOneField('notices.Department', on_delete=models.CASCADE, null=True, blank=True, related_name='student_department')
