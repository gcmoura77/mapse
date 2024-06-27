from django.db import models

class TimeStampedModel(models.Model):
    created      = models.DateTimeField(auto_now_add=True)
    modified     = models.DateTimeField(auto_now =True)
    # created_by   = models.ForeignKey("User", on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
