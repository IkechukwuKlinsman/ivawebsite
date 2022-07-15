from django.db import models
from django.utils.translation import gettext_lazy as _



class Waitlist(models.Model):
    first_name = models.CharField(_('first name'), max_length= 500)
    last_name = models.CharField(_('last name'), max_length= 500)
    email = models.EmailField(_('email address'), unique = True)


    def __str__(self) -> str:
        return f'{self.email}'