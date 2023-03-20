from django.urls import path, include

from .views import CustomLoginView, signup, CustomLogoutView, profile

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
]
