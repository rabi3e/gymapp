from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

class Adherent(models.Model):
    SEX_TYPE = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    nom = models.CharField(_("Nom"), max_length=150)
    prenom = models.CharField(_("Prénom"), max_length=50)
    sexe = models.CharField(_("Sexe"), max_length=1, choices= SEX_TYPE)
    dte_naissance = models.DateField(_("Date de Naissance"), auto_now=False, auto_now_add=False)
    creation_dte = models.DateTimeField(_("Date d'enregistrement"),auto_now_add=True)
    save_by = models.ForeignKey(User, verbose_name=_(""), on_delete=models.PROTECT)
    image = models.ImageField(_("Image"), upload_to='Adherents')
    adresse = models.CharField(_("Adresse"), max_length=700)
    ville = models.CharField(_("Ville"), max_length=100)
    mail = models.EmailField(_("E-Mail"), max_length=654)
    tel = models.CharField(_("Téléphone"), max_length=10)

    def __str__(self):
        return self.nom, self.prenom

    def __unicode__(self):
        return 
    
    class Meta:
        verbose_name = 'Adherent'
        verbose_name_plural = 'Adherents'
