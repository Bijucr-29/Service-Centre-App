from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
# from api.views import CustomerViewSetView,WorkCreateView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from api import views
router.register("customers",views.CustomerViewSetView,basename="customers")



urlpatterns=[

        path('token/',ObtainAuthToken.as_view()),
        path('customers/<int:pk>/work/',views.WorkCreateView.as_view()),
        path('work/<int:pk>/',views.WorkDetailView.as_view())


]+router.urls