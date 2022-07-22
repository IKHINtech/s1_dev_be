
from django.urls import re_path, include
from s1_developer.app.views.create_reserve_views import CreateReserveViewSet
from s1_developer.app.views.project_views import ProjectViewSet
from s1_developer.app.views.reserve_views import ReserveViewSet
from s1_developer.app.views.sales_views import SalesViewSet
from rest_framework import routers
router = routers.DefaultRouter()

router.register('list_sales', SalesViewSet)
router.register('list_project', ProjectViewSet)
router.register('list_reserved_va', ReserveViewSet)
router.register('reserve_va', CreateReserveViewSet)
urlpatterns = [
    re_path('', include(router.urls))]
