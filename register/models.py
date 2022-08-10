from django.db import models
from django.utils.translation import gettext_lazy as _



class Waitlist(models.Model):
    email = models.EmailField(_('email address'), unique = True)


    def __str__(self) -> str:
        return f'{self.email}'