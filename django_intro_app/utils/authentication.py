from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from django_intro_app.models import TrackingDevice


class TrackingDeviceAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    model = TrackingDevice

    def authenticate_credentials(self, key):
        try:
            device: TrackingDevice = TrackingDevice.objects.get(api_key=key)
        except TrackingDevice.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid API key.')

        return device, device.api_key
