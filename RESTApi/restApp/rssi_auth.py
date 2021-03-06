from tastypie.authentication import Authentication
from tastypie.authentication import BasicAuthentication
from mongoengine.django.auth import User
from django.http import Http404     

class RssiAuth(Authentication):
    
    def is_authenticated(self, request, **kwargs):
        user_id = request.GET.get('access_key')
        try:
            user = User.objects.get(id=user_id)
            return True
        except Exception,e:
            print e
            raise Http404("User Not Authenticated!")

    