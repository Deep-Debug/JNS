from django.db import models

# Create your models here.


class Complain(models.Model):
    Complain_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    problem = models.CharField(max_length=40)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='media/pics')
    address=models.TextField(max_length=1000)
    zip=models.CharField(max_length=20)
    ward=models.CharField(max_length=20)
    solved=models.BooleanField(default=False)
    unsolved=models.BooleanField(default=True)
    date=models.DateField(auto_now=True)
    class Meta:
        db_table = "Complain"
    def _str_(self):
        return str(self.Complain_id)