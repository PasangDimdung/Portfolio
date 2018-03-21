from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomepageView.as_view(), name='base'),
    path('about/',views.AboutView.as_view(), name='about'),
    path('contact/',views.ContactView.as_view(), name='contact'),
    path('photos/', views.PhotoView.as_view(), name='photos'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    ]