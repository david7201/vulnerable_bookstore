from django.urls import path
from .views import SignupPageView, view_profile

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    # path('profile/<int:profile_id>/', view_profile, name='view_profile'), 
]

