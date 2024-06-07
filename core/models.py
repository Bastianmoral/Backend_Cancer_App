from django.db import models

# Create your models here.

class CancerType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Gene(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Drug(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Test(models.Model):
    code = models.CharField(max_length=100)
    genes = models.ManyToManyField(Gene)
    
    def __str__(self):
        return self.name

class CancerGeneDrug(models.Model):
    cancer = models.ForeignKey(CancerType, on_delete=models.CASCADE)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    tests = models.ManyToManyField(Test)

class DrugAvailability(models.Model)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    institute = models.CharField(max_length=100, default="ISP Inst Salud Pública de Chile")