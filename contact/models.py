from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=450)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'Message from {self.name}'