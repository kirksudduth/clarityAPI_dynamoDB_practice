from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from clarityAPIapp.models import EmployeeModel
from clarityAPIapp.views import EmployeeView
from clarityAPIapp.models import PatientModel
from clarityAPIapp.views import PatientView
from clarityAPIapp.views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, 'user')
router.register(r'employees', EmployeeView, 'employee')
router.register(r'patients', PatientView, 'patient')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
