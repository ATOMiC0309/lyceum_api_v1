from django.db import models


# Create your models here.
class Direction(models.Model):
    direction_name = models.CharField(max_length=150)
    direction_title = models.CharField(max_length=300)

    def __str__(self):
        return self.direction_name


class Teacher(models.Model):
    firstname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    image = models.ImageField(upload_to='Teachers/')
    job_title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, related_name='teachers')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Leader(models.Model):
    firstname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    image = models.ImageField(upload_to='Leaders/')
    job_title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class EducationDirect(models.Model):
    edu_name = models.CharField(max_length=200)
    edu_image = models.ImageField(upload_to='EducationDirects/')
    edu_place = models.IntegerField()
    edu_title = models.CharField(max_length=300)

    def __str__(self):
        return self.edu_name


class New(models.Model):
    new_image = models.ImageField(upload_to='News/')
    news_title = models.CharField(max_length=300)
    news_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.news_title


class Application(models.Model):
    firstname = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email_address = models.EmailField()
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class ActiveStudent(models.Model):
    group_name = models.CharField(max_length=150)
    group_image = models.ImageField(upload_to='ActiveGroups/')
    group_title = models.CharField(max_length=300)
    group_result = models.IntegerField()

    def __str__(self):
        return self.group_name
