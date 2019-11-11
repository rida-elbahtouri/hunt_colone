from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
def home(request):
    products=Product.objects
    return render(request,'home/home.html',{'products':products})

@login_required(login_url="/accounts/singhup")
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['description'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product=Product()
            product.title=request.POST['title']
            product.description=request.POST['description']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='http://'+request.POST['url']

            product.icon=request.FILES['icon']
            product.image=request.FILES['image']
            product.date= timezone.datetime.now()
            product.hunter= request.user
            product.save()
            return redirect('/products/'+str(product.id))


        else:
            return render(request,'home/create.html',{'eror':'make sure all the field has been fulled'})



    else:

        return render(request,'home/create.html')


def details(request,product_id):
      product=get_object_or_404(Product,pk=product_id)
      return render(request,'home/details.html',{'product':product})

@login_required(login_url="/accounts/singhup")
def upvote(request,product_id):
    #make it upvotes one for user and next click do a -1
    #add some propety to the button like the defrent color when you all ready upvote it
    #make an other button with propety of -1 to total votes
    if request.method=='POST':
        product=get_object_or_404(Product,pk=product_id)
        product.votes_total +=1
        product.save()
        return redirect('/products/'+str(product.id))
