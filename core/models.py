from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _  # ✅ Import for translations

class Hospital(models.Model):
    hospital_id = models.UUIDField(_("Hospital ID"), primary_key=True, default=uuid.uuid4, editable=False)
    hospital_name = models.CharField(_("Hospital Name"),default=False, max_length=100)
    latitude = models.FloatField(_("Latitude"), default=0, null=False)
    longitude = models.FloatField(_("Longitude"), default=0, null=False)
    phone_number = models.CharField(_("Phone Number"), max_length=15, blank=False, null=False, unique=True)
    emergency = models.BooleanField(_("Emergency Available"), default=False)
    general_beds = models.IntegerField(_("General Beds"), default=0, null=False)
    icu_beds = models.IntegerField(_("ICU Beds"), default=0, null=False)  
    private_beds = models.IntegerField(_("Private Beds"), default=0, null=False)

    def __str__(self):
        return self.hospital_name