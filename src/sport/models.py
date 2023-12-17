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
    image = models.ImageField(_("Image"), upload_to='Adherents',null=True,blank=True)
    adresse = models.CharField(_("Adresse"), max_length=700)
    ville = models.CharField(_("Ville"), max_length=100)
    mail = models.EmailField(_("E-Mail"), max_length=654,null=True,blank=True)
    tel = models.CharField(_("Téléphone"), max_length=10)
    acte_naissance = models.ImageField(_("Acte de Naissance"), upload_to='Adherents_acte',null=True,blank=True)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    class Meta:
        verbose_name = 'Adherent'
        verbose_name_plural = 'Adherents'

class Sport(models.Model):
    nom = models.CharField(_("Decipline"), max_length=50)
    jour = models.CharField(_("Jour"), max_length=150)
    prix = models.FloatField(_("Prix"))

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'

