from mozilla_django_oidc.auth import OIDCAuthenticationBackend
import unicodedata
from django.conf import settings
oidc_client_id = settings.OIDC_RP_CLIENT_ID

def generate_username(email):
    # Using Python 3 and Django 1.11+, usernames can contain alphanumeric
    # (ascii and unicode), _, @, +, . and - characters. So we normalize
    # it and slice at 150 characters.
    return unicodedata.normalize('NFKC', email)[:150]

class MyOIDCAuthBackend(OIDCAuthenticationBackend):
    # def filter_users_by_claims(self, claims):
    #     email = claims.get('email')
    #     if not email:
    #         return self.UserModel.objects.none()

    #     try:
    #         profile = Profile.objects.get(email=email)
    #         return [profile.user]

    #     except Profile.DoesNotExist:
    #         return self.UserModel.objects.none()
    def create_user(self, claims):
        user = super(MyOIDCAuthBackend, self).create_user(claims)
        is_admin = 'kiosk-admin' in claims.get('resource_access').get(oidc_client_id).get('roles', [])
        is_superuser = 'kiosk-superuser' in claims.get('resource_access').get(oidc_client_id).get('roles', [])
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.is_staff = is_admin
        user.is_superuser = is_superuser
        user.save()

        return user

    def update_user(self, user, claims):
        is_admin = 'kiosk-admin' in claims.get('resource_access').get(oidc_client_id).get('roles', [])
        is_superuser = 'kiosk-superuser' in claims.get('resource_access').get(oidc_client_id).get('roles', [])
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.is_staff = is_admin
        user.is_superuser = is_superuser
        user.save()

        return user
    def verify_claims(self, claims):
        print(claims)
        verified = super(MyOIDCAuthBackend, self).verify_claims(claims)
        is_admin = 'kiosk-admin' in claims.get('resource_access').get(oidc_client_id).get('roles', [])
        return verified and is_admin