from django.db import models

class Contact(models.Model):
    name = models.TextField();
    email = models.EmailField();
    sub = models.TextField();
    msg = models.TextField();
    
    def __str__(self):
        return self.name +" "+ str(self.id)
