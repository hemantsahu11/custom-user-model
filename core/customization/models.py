from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


# class TeacherManagerActive(models.Manager):
#
#     def get_queryset(self):
#         return super(TeacherManagerActive, self).get_queryset().filter(is_active=True)    # by this condition we will show only active users to console
#
#
# class TeacherManagerInactive(models.Manager):
#
#     def get_queryset(self):
#         return super(TeacherManagerInactive, self).get_queryset().filter(is_active=False)
#
#
# class Teacher(User):
#     active = TeacherManagerActive()    # now instead of Teacher.objects.all()  we will use Teacher.active.all() then it will show active user
#     inactive = TeacherManagerInactive()   # by calling Teacher.inactive.all() we can get the inactive users
#
#     class Meta:
#         proxy = True
#
#     @classmethod              # Manager works on whole table while method works on individual objects
#     def count_all(cls,):
#         return cls.objects.filter(is_active=True).count()   # returns the count of active users
#
#     def check_active(self):
#         if self.is_active:
#             return "User active"
#         else:
#             return "User is not active"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    #maintaining one to one relationship between User Model and UserProfile
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)     # this is just to notify django that whenever superuser or any user is created just link them to userprofile also
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)   # by using this user instance will be saved to UserProfile table also