from django.db import models

# Create your models here.
class empmodel (models.Model):
    ename = models.CharField(max_length=50 , blank=True ,null=True)
    eage =  models.IntegerField()
    mail = models.CharField(max_length=100)
    ephno = models.CharField(max_length=50)
    esal = models.IntegerField()


    class Meta:
        db_table = "emp"


