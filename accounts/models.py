from django.db import models
from django.conf import settings
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.utils.encoding import smart_text
from django.utils import timezone
# from .validators import validate_author_email, validate_sahar
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from .utils import code_generator
from PIL import Image


USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$' #We removed @ because we don't want username and email be same thing


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    username = models.CharField(
                        max_length=255,
                        validators=[
                                RegexValidator(
                                    regex = USERNAME_REGEX,
                                    message = 'Username must be Alphanumeric contain any of the following". @ + -" ',
                                    code = 'invalid_usarname'
                                )],
                        unique=True,
                    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    zipcode = models.CharField(max_length=120, default="92660")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin


class ActivationProfile(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key     = models.CharField(max_length=120)
    expired = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.key = code_generator()
        super(ActivationProfile, self).save(*args, **kwargs)

def post_save_activation_receiver(sender, instance, created, *args, **kwargs):
    if created:
        # send email
        print("activation created")
        url = "/activate" + instance.key
        # send email

post_save.connect(post_save_activation_receiver, sender=ActivationProfile)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            

    # def __str__(self):
    #     return str(self.user.username)

    def __unicode__(self):
        return str(self.user.username)

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
            ActivationProfile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
