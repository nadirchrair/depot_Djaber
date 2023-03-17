from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.timezone import get_current_timezone
from datetime import datetime

class Depot(models.Model):
    admin = models.OneToOneField(User,on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.nom

class Category(models.Model):
    nom = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.nom

class Produit(models.Model):
    depot = models.ForeignKey(Depot,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)    
    quantity_Init = models.IntegerField()
    quantity_Act = models.IntegerField(default=0)
    quantity_Vend = models.IntegerField(default=0)
    prix_u_TTC = models.FloatField()
    prix_vente_TTC = models.FloatField(default=0)
    total_achat = models.FloatField(default= 0)
    total_vendu = models.FloatField(default=0)
    benefice = models.FloatField(default=0)
    
    def save(self,*args, **kwargs):
        self.total_achat = self.prix_u_TTC * self.quantity_Init
        self.quantity_Act = self.quantity_Init - self.quantity_Vend
        self.total_vendu = self.quantity_Vend * self.prix_vente_TTC
        if self.total_vendu ==0 :
            self.benefice=0
        else  :  
         self.benefice = self.total_vendu - (self.quantity_Vend *self.prix_u_TTC)  
        super(Produit,self).save(*args, **kwargs)
    def __str__(self):
        return self.designation
class Vente(models.Model):
    produit = models.ForeignKey(Produit,on_delete=models.PROTECT)
    quantity_Vendu = models.IntegerField()
    total_vente = models.FloatField(default=0)
    vendu_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.produit.designation
        
    def save(self, *args, **kwargs):
        self.total_vente = self.produit.prix_vente_TTC * self.quantity_Vendu
        if self.produit.quantity_Act < self.quantity_Vendu:
            raise ValidationError('The quantity sold is greater than the available quantity.')
        else:
            
            self.produit.quantity_Vend =  self.quantity_Vendu+self.produit.quantity_Vend
            self.produit.save()
            super(Vente, self).save(*args, **kwargs)
            
class Operation(models.Model):
    Point_Depart= models.CharField(max_length=50)
    Point_darrivée= models.CharField(max_length=50)
    prix_Transport = models.IntegerField(default=0)
    date_depart = models.DateField(null=True,blank=True)
    prix_de_facture= models.FloatField()
    clarque = models.FloatField(null=True,blank=True,default=True)
    Pallete = models.FloatField(null=True,blank=True,default=True)
    Total = models.FloatField(null=True,blank=True,default=True)
    def save(self,*args, **kwargs):
        self.Total = self.prix_Transport + self.prix_de_facture + self.clarque + self.Pallete
        super(Operation,self).save(*args, **kwargs)

    def __str__(self):
        return self.Point_Depart+self.Point_darrivée