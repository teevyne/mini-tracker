from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from tracker.models import Cylinder
from tracker.serializer import CylinderSerializer


class CylinderCreateView(generics.ListCreateAPIView):
    queryset = Cylinder.objects.all()
    serializer_class = CylinderSerializer


class CylinderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cylinder.objects.all()
    serializer_class = CylinderSerializer


@api_view(['GET', 'PATCH'])
def change_location_from_retailer_to_dispatch(self, cylinder_name):
    obj = get_object_or_404(Cylinder, cylinder_number=cylinder_name)
    obj.issue_cylinder_for_delivery()
    obj.save()
    return Response("Changed state to dispatch")


@api_view(['GET', 'PATCH'])
def change_location_from_dispatch_to_user(self, cylinder_name):
    obj = get_object_or_404(Cylinder, cylinder_number=cylinder_name)
    obj.issue_cylinder_to_final_user()
    obj.save()
    return Response("Changed state to user")


@api_view(['GET', 'PATCH'])
def change_location_from_user_to_dispatch(self, cylinder_name):
    obj = get_object_or_404(Cylinder, cylinder_number=cylinder_name)
    obj.return_cylinder_from_final_user()
    obj.save()
    return Response("Changed state to dispatch")


@api_view(['GET', 'PATCH'])
def change_location_from_dispatch_to_retailer(self, cylinder_name):
    obj = get_object_or_404(Cylinder, cylinder_number=cylinder_name)
    obj.return_cylinder_to_retailer_store()
    obj.save()
    return Response("Changed state to retailer")
