from django.shortcuts import render,redirect
from django.http import HttpRequest,JsonResponse
from django.core.mail import EmailMessage
from .models import Register,Login,Contact,Course,Test
from django.contrib import messages
import random
import hashlib
import json







def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        contact=Contact()
        contact.name=name
        contact.phone=phone
        contact.save()
        messages.success(request,"Will contact you shortly")
        return redirect('index')

   

    return render(request,'index.html')



def register(request):

    if "email" in request.session:
        return redirect('dashboard')

    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        hobbies=request.POST.getlist('hobbies')
        avatar=request.FILES.get('avatar')
        register=Register()
        if Register.objects.filter(email=email).exists():
            messages.warning(request,'Email already exists')
            return redirect('register')
        else:
            try:
                register.firstname=firstname
                register.lastname=lastname
                register.dob=dob
                register.gender=gender
                register.email=email
                register.phone=phone
                register.country=country
                register.state=state
                register.city=city
                register.hobbies=hobbies
                register.avatar=avatar
                mail=EmailMessage('Registration',f'{firstname} you are successfully registered',"dd",[email])
                mail.send()
                register.save()
                messages.success(request, 'You are successfully registered!')
                return redirect('register')
            except:
                messages.error(request,'unable to send')
           
            
            # qw=Register.objects.get(email=email)
            # print(qw.firstname)
            
        
            return redirect('register')
   
        

        

    return render(request,'register.html')



def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('message')
        message=request.POST.get('message')
        to="hashifs228@gmail.com"
        contact=Contact()
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()

        try:
            EmailMessage(subject,message,'',[to]).send()
            EmailMessage("Enquiry","Thanks for the enquiry.We will contact you shortly",to,[email]).send()
            messages.error(request,"sent successfully")
            return redirect('contact')
        except:
            messages.error(request,'unable to send')

    return render(request,'contact.html')


def course(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        contact=Contact()
        contact.name=name
        contact.phone=phone
        contact.save()
        messages.success(request,"Will contact you shortly")
        return redirect('course')




    return render(request,'course.html')


def logout(request):

    if request.method == 'POST':
        request.session.flush()
        return redirect('login')
    else:
        return redirect('dashboard')

    
    # request.session.flush()  
    # return redirect('login')


def knowus(request):
    return render(request,'knowus.html')


def hea(request):
    return render(request,'hea.html')





def signup(request):
    if 'pass' in request.session:
        return redirect('password')

    otpview=request.session.get('otp',None)
    if 'email' in request.session:
        return redirect(login)

    if request.method=='POST':

        username=request.POST.get('username')
        otp=request.POST.get('otp')
        # otpp=request.POST.get('otp')
        login=Login.objects.filter(email=username)



        if login.exists():
            messages.error(request,'already exists')
            return redirect('signup')

        
        elif not otpview:
            if Register.objects.filter(email=username).exists():
                
                try:
                    otpmail=random.randrange(100001,855555)
                    
                    request.session['otp']=otpmail
                    request.session['userr'] = username
                    otpview=request.session.get('otp',None)
                    
                    
                    qqq= EmailMessage("otp",f'your otp is {otpmail}',"",[username])
                    qqq.send()
                    
                    # request.session['user'] = username

                    print(otpmail)
                except:
                    request.session.pop('otp',None)
                    request.session.pop('userr',None)
                    return redirect('signup')
        else:   
            z=str(request.session.get('otp'))
         
            if otp==z:
                request.session['pass']=True
                return redirect('password')
                


            else:
                print(otp)
                print('invalid')
                if otp=="":
                    messages.error(request,'otp should not be empty')
                elif not otp.isdigit():
                    messages.error(request,'only numbers')

                elif len(otp)!=6:
                    messages.error(request,'Otp is 6 digits')
                else:

                    messages.error(request,'invalid otp')
                    return redirect('signup')


                
                
            



    return render(request,'signup.html',{'otpview':otpview})



def password(request):
    if 'pass' in request.session:
        request.session.pop('otp',None)
        r=str(request.session.get('userr'))
        print(r)
        password=request.POST.get('password')
        cpassword=request.POST.get('confirmpassword')
        if request.method=="POST":
            if password==cpassword:
                passwordd=Login()
                hpassword=hashlib.sha256(password.encode('utf-8')).hexdigest()

                passwordd.email=r
                passwordd.password=hpassword
                passwordd.save()
                request.session.pop('pass',None)
                return redirect('login')
            else:
                messages.error(request,'password do not match')

    else:
        return redirect('login')

    
    return render(request,'password.html')



def login(request):

    if 'email' in request.session:
            return redirect('dashboard')


    if request.method=="POST":
        
        # data=json.loads(request.body)
        username=request.POST.get('email')
        password=request.POST.get('password')
        login=Login()
        if Login.objects.filter(email=username).exists():
            g=Login.objects.get(email=username)
            print(g.password)
            hpassword=hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hpassword==g.password:
                request.session['email']=username
                return redirect('dashboard')
            else:
                messages.error(request,"Incorrect Password",extra_tags='passw')
                return redirect('login')


        else:
            messages.error(request,"Not signed up",extra_tags='emai')
            # print(data.get("emailo"))
            return redirect('course')



    return render(request,'login.html')


def dashboard(request):
     if 'email' in request.session:

        register=Register.objects.get(email=request.session.get('email'))
        login=Login.objects.get(email=request.session.get('email'))
        w=login.coursesselected


        if w is None:
            c=""
            y="0"

        else:
            fin=w.split(",")
            y=len(fin)
            # print(y)
            c=[]
            for i in range(y):
                c.append(f'({i+1}){fin[i]}')
            print(c)
            
        

        
        

        
        # courses=Course.objects.all()
        
        
        return render(request,'dashboard.html',{'register':register,'login':login,'co':c,'t':y})
     else:
        return redirect('login')

        

def dashboardcourse(request):
     



     if 'email' in request.session:
            courses=Course.objects.all()
            # print(courses)
     else:
            return redirect('login')
      
     
     

     if request.method == 'POST':
        try:
            data = json.loads(request.body)
            course_name = data.get('cs')
            ga=Login.objects.get(email=request.session.get('email'))
            if ga.coursesselected is None:
                ga.coursesselected=course_name
                ga.save()


            elif course_name in ga.coursesselected:
                pass
            else:
                ga.coursesselected+=','+course_name
                ga.save()

            # if course_name not in ga.coursesselected:
            #     ga.coursesselected+=','+course_name
            #     ga.save()
            
            



        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        



        

     return render(request,'dashboardcourse.html',{'courses':courses})





def editprofile(request):
    register=Register.objects.get(email=request.session.get('email'))


    if request.method=="POST":
        register=Register.objects.get(email=request.session.get('email'))
        login=Login.objects.get(email=request.session.get('email'))
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        profilephoto=request.FILES.get('profilephoto')
        if profilephoto:
            register.avatar=profilephoto
        else:
            pass


        
        register.firstname=firstname
        register.lastname=lastname
        register.email=email
        login.email=email
        register.phone=phone
        

        register.save()
        login.save()
        request.session.pop('email',None)
        request.session['email']=email
        messages.success(request,'Profile updated')
        return redirect('dashboard')

    return render(request,'editprofile.html',{'register':register})



def changepassword(request):
    if not 'email' in request.session:
        return redirect('login')
       
    if request.method=='POST':
        current=request.POST.get('currentpassword')
        newpassword=request.POST.get('password')
        confirm=request.POST.get('confirmpassword')
        
        if newpassword==confirm:
            email=request.session.get('email')
            login=Login.objects.get(email=email)
            hcurrent=hashlib.sha256(current.encode('utf-8')).hexdigest()
            hpassword=hashlib.sha256(newpassword.encode('utf-8')).hexdigest()
        
            
            if hcurrent==login.password:
                login.password=hpassword
                login.save()
                request.session.pop('email',None)
                return redirect ('login')
            else:
                messages.error(request,'password incorrect')
        else:
            messages.error(request,'new and confirm donot match')
                    
                    



    return render(request,'changepassword.html')

def placement(request):
    d=range(1) 
    return render(request,'placement.html',{'d':d})

def courses(request):
    return render(request,'courses.html')

def python(request):

    return render(request,'python.html')



def java(request):

    return render(request,'java.html')


def flutter(request):
    return render(request,'flutter.html')


def php(request):
    return render(request,'php.html')



def asp(request):
    return render(request,'asp.html')


def aws(request):
    return render(request,'aws.html')


def azure(request):
    return render(request,'azure.html')


def digitalmarketing(request):
    return render(request,'digitalmarketing.html')


def rhcsa(request):
    return render(request,'rhcsa.html')


def rhce(request):
    return render(request,'rhce.html')



def networking(request):
    return render(request,'networking.html')


def microsoftbi(request):
    return render(request,'microsoftbi.html')


def mern(request):
    return render(request,'mern.html')


def mean(request):
    return render(request,'mean.html')


def ionic(request):
    return render(request,'ionic.html')

def devops(request):
    return render(request,'devops.html')



def datascience(request):
    return render(request,'datascience.html')



def dataanalytics(request):
    return render(request,'dataanalytics.html')


def softwaretesting(request):
    return render(request,'softwaretesting.html')


def webdesign(request):
    return render(request,'webdesign.html')



def ccna(request):
    return render(request,'ccna.html')



def uiux(request):
    if request.method=='GET':
        a=json.loads(request.body)
        
        print(a.get('der'))
        
    return render(request,'uiux.html')


from django.views.generic.edit import CreateView,DeleteView

from django.views.generic import DetailView



class Det(DetailView):
    model=Test
    context_object_name='course'
    template_name='Det.html'

class Cre(CreateView):
    model=Test
    fields=['course','fee','duration']
    template_name='Cre.html'
    success_url = '/myapp/login/'


class Del(DeleteView):
    model=Test
    template_name='del.html'
    success_url = '/myapp/login/'




























