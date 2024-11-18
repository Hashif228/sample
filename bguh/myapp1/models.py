from django.db import models

# Create your models here.
# if 57026997445==57026997445:
#     print('hi')
class Register(models.Model):
    # id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=52)
    lastname=models.CharField(max_length=52)
    dob=models.DateField(max_length=52)
    gender=models.CharField(max_length=52)
    email=models.CharField(max_length=52)
    phone=models.CharField(max_length=52)
    country=models.CharField(max_length=52)
    state=models.CharField(max_length=52)
    city=models.CharField(max_length=52)
    hobbies=models.JSONField(max_length=52)
    avatar=models.ImageField(max_length=502,upload_to='files/',default='files/hs_aXjcotW.png')



    def __str__(self):
        return self.firstname


class Login(models.Model):
    email=models.CharField(max_length=52)
    password=models.CharField(max_length=152,null=True)
    coursesselected=models.CharField(max_length=585,null=True)
    # ids = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.email
        




class Contact(models.Model):
    name=models.CharField(max_length=52)
    phone=models.CharField(max_length=52,default='nil')
    email=models.CharField(max_length=52,default='nil')
    subject=models.CharField(max_length=52,default='nil')
    message=models.CharField(max_length=52,default='nil')
    def __str__(self):
        return self.name
    





class Course(models.Model):
    course=models.CharField(max_length=52)
    duration=models.CharField(max_length=52)
    fee=models.CharField(max_length=52)

    def __str__(self):
        return self.course
    

class Test(models.Model):
    course=models.CharField(max_length=52)
    duration=models.CharField(max_length=52)
    fee=models.CharField(max_length=52,unique=True)

    def __str__(self):
        return self.course