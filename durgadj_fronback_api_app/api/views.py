from rest_framework import viewsets
# from durgadj_fronback_api_proj.durgadj_fronback_api_app.models import Hydjobs
# from durgadj_fronback_api_proj.durgadj_fronback_api_app.api.serializers import HydJobsSerializer

from durgadj_fronback_api_app.models import Hydjobs
from durgadj_fronback_api_app.api.serializers import HydJobsSerializer



class HydJobsCRUDCBV(viewsets.ModelViewSet):
    serializer_class = HydJobsSerializer
    queryset = Hydjobs.objects.all()