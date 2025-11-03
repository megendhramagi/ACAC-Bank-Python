from django.shortcuts import render,redirect
from  .dataBaseMgt import *
# Create your views here.
def login(request):
    return render(request,'login.html',{})

def register(request):
    gAccNo=randomm(6)
    gPinNo=randomm(4)
    return render(request,'register.html',{"gAccNo":gAccNo,"gPinNo":gPinNo})

def portal(request):
    print(request.POST)
    uData=request.session.get('uData') #we first del the session and store in the uData aslo we use .get without del
    return render(request,'portal.html',{'uData':uData}) #pass like this db method(request.POST) for easy

def deposit(request):
    uData=request.session.get('uData') #getting only Avail bal and convert into int ( from uDATA session)
    accNo=uData[0][0]
    AvailBal=int(uData[0][5])
    depositAmt=int(request.POST['depAmt']) # get only depAmt from portal(depoist form)
    tot=AvailBal+depositAmt
    isOk=updateAmt(accNo,tot)
    if(isOk):
        uData[0][5]=tot
        uData[1]="Amount Depoisted Successfully" #o has value of usr datas and 1 is error msg
        request.session['uData']=uData
    else:
        uData[1]="Depoist Failed"
    return redirect('portal')
    #return render(request,'portal.html',{'emsg':"OK"})

def withdraw(request):
    uData=request.session.get('uData') #getting only Avail bal and convert into int ( from uDATA session)
    accNo=uData[0][0]
    AvailBal=int(uData[0][5])
    withdrawAmt=int(request.POST['withAmt']) # get only withAmt from portal(depoist form)
    if(withdrawAmt<=AvailBal):
        tot=AvailBal-withdrawAmt
        isOk=updateAmt(accNo,tot)
        if(isOk):
            uData[0][5]=tot
            uData[1]="Amount withdrawed Successfully" #o has value of usr datas and 1 is error msg
        else:
            uData[1]="withdrawal Failed | Server Error"
    else:
        uData[1]="withdrawal failed | Insufficent Amount"
    request.session['uData']=uData
    return redirect('portal')

def transfer(request):
    uData=request.session.get('uData') #getting only Avail bal and convert into int ( from uDATA session)
    accNo=uData[0][0]
    AvailBal=int(uData[0][5])
    transferacc=int(request.POST['tAccNo'])
    transferAmt=int(request.POST['tAmt'])
    if(transferAmt<=AvailBal):
        tot=AvailBal-transferAmt
        isOk1=updateAmt(accNo,tot)
        isOk2=updateTransferAmt(transferacc,transferAmt)
        if(isOk1 and isOk2):
            uData[0][5]=tot
            uData[1]="Amount Transfer Successfully"
        else:
            uData[1]="Transfer Failed | Server Error or invalid Transfer Snumber"
    else:
        uData[1]="Transfer failed | Insufficent Amount"
    request.session['uData']=uData
    return redirect('portal')
def logout(request):
    request.session.pop('uData')
    return redirect('login')

def loading(request): #do from here tommarrow
    print(request.POST)
    Credentials =request.POST
    if(len(Credentials)==3): # if its 3 come from login page, so we need to store some data
        isOk,usrData=loginDB(Credentials)
         #creating a str value for show result is amt depoisted success fully or not 
        print(usrData)
        if(isOk):
            usrData.append("")
            request.session['uData']=usrData
            #return redirect('portal')
            return render(request,'loading.html',{"purpose":"login","msg":"Logging in...."})
        else:
            return render(request,'login.html',{'emsg':'Login Failed..'})
    elif(len(Credentials)==8): # if its 5 its come from register page
        isOk=registerDB(Credentials) 
        print(isOk)
        print(Credentials)
        return render(request,'loading.html',{"purpose":"reg","isOk":isOk})
    else:
        return render(request,'loading.html')
    
    
