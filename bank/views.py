from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from bank.models import customer,transfer

def index(request):
    customers = customer.objects.all()
    blst = []
    ids = customer.objects.values('id')
    ct = 0
    for cust in customers:
        lst = []
        lst.append(ids[ct]['id'])
        lst.append(cust.user_name)
        lst.append(cust.user_mail)
        lst.append(cust.user_cbal)
        lst.append(cust.start_date)
        blst.append(lst)
        ct += 1
        
    return render(request,'bank/index.html',{'customers':blst})

def pay(request):
    amt = int(request.POST.get('a','def'))
    frome = int(request.POST.get('b','def'))
    toe = int(request.POST.get('c','def'))
    customers = customer.objects.all()
    tp = customer.objects.values('id')
    tp = [ k['id'] for k in tp ]
    if toe in tp:
        tid = tp.index(toe)
        fid = tp.index(frome)
        for x in customers[tid:tid+1]:
            x.user_cbal += amt
            x.save()
        for x in customers[fid:fid+1]:
            x.user_cbal -= amt
            x.save()
        a = transfer()
        a.fro_user_id = frome      
        a.to_user_id = toe
        a.amt_transf = amt
        a.save()      

    else:
        msg = "Transaction failed due to wrong input Id"
        msg += "<br><a href='/home/'>Go to HomePage</a>"
        return HttpResponse(msg)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def addcus(request):
    a = customer()
    a.user_name = request.POST.get('name','default')
    a.user_mail = request.POST.get('mail','default')
    a.user_cbal = request.POST.get('cbal','default')
    a.start_date = request.POST.get('date','default')
    a.save()
    flg = 1
    return render(request,'bank/addcus.html',{'flg':flg})

def addcus2(request):
    return render(request,'bank/addcus2.html')

def transfers(request):
    tfs = transfer.objects.all()
    tlast = []
    ids = transfer.objects.values('id')
    ct = 0
    for transf in tfs:
        lst = []
        lst.append(ids[ct]['id'])
        lst.append(transf.fro_user_id)
        lst.append(transf.to_user_id)
        lst.append(transf.amt_transf)
        lst.append((transf.tr_date).strftime("%d/%m/%Y"))
        lst.append((transf.tr_time).strftime("%H:%M:%S"))
        tlast.append(lst)
        ct += 1
    
    return render(request,'bank/transfers.html',{'transfers':tlast})

# Create your views here.
