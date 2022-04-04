from django.db import models
from django.core.validators import MinValueValidator


from apps.poll.choices import gender_choices,age_range

# Create your models here.

'''We created the Social Network model to be able to scale the application in the future.'''

class SocialNetwork(models.Model):
    name = models.CharField(verbose_name='Red Social',max_length=255,blank=False,null=False)

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['pk']
    
    def __str__(self):
        return self.name

class Poll(models.Model):
    email = models.EmailField(verbose_name='Correo Electronico',max_length=255,blank=False,null=False,unique=True)
    age = models.CharField(verbose_name='Edad',max_length=15, choices=age_range, default='18-25',null=False,blank=False)
    gender = models.CharField(verbose_name='Sexo',max_length=10, choices=gender_choices, default='male',null=False,blank=False)
    favorite_sn = models.ForeignKey(SocialNetwork,verbose_name='Red Social',on_delete=models.CASCADE)
    time_avg_facebook = models.DecimalField(verbose_name='Tiempo promedio en Facebook',decimal_places=2,max_digits=6,validators=[MinValueValidator(0)],blank=False,null=False,default=1.5)
    time_avg_whatsapp = models.DecimalField(verbose_name='Tiempo promedio en Whatsapp',decimal_places=2,max_digits=6,validators=[MinValueValidator(0)],blank=False,null=False,default=1.5)
    time_avg_twitter = models.DecimalField(verbose_name='Tiempo promedio en Twitter',decimal_places=2,max_digits=6,validators=[MinValueValidator(0)],blank=False,null=False,default=1.5)
    time_avg_instagram = models.DecimalField(verbose_name='Tiempo promedio en Instagram',decimal_places=2,max_digits=6,validators=[MinValueValidator(0)],blank=False,null=False,default=1.5)
    time_avg_tiktok = models.DecimalField(verbose_name='Tiempo promedio en Tiktok',decimal_places=2,max_digits=6,validators=[MinValueValidator(0)],blank=False,null=False,default=1.5)

    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'
        

    def __str__(self):
        return f'No:{self.pk} {self.email}'