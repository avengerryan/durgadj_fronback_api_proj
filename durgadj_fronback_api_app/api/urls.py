
from django.conf.urls import url, include
from rest_framework import routers

# from durgadj_fronback_api_proj.durgadj_fronback_api_app.api.views import HydJobsCRUDCBV
# from durgadj_fronback_api_app.api.views import HydJobsCRUDCBV
from .views import HydJobsCRUDCBV


router = routers.DefaultRouter()
router.register('hydjobsinfo', HydJobsCRUDCBV)


urlpatterns = [
    url(r'', include(router.urls)),

]