from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site

from .models import User


from .serializers import RegistrationSerializer


tokenValue = {}

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Registration Successful"
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token

            # Send Email Verification Link

            current_site = get_current_site(request)
            htmly = get_template('Users/ActivateAccount.html')

            ans = {
                    'user':user,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                }

            tokenValue[str(ans['uid'])] =  str(ans['token'])

            html_content = htmly.render(ans)

            subject, from_email, to = 'Welcome!', 'jayashsatolia@gmail.com', user.email

            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        else:
            data = serializer.errors
        return Response(data)


def activate(request, uidb64, token):
    print(tokenValue)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and tokenValue[str(uidb64)] == str(token):
        user.is_verified = True
        user.save()
        return HttpResponse('Thanks for Confirmation! You can now login to your Account.')
    else:
        return HttpResponse('Activation link is invalid!')