from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProduitForm(forms.ModelForm):
    class Meta:
        model= Produit
        fields= [
            'depot','category','designation','quantity_Init','prix_u_TTC','prix_vente_TTC'
        ]
        
        widgets = {
            'depot' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'designation' : forms.TextInput(attrs={'class':'form-control'}),
            'quantity_Init' : forms.NumberInput(attrs={'class':'form-control'}),
            'prix_u_TTC' : forms.NumberInput(attrs={'class':'form-control','step': "0.01"}),
            'prix_vente_TTC' : forms.NumberInput(attrs={'class':'form-control','step': "0.01"}),
        }

class VenteForm(forms.ModelForm):
    class Meta:
        model= Vente
        fields= [
            'produit','quantity_Vendu'
        ]
        
        widgets = {
            'produit' : forms.Select(attrs={'class':'form-control'}),
            'quantity_Vendu' : forms.NumberInput(attrs={'class':'form-control'}),
        }   
        def __init__(self, depot=None, **kwargs):
          super(VenteForm, self).__init__(**kwargs)
          if depot:
            self.fields['produit'].queryset = Produit.objects.filter(depot=depot)

class OperationForm(forms.ModelForm):
    class Meta:
        model= Operation
        fields= [
            'Point_Depart','Point_darrivée','prix_de_facture','clarque','date_depart','prix_Transport','Pallete'
        ]
        
        widgets = {
            'Point_Depart' : forms.TextInput(attrs={'class':'form-control'}),
            'Point_darrivée' : forms.TextInput(attrs={'class':'form-control'}),
            'prix_de_facture' : forms.NumberInput(attrs={'class':'form-control'}),
            'clarque' : forms.NumberInput(attrs={'class':'form-control'}),
            'prix_Transport' : forms.NumberInput(attrs={'class':'form-control'}),
            'date_depart' : forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
            'Pallete' : forms.NumberInput(attrs={'class':'form-control'}),

        }
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),

        }