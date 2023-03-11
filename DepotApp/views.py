from django.shortcuts import render ,redirect 
from .models import * 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LoginView 
from django.urls import reverse_lazy 
from django.http import HttpResponseForbidden  
from .forms import *
from django.urls import reverse 
from django.shortcuts import get_object_or_404  
from django.contrib.auth import logout
from .filters import *
from datetime import datetime




class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('depots')
    
    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('depots')
        else:
            depot = Depot.objects.filter(admin = self.request.user)
            if depot.exists() :
                depot = Depot.objects.get(admin=self.request.user)
                url = reverse('AcueilPage', args=[depot.id])
                return url       
        return super().get_success_url()
    def form_valid(self, form):
        if not self.request.user.is_superuser:
            print(self.request.user.username)
        return super().form_valid(form)


@login_required(login_url='/login')
def AllDepot(request):
    depots=  Depot.objects.all()
    depot={
        'depot':depots
    }
    
    return render(request, 'Depots/Alldepots.html',depot)


@login_required(login_url='/login')
def AjouterProduit(request,id):
    depot=Depot.objects.get(id=id)
    Produitform=ProduitForm(initial={'depot': depot})

    if request.method == 'POST':
        Produitform = ProduitForm(request.POST)
        if Produitform.is_valid():
            Produitform.save()
            return redirect('AllProduct',id=id)
    context = {'form': Produitform}  
    return render(request,'Produit/AjouterProduit.html',context)


@login_required(login_url='/login')
def modifier_produit(request,id):
    produit = Produit.objects.get(id=id)
    if request.method == 'POST':
        produit_form = ProduitForm(request.POST,instance =produit)
        if produit_form.is_valid():
            produit_form.save()
        return redirect('AllProduct',id=produit.depot.id)    
    else:
        produit_form = ProduitForm(instance =produit)
    context = {
        'form':produit_form,
    }    
    return render(request,'Produit/modifie_produit.html',context)

@login_required(login_url='/login')
def AlLProduct(request,id):
    depot = Depot.objects.get(id=id)
    produit=  Produit.objects.filter(depot = depot)
    now = datetime.today()
    vent= Vente.objects.filter(produit__depot=depot,vendu_at=now)
    
    
    product={
        'produit':produit,
        'depot':depot,
        'vente': vent,
    }    
    return render(request,'Produit/AllProduct.html',product)
@login_required(login_url='/login')
def AlLHistorique(request,id):
    depot = Depot.objects.get(id=id)
    produit=  Produit.objects.filter(depot = depot)
    vent= Vente.objects.filter(produit__depot=depot)
    
    myfilter = OperationFilter(request.GET,queryset=vent)
    vent=myfilter.qs
    
    product={
        'depot':depot,
        'vente': vent,
        'myfilter':myfilter
    }    
    return render(request,'Produit/AllVente.html',product)












@login_required(login_url='/login')
def AllOperation(request):

    operation= Operation.objects.all()
   

    operation={
        'operation':operation,


    }
    
    return render(request,'Operation/AllOperation.html',operation)


@login_required(login_url='/login')
def modificationOperation(request,id):
    operation = Operation.objects.get(id=id)
    if request.method == 'POST':
        operation_form = OperationForm(request.POST,instance =operation)
        if operation_form.is_valid():
            operation_form.save()
        return redirect('AllOperation')    
    else:
        operation_form = OperationForm(instance =operation)
    context = {
        'form':operation_form,
    }    
    return render(request,'Operation/modifie_Operation.html',context)
@login_required(login_url='/login')
def AjouterOperatione(request):
    Operationform=OperationForm()

    if request.method == 'POST':
        Operationform = OperationForm(request.POST)
        if Operationform.is_valid():
            Operationform.save()
            return redirect('AllOperation')
    context = {'form': Operationform}  
    return render(request,'Operation/AjouterOperation.html',context)



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            is_superuser = request.POST.get('is_superuser')
            print(is_superuser)
            if is_superuser == 1:
                user.is_superuser = is_superuser
            user.save()
            return redirect('AllAdmin')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signUp.html', {'form': form})




                                     
@login_required(login_url='/login')
def AllAdmin(request):
    user= User.objects.all()
    user={
        'user':user,
    }
    
    return render(request,'Admin/AllAdmin.html',user)
@login_required(login_url='/login')
def AcueilPage(request,id):
    depot = Depot.objects.get(id=id)
    produit=  Produit.objects.filter(depot = depot)
    vent= Vente.objects.filter(produit__depot=depot)
    context={
        'depot':depot,
        'vent':vent
    }
    return render(request,'Adminsecond/accueilPage.html',context)
@login_required(login_url='/login')
def AjouterVente(request,id):
    depot = get_object_or_404(Depot, pk=id)
    if request.method == 'POST':
      form = VenteForm(request.POST)
      if form.is_valid():
        vente = form.save(commit=False)
        vente.depot = depot  # set the depot attribute of the vente object
        vente.save()
        return redirect('AcueilPage',id=id)
    else:
     form = VenteForm()
     form.fields['produit'].queryset = Produit.objects.filter(depot=depot) # filter the produit choices based on the depot
    context = {'form': form}
    return render(request, 'Adminsecond/AjouterVente.html', context)
def user_logout(request):
    logout(request)
    return redirect('login')

