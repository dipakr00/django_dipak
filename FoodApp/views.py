from django.shortcuts import render
from .models import Food,Consume_Food

# Create your views here.

def Home(request):
    if request.method=='POST':
        consumed_food=request.POST.get('food_consumed')
        comsume=Food.objects.get(name=consumed_food)
        user=request.user
        consume=Consume_Food(user=user,food_consumed=consume)
        consume.save()
        food=Food.object.all()
    else:
        food=Food.objects.all() 
    consumed_food=Consume_Food.filter(user=request.user)   
    return render(request,'Home.html',{'food':food,'consume_food':consumed_food})
