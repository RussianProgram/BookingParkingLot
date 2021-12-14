from django.db import models
from django.conf import settings


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='employee',
                                on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

    ROLES = (
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20,
                            choices=ROLES,
                            default='employee')

    def __str__(self):
        return f'Employee:{self.user.username}'