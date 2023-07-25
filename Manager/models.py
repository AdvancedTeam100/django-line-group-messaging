from django.db import models

# Create your models here.
class Manager(models.Model):
    MemberId = models.CharField(max_length=30)
    Name = models.CharField(max_length=50)
    Group_Name = models.CharField(max_length=300)
    etc = models.CharField(max_length=300)
    Start_Date = models.DateField()
    End_Date = models.DateField()

    class Meta:
        db_table = 'Line_Memebers'