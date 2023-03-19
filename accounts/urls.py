from django.contrib.auth.views import LoginView
from django.urls import path, include

from events.views import event_signup, event_signoff
from .views import CustomLoginView, signup, CustomLogoutView, profile

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('social_django.urls', namespace='social')),
    path('signup/<int:event_id>/', event_signup, name='event_signup'),
    path('signoff/<int:event_id>/', event_signoff, name='event_signoff'),
]
