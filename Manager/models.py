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

# Create your models here.
class Message(models.Model):
    sender_id = models.CharField(max_length=30)
    receiver_id = models.CharField(max_length=30)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Line_Messages'
