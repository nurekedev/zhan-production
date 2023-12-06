from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class ContactThrottling(AnonRateThrottle):
    scope = 'contact_form'
