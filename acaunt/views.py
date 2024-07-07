import re
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import profile , masseges
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST' and 'blogin' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password) ##

        if user:
            auth.login(request,user) ##
            return redirect('home')
        else:
            messages.error(request, "not faund")

    return render(request, 'acaunts/login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')

def singup(request):
    if request.method == 'POST' and 'bsingup' in request.POST:
        user_image = None
        fname = None
        lname = None
        username = None
        email = None
        Password = None

        if 'userImage' in request.FILES:
            user_image = request.FILES['userImage']
        else:
            messages.error(request, 'error in User image ')
        if 'firstName' in request.POST:
            fname = request.POST['firstName']
        else:
            messages.error(request, 'error in first name ')
        if 'lastName' in request.POST:
            lname = request.POST['lastName']
        else:
            messages.error(request, 'error in lastName ')
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            messages.error(request, 'error in username ')
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'error in email ')
        if 'password' in request.POST:
            Password = request.POST['password']
        else:
            messages.error(request, 'error in password ')

        if user_image and fname and lname and username and email and Password:

            if User.objects.filter(username = username).exists(): ##
                messages.error(request, 'user name exists ')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email is exists ')
                else:
                    pattern = r'^[\w\.-]+@[\w\.-]+$'
                    if re.match(pattern,email):
                        user = User.objects.create_user( ##
                            first_name=fname,
                            last_name=lname,
                            email=email,
                            username=username,
                            password=Password)
                        user.save()

                        prfile = profile(
                            user = user,
                            userimage = user_image
                        )
                        prfile.save()

                        fname = ''
                        lname = ''
                        username = ''
                        email = ''
                        Password = ''

                        return redirect('login')

                    else:
                        messages.error(request, 'envaled email')
        else:
            messages.error(request, 'empty input')

        return render(request, 'acaunts/singup.html', {
            'firstName': fname,
            'lastName': lname,
            'email': email,
            'username': username,
        })
    else:
        return render(request, 'acaunts/singup.html')

def edit_user (request):

    if request.user is not None:
        userprofile = profile.objects.get(user=request.user)
        context = {
            'fname': request.user.first_name,
            'lname': request.user.last_name,
            'image': userprofile.userimage,
            'username': request.user.username,
            'emaile': request.user.email,
            'pass': request.user.password,
        }

    userprofile = profile.objects.get(user=request.user)
    if request.method =='POST':
        request.user.first_name = request.POST['firstName']
        request.user.last_name = request.POST['lastName']
        request.user.username = request.POST['username']
        request.user.email = request.POST['email']
        if not request.POST['password'].startswith('pbkdf2_sha256$'):
            request.user.set_password(request.POST['password'])
        request.user.save()
        userprofile.save()
        auth.login(request,request.user)

    return render(request, 'acaunts/profile.html',context)


def view_message(request,user_id):
    messagess = masseges.objects.filter(recipient=user_id).order_by('-timestamp')
    return render(request, 'acaunts/show.html', {'message': messagess})

def make_reader(request,massage_id):
    messagess = masseges.objects.get(id=massage_id)
    messagess.is_read = True
    messagess.save()
    return redirect('home')

def delet_massage(request,delet_id):
    messagess = masseges.objects.get(id=delet_id)
    if messagess:
        messagess.delete()
    return redirect('home')
@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_success')
    else:
        form = MessageForm(user=request.user)
    return render(request, 'acaunt/send_message.html', {'form': form})

def message_success(request):
    return render(request, 'acaunt/message_success.html')