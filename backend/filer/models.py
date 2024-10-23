from django.db import models

class Filer(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['uploaded_at']
        
    def __str__(self):
        return self.name