from django.urls import path, include
from rest_framework import routers
from task import views

#versionado de la api 'api/v1'

router = routers.DefaultRouter()

router.register(r'tasks',views.TaskView, 'task')

urlpatterns = [
    path('api/v1/', include(router.urls))

]