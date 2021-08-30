from django.urls import path

from tracker.views import CylinderCreateView, change_location_from_retailer_to_dispatch, CylinderDetailView, \
    change_location_from_dispatch_to_user, change_location_from_user_to_dispatch, \
    change_location_from_dispatch_to_retailer

urlpatterns = [
    path("cylinder/", CylinderCreateView.as_view()),
    path("cylinder/<int:pk>/", CylinderDetailView.as_view()),

    path("retailer_to_dispatch/<str:cylinder_name>/", change_location_from_retailer_to_dispatch),
    path("dispatch_to_user/<str:cylinder_name>/", change_location_from_dispatch_to_user),
    path("user_to_dispatch/<str:cylinder_name>/", change_location_from_user_to_dispatch),
    path("dispatch_to_retailer/<str:cylinder_name>/", change_location_from_dispatch_to_retailer),
]
