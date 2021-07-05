from django.contrib.auth import decorators
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Blog, UserProfile,ProfileGallery
from django.contrib.auth.decorators import login_required
from .decorators import restrictPages
from .forms import *
from django.contrib.auth.hashers import check_password
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    # blogs = Blog.objects.all().order_by('-blogtime')
    blogs = Blog.date_objects.all()
   
    user = User.objects.all()
    dict= {
        'blog':blogs,
        'users': user,
        
        }
        
    return render(request,'index.html', dict)

def contactus(request):
    
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():
            form.save()
            # messages.info(request,"Thank You for Contacting Us.")
            return redirect('/')
        else:
            # messages.info(request,"Something Went Wrong. Please Try Again.")
            return redirect('/contact-us')
    else:
        form = ContactForm()
        return render(request,'contactus.html',{'form':form})

@login_required(login_url='/login')
def search(request):

    query = request.GET['search_user']

    filterUser = User.objects.filter(username__icontains=query)


    posting = {'filterUser':filterUser,
                'query':query
                }

    return render(request,'search.html',posting)




# ModelForm Register View
@restrictPages
def register(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.info(request,'Registration Complete. Please Log in.')
            return redirect('/login')

    
    return render(request,'register.html',{'userForm':form})


@restrictPages
def logins(request):
    if request.method == 'POST':
        usernames = request.POST['login_username']
        passwords = request.POST['login_password']


        user = authenticate(username=usernames.lower(), password=passwords)
        print(user)
        if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'Successfully Log in.')
            return redirect('/')
        else:
            messages.add_message(request, messages.WARNING, 'Sorry, Invalid Credentials. Please Log in Again.')
            return redirect('/login')
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"Logout Successfully.")
    return redirect('/')

@login_required(login_url='/login')
def updateProfile(request):
    users = request.user
    form = UserUpdateForm(instance = request.user)
    profileform = ProfileForm(instance = request.user.userprofile)
    
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance = request.user)
        profileform = ProfileForm(request.POST,instance=request.user.userprofile)
        if form.is_valid() and profileform.is_valid():
            form.save()
            profileform.save()
            return redirect('/profile')
        
       
    dict={
        'user':users,
        'form':form,
        'profileForm':profileform
    }

    return render(request, 'updateProfile.html',dict)

@login_required(login_url='/login')
def blog(request):

    author_name = request.user.first_name + " " + request.user.last_name
    if request.method == 'POST':
       form = BlogForm(request.POST)
       form.instance.blog_user = request.user
       form.instance.blog_author = author_name
       if form.is_valid():
           form.save()
           return redirect('/blog')


    form = BlogForm()

    user = request.user
    userblog = user.blog_set.all().order_by('-blogtime')
    dict= {
        'blog':userblog,
        'form':form
    }
    return render(request,'blog.html',dict)

@login_required(login_url='/login')
def addblog(request):
    author_name = request.user.first_name + " " + request.user.last_name
    if request.method == 'POST':
       form = BlogForm(request.POST)
       form.instance.blog_user = request.user
       form.instance.blog_author = author_name
       if form.is_valid():
           form.save()
           return redirect('/blog')
    
    else:
        form = BlogForm()
        context = {'form':form}
        return render(request,'addblog.html',context)

@login_required(login_url='/login')
def deleteblog(request,id):
    try:
        user = request.user
        print("request.user",user)
        blogInfo = Blog.objects.get(id=id)
        userInformation = blogInfo.blog_user
        print("user",userInformation)

        if user == userInformation:
            blogInfo.delete()
            messages.info(request,"Blog has been deleted Successfully.")
            return redirect("/blog/")
        else:
            messages.info(request,"Sorry, Error Occured. You don't have access.")
            return redirect('/')
    except:
        messages.info(request," Sorry Error Occured.")
        return redirect("/blog/")


@login_required(login_url='/login')
def updateblog(request,id):
    try:
        user = request.user.id

        bloginfo = Blog.objects.get(id=id)
        userInformation = bloginfo.blog_user.id
        if user == userInformation:
            dict ={
                'blog':bloginfo
            }
            if request.method =='POST':
                posting = request.POST
                post = posting['blogpost']
                title = posting['title']

                bloginfo.blogpost = post
                bloginfo.blogtitle = title
                bloginfo.save()
                messages.info(request,"Your blog has been updated.")
                return redirect("/blog/")
            else:
                return render(request, "updateblog.html",dict)
        else:
            messages.info(request,"Sorry, You don't have access.")
            return redirect("/")
    except:
        return redirect("/")
    
    

@login_required(login_url='/login')
def profile(request):
    user = request.user
    blog = user.blog_set.all()    
    content = {
        'blog':blog
    }
    return render(request, 'profile.html', content)

@login_required(login_url='/login')
def uploadImages(request):
    user = request.user
    try:
        if request.method =="POST":
            imagefile = request.FILES['uploadImage']
            user.userprofile.userImage = imagefile
            user.userprofile.save()
            messages.info(request,"Profile has been updated successfully.")
            return redirect('/profile')

    except:
        return redirect('/')

@login_required(login_url='/login')
def uploadGallery(request):
    user = request.user
   
    if request.method =="POST":
        imagefile = request.FILES['galleryImage']
        c = user.profilegallery_set.create(userGallery=imagefile,userInfo=user)
        c.save()
        messages.info(request,"Image is added to Gallery.")
        return redirect('/profile/gallery')


@login_required(login_url='/login')
def delete_user(request):
    user  = request.user
    #  Checking password for deleting account
    if request.method == "POST":
        checkPassword = request.POST['check_password']
        check_Password = user.check_password(checkPassword)
       
        if checkPassword == '':
            messages.info(request,"Please Enter Password to Continue.")
            return redirect('/settings')

        if check_Password == True:
            user.delete()
            messages.info(request," User has been deleted. Thank you for Joining Us.")
            return redirect('/')
        else:
            messages.info(request," Invalid Password.")
            return redirect('/settings')



def view_profile(request,username):
    user = User.objects.get(username=username)
    imageGallery = user.profilegallery_set.all()
    return render(request,'view_profile.html',{'user':user,'gallery':imageGallery})

def profile_gallery(request):
    user = request.user
    gallery = user.profilegallery_set.all()
    profileGallery = user.userprofile.userImage

    content = {
        'gallery':gallery,
        'profile':profileGallery
    }
    return render(request,'profile_html/profile_gallery.html',content)

def profile_settings(request):
    return render(request,'profile_html/profile_settings.html')