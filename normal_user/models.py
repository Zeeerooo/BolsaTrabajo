from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class EmailConfirmation(models.Model):
    '''
    EmailConfirmation es una tabla que relaciona User con la fecha del envio del mail y el string aleatorio de verificacion.
    La fecha sirve para expirar la cuenta y no haya confirmado la cuenta.
    '''
    user = models.OneToOneField('auth.user')
    sent = models.DateTimeField(default=datetime.now,blank=True)
    code = models.CharField(max_length=40)

    def key_expired(self):
        expiration_date = self.sent + timedelta(
            days=settings.EMAIL_CONFIRMATION_DAYS) #definir EMAIL_CONFIRMATION_DAYS
        return expiration_date <= datetime.now()
    def __unicode__(self):
        return 'Email de confirmacion para '+ self.user.email