from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.urls import reverse

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    profile_pic=models.ImageField(upload_to='contact_pic',blank=True)
    # phonenumber = PhoneNumberField(blank=True)
    phonenumber=models.CharField(max_length=10)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    def __str__(self):
        return self.full_name()
    def get_absolute_url(self):
        return reverse("contactapp:contact_detail",kwargs={'pk':self.pk})

