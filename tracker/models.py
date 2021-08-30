from django.db import models
from django_fsm import FSMField, transition

LOCATION = (
    ('with-retailer', 'with-retailer'),
    ('with-dispatch', 'with-dispatch'),
    ('with-user', 'with-user')
)


class Cylinder(models.Model):
    cylinder_number = models.CharField(max_length=20)
    assigned_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    assigned_to = FSMField(choices=LOCATION, default='with-retailer', protected=True)

    def __str__(self):
        return self.cylinder_number

    @transition(field=assigned_to, source='with-retailer', target='with-dispatch')
    def issue_cylinder_for_delivery(self):
        return "Cylinder has been issued for delivery to user"

    @transition(field=assigned_to, source='with-dispatch', target='with-user')
    def issue_cylinder_to_final_user(self):
        return "Cylinder has been delivered to the final user"

    @transition(field=assigned_to, source='with-user', target='with-dispatch')
    def return_cylinder_from_final_user(self):
        return "Cylinder has been retrieved from final user for return"

    @transition(field=assigned_to, source='with-dispatch', target='with-retailer')
    def return_cylinder_to_retailer_store(self):
        return "Cylinder has been returned to the retailer"
