from django.http import JsonResponse

from django.shortcuts import render, redirect
from .models import AdminUser, AddProperty, PageContent1, Home, AboutUs, Faq
# Create your views here.

def home(request):
    data = Home.objects.all()
    # user = AdminUser.objects.get(email=request.session['login_user'])
    return render(request, 'home1.html', {'data': data})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        terms_confirmed = request.POST.get('terms_confirmed')
        print(username, email, password, terms_confirmed)
        try:
            AdminUser.objects.get(email=email)
            return JsonResponse({"status": "Email is Already Registered"})
        except:
            if (password_check(password)):

                AdminUser.objects.create(username=username, email=email, password=password)
                return JsonResponse({"status": "User Login Success"})

            else:
                return JsonResponse({"status": "Incorrect Password"})




def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        print(val)
        return val


def login(request):

    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password')
        print(email, password)
    try:
        user = AdminUser.objects.get(email=email)

    except:
        return JsonResponse({"status": "Invaild Email"})

    if user.password == password:
        request.session['login_user'] = email
        return JsonResponse({"status": "User Login Success"})

    else:
        return JsonResponse({"status": "Incorrect Password"})


def logout(request):
    try:
        del request.session['login_user']
        return render(request, 'home1.html')
    except:
        return render(request, 'home1.html')





def addoffer(request):
    if request.method == 'POST':
        mlsnumber = request.POST.get('mlsnumber')
        listingprice = request.POST.get('listingprice')
        address = request.POST.get('address')
        streetaddress1 = request.POST.get('streetaddress1')
        streetaddress2 = request.POST.get('streetaddress2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        postalcode = request.POST.get('postalcode')
        print(mlsnumber, listingprice, address, streetaddress1, streetaddress2, city, state, country, postalcode)

        try:
            AddProperty.objects.create(

                mlsnumber=mlsnumber,
                listingprice=listingprice,
                address=address,
                streetaddress1=streetaddress1,
                streetaddress2=streetaddress2,
                city=city,
                state=state,
                country=country,
                postalcode=postalcode,
                createdby=request.session['login_user'],
            )
        except:
            return render(request, 'addoffer.html')





    return render(request, 'addoffer.html')


def viewoffer(request):
    user = AdminUser.objects.get(email=request.session['login_user'])
    offer_obj = AddProperty.objects.filter(createdby=request.session['login_user'])

    return render(request, 'viewoffer.html', {'offer_obj': offer_obj, 'user': user})


def myprofile(request):
    if request.method == 'POST':
        username1 = request.POST.get('username1')
        email12 = request.POST.get('useremail')
        title1 = request.POST.get('title1')
        phone1 = request.POST.get('phone1')
        address1 = request.POST.get('address1')
        city1 = request.POST.get('city1')
        state1 = request.POST.get('state1')
        zip1 = request.POST.get('zip1')
        print(username1, email12, title1, phone1, address1, city1, state1, zip1)
        user = AdminUser.objects.get(email=email12)
        user.email = email12
        user.username = username1
        user.title = title1
        user.phone = phone1
        user.Address = address1
        user.city = city1
        user.state = state1
        user.zip = zip1
        if 'myfile' in request.FILES:
            user.image = request.FILES['myfile']
            user.save()
        else:
            user.save()


    user = AdminUser.objects.get(email=request.session['login_user'])
    return render(request, 'myprofile.html', {'user': user})



def pagecontent(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        address = request.POST.get('address')
        content = request.POST.get('content')
        myfile = request.FILES['myfile']
        print(title, address, content)
        PageContent1.objects.create(title=title, address=address, content=content, image=myfile)
    return render(request, 'pagecontent.html')


def pagecontent1(request):
    data = PageContent1.objects.all()

    return render(request, 'pagecontent1.html', {'data': data})


def aboutus(request):
    data = AboutUs.objects.all()

    return render(request, 'aboutus.html', {'data': data})


def faq(request):
    data = Faq.objects.all()

    return render(request, 'faq.html', {'data': data})


def header(request):
    user = AdminUser.objects.get(email=request.session['login_user'])
    return render(request, 'header.html', {'user': user})


def base(request):
    user = AdminUser.objects.get(email=request.session['login_user'])
    return render(request, 'base1.html', {'user': user})


