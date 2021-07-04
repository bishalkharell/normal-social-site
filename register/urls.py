from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name="homePage"),
    path('contact-us/', views.contactus,name="contactus"),
    path('register/', views.register,name="registerPage"),
    path('login/', views.logins,name="loginPage"),
    path('logout/', views.logout_view,name="logout"),
    path('profile/', views.profile,name="profile"),
    path('update_profile/', views.updateProfile, name="update_profile"),
    path('blog/', views.blog,name="blog"),
    path('addblog/', views.addblog, name="addblog"),
    path('delete_blog/<int:id>', views.deleteblog, name="deleteblog"),
    path('update_blog/<int:id>', views.updateblog, name="updateblog"),
    path('search/',views.search,name="search"),
    path('photo_upload/',views.uploadImages,name="uploadimage"),
    path('gallery_upload/',views.uploadGallery,name="uploadGallery"),
    path('view_profile/<str:username>',views.view_profile,name="view_profile"),
    path('profile/gallery/',views.profile_gallery,name="profile_gallery"),
    path('settings/',views.profile_settings,name="profile_settings"),


    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
