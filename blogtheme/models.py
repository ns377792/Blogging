from django.db import models
from django.db.models.base import Model

# Create your models here.

class Navlog(models.Model):
    NAV_CHOICES = (
        ("logo", "logo"),
    )
    logo = models.CharField(max_length=20, choices=NAV_CHOICES,unique=True)
    name = models.CharField(max_length=20)
    name2 = models.CharField(max_length=20)
    
class Nav_menu(models.Model):
    MENU_CHOICES = (
        ("menu1", "menu1"),
        ("menu2", "menu2"),
        ("menu3", "menu3"),
        ("menu4", "menu4"),
        ("menu5", "menu5"),
        ("menu6", "menu6"),
    )
    your_menu = models.CharField(max_length=20,default="icon1", choices=MENU_CHOICES,unique=True)
    menuname = models.CharField(max_length=15)
    menuurl = models.CharField(max_length=40)

class Nav_social_media_icon(models.Model):
    ICON_CHOICES = (
        ("icon1", "icon1"),
        ("icon2", "icon2"),
    )
    your_icon = models.CharField(max_length=20,default="icon1", choices=ICON_CHOICES,unique=True)
    icon = models.CharField(max_length=30)
    iconlink = models.CharField(max_length=60)

class FooterHeading(models.Model):
    FOOTER_CHOICES = (
        ("first", "first"),
        ("second", "second"),
        ("third", "third"),
        ("fourth", "fourth"),
    )
    sno = models.CharField(max_length=25,choices=FOOTER_CHOICES, unique=True)
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.sno+" - "+self.name
    

class FooterLink(models.Model):
    head = models.ForeignKey(FooterHeading, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    link = models.CharField(max_length=200)

class copyrightClaim(models.Model):
    COPYRIGHT_CHOICES = (
        ("footer", "footer"),
    )
    location = models.CharField(max_length=25, choices=COPYRIGHT_CHOICES, unique=True)
    msg = models.CharField(max_length=155)