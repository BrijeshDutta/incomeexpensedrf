from django.db import models
from authentication.models import User

# Income model

class Income(models.Model):
    
    "Adding mutiple choices for a field"
    
    SOURCE_OPTIONS = [
        ('SALARY','SALARY'),
        ('BUSINESS','BUSINESS')
    ]
    
    source = models.CharField(choices=SOURCE_OPTIONS, max_length=265)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    date = models.DateField(null=False,blank=False)
    
    
    class Meta:
        ordering:['-date']
        
    
    def __str__(self):
        return str(self.owner)
    