from rest_framework.serializers import ModelSerializer
# from durgadj_fronback_api_proj.durgadj_fronback_api_app.models import Hydjobs
from durgadj_fronback_api_app.models import Hydjobs


class HydJobsSerializer(ModelSerializer):
    class Meta:
        model = Hydjobs
        fields = '__all__'
