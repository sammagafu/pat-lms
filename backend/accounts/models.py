from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django_resized import ResizedImageField
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_approved=False,
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now, 
            **extra_fields
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        return user

    
    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    full_name = models.CharField(verbose_name="First name",max_length=254, null=False, blank=True)
    phone = models.CharField(verbose_name="Phone Number",max_length=14, validators=[RegexValidator(r'^(\+\d{1,3})?,?\s?\d{8,13}')],unique=True,help_text="Example +255714112233",null=False,blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_tuitor = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    mctnumber = models.CharField(_("MCT Number"), max_length=50,blank=True,null=True)
    avatar = ResizedImageField(upload_to = 'profile/images/%Y/%m/%d',verbose_name=_("Profile Image"),size=[300, 300], crop=['middle', 'center'],default='default.jpg')
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    
    # def get_user_fullname(self):
    #   return "{} {}".format(self.first_name,self.last_name)

    def get_user_is_approved(self):
      return self.is_approved

    def __str__(self):
        return self.email

    def get_avatar(self):
        if self.avatar:
            return 'http://api.pediatrics.or.tz' + self.avatar.url
        return ''

    def save(self,*args, **kwargs):
        if self.typeofmember == "Ordinary Member":
            self.memberId = "pat-od-"+ self.id
        else:
            self.memberId = "pat-as-"+ str(random.randint(0,1000))
        super(User,self).save()