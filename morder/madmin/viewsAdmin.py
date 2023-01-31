from django.shortcuts import render
from django.http import HttpResponse
from mshop.models import Orders, OrderUpdate, Products, MilmaCurrentOrder
# from milmaAdmin.models import CurOrder
from math import ceil


# Create your views here.

def index(request):
    form = Orders.objects.all()
    formdata = Orders.objects.values_list('order_id','name','curlocation','items_json')
    # print(formdata)
    context = {'form':form}
    return render(request, 'madmin/index.html', context)


def currentOrder(request):
    form = Orders.objects.all()
    formdata = Orders.objects.values_list('order_id','name','curlocation','items_json')
    prod = Products.objects.all()
    formlst1 = []
    formlst2 = []
    formlst3 = []
    formlst4 = []
    for i in range(len(formdata)):
        formlst1.append(formdata[i][0])
        formlst2.append(formdata[i][1])
        formlst3.append(formdata[i][2])
        formlst4.append(formdata[i][3])
        
    if request.method=="POST":
        for i in range((len(formlst1))):
            str1 = str(formlst1[i])
            orderstatus = request.POST.get('orderstatus_'+str1,'')
            if orderstatus=='order_accepted':
                order_id = formlst1[i]
                MilmaCurrentOrder.objects.filter(order_id=order_id).update(orderstatus=orderstatus)
                OrderUpdate.objects.filter(order_id=order_id).update(update_desc='Preparing your order')
                

            elif orderstatus=='order_delivered':
                order_id = formlst1[i]
                MilmaCurrentOrder.objects.filter(order_id=order_id).update(orderstatus=orderstatus)
                OrderUpdate.objects.filter(order_id=order_id).update(update_desc='Order has been delivered')
                MilmaCurrentOrder.objects.get(order_id=order_id).delete()
                
            if orderstatus != '' and orderstatus=="order_placed":
                order_id = formlst1[i]
                name = formlst2[i]
                # print(name)
                curlocation = formlst3[i]
                items_json = formlst4[i]
                curorder = MilmaCurrentOrder(orderstatus=orderstatus, order_id = order_id, name=name, items_json=items_json, curlocation=curlocation)
                # print(curorder)
                curorder.save()
                

    curord = MilmaCurrentOrder.objects.all()
    


    context = {'form':form, 'prod':prod, 'curord':curord}
    return render(request, 'madmin/curorder.html', context)
    



    

