from django.db import models

# Create your models here.
class Drive(models.Model):
    DEPARTMENT_CHOICES = [
        ('Civil Engineering With Computer Applications', 'Civil Engineering With Computer Applications'),
        ('Robotics and Artificial Intelligence', 'Robotics and Artificial Intelligence'),
        ('Mechanical and Mechatronics Engineering (Additive Manufacturing)', 'Mechanical and Mechatronics Engineering (Additive Manufacturing)'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Electronics and Computer Engineering', 'Electronics and Computer Engineering'),
        ('Electrical and Computer Engineering', 'Electrical and Computer Engineering'),
        ('Computer Science and Engineering', 'Computer Science and Engineering'),
        ('Civil Engineering (Construction Technology)', 'Civil Engineering (Construction Technology)'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Artificial Intelligence and Data Science', 'Artificial Intelligence and Data Science'),
        ('Architecture', 'Architecture'),
    ]
     
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=30)
    comany_logo = models.ImageField(null=True,blank=True)
    date = models.DateField()
    content = models.TextField()
    Bond = models.CharField(max_length=50)
    industy_type = models.CharField(max_length=50) 
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    job_role = models.CharField(max_length=50)
    job_location = models.CharField(max_length=50)
    job_eligibility = models.TextField()
    selection_process = models.TextField()
    job_CTC = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    drive_id = models.AutoField(primary_key=True)


    def __str__(self):
        return self.title
    class Meta:
        ordering = ['creation_date']