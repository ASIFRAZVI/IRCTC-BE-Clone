from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

# scope based trotling  alternativly we can do directly in views
# class ScopBased(UserRateThrottle): # use this class in troting class in views
    # scope= "contact" # then use this scop in setting and define requests


