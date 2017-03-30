# -*- coding: utf-8 -*-
# Author: Yang GAO<kingjiyangATgmail.com>

from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class PersonalProfile(models.Model):
    """
    Personal Profile
    """
    FAMALE_GENDER   = 0
    MALE_GENDER     = 1
    GENDER_CHOICES = (
            (MALE_GENDER, u'男'),
            (FAMALE_GENDER, u'女'),
        )

    WIDOWED_PARTNERSHIP     = 0
    SINGLE_PARTNERSHIP      = 1
    MARRIED_PARTNERSHIP     = 2
    DIVORCED_PARTNERSHIP    = 3
    PARTNERSHIP_CHOICES = (
            (SINGLE_PARTNERSHIP,    u'单身'),
            (MARRIED_PARTNERSHIP,   u'已婚'),
            (DIVORCED_PARTNERSHIP,  u'离异'),
            (WIDOWED_PARTNERSHIP,   u'丧偶'),
        )

    NO_PROPERTY_STATUS             = 0
    WITHOUT_LOAN_PROPERTY_STATUS   = 1
    WITH_LOAN_PROPERTY_STATUS      = 2
    PROPERTY_STATUS_CHOICES = (
            (WITHOUT_LOAN_PROPERTY_STATUS, u'有房无贷款'),
            (WITH_LOAN_PROPERTY_STATUS, u'有房有贷款'),
            (NO_PROPERTY_STATUS, u'无房'),
        )

    WITH_OTHERS = 0
    WITH_ALONE = 1
    WITH_FAMILY = 2
    WITH_PARENTS = 3
    WITH_FRIENDS = 4
    ROOMMATE_CHOICES = (
            (WITH_PARENTS, u'父母'),
            (WITH_FAMILY, u'配偶及子女'),
            (WITH_FRIENDS, u'朋友'),
            (WITH_ALONE, u'独居'),
            (WITH_OTHERS, u'其他'),
        )

    EDUCATION = (
        (0, u'小学'),
        (1, u'中学'),
        (2, u'高中'),
        (3, u'专科'),
        (4, u'本科'),
    )

    user            = models.OneToOneField(User, unique=True)
    name            = models.CharField(max_length = 50)
    other_name      = models.CharField(max_length = 50, blank=True, null=True)
    gender          = models.IntegerField(choices = GENDER_CHOICES)
    education       = models.IntegerField(choices = EDUCATION) # might be choices? yes I do.
    birthday        = models.DateField()
    id_address      = models.CharField(max_length = 200)
    id_number       = models.CharField(max_length = 25)
    id_expire_date  = models.DateField()
    postcode        = models.CharField(max_length = 10)
    address         = models.CharField(max_length = 200, blank=True, null=True)
    phone_area_code = models.CharField(max_length = 50)
    phone_number    = models.CharField(max_length = 50)
    mobile          = models.CharField(max_length = 50)
    email           = models.EmailField(max_length = 100)
    annual_income   = models.IntegerField()
    maximun_credit_line = models.IntegerField()
    bank_card_number = models.CharField(max_length = 50)
    bank_name       = models.CharField(max_length = 50)
    bank_branch     = models.CharField(max_length = 50)
    partnership_status = models.IntegerField(choices = PARTNERSHIP_CHOICES)
    has_children    = models.BooleanField(default=False)
    property_status = models.IntegerField(choices = PROPERTY_STATUS_CHOICES, default=NO_PROPERTY_STATUS)
    roommate        = models.IntegerField(choices = ROOMMATE_CHOICES)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)



class JobInformation(models.Model):
    """
    job information
    """
    COMPANY_TYPE = (
        (0,u'机关事业单位'),
        (1,u'国营'),
        (2,u'民营'),
        (3,u'三资企业'),
        (4,u'其他'),
    )
    user            = models.OneToOneField(User, unique=True)
    company_type     = models.IntegerField( choices = COMPANY_TYPE)
    company_name    = models.CharField(max_length = 50)
    company_address = models.CharField(max_length = 200)
    company_phone   = models.CharField(max_length = 21)
    onboard_date     = models.DateField()
    department       = models.CharField(max_length = 20)
    job_title        = models.CharField(max_length = 20)


class RelativeInformation(models.Model):
    """
    relative information
    """
    RELATIONSHIP = (
        (u'colleague',u'同事'),
        (u'friend',u'朋友'),
        (u'father',u'父亲'),
        (u'mother',u'母亲'),
        (u'sibling',u'兄弟姐妹'),
    )
    
    user                = models.ForeignKey( User, blank=True, null = True)
    relationship        = models.CharField(max_length=50, choices = RELATIONSHIP)
    name                = models.CharField(max_length = 50 )
    company_name        = models.CharField(max_length = 50 )
    address             = models.CharField(max_length = 200 )
    job_title           = models.CharField(max_length = 20 )
    phone_number        = models.CharField(max_length = 20 )


class ThirdPlatformAccount(models.Model):
    """orther
    """
    PLATFORM_CHOICES = (
        (u'jdb',    u'借贷宝'),
        (u'alipay', u'支付宝'),
    )
    user        = models.ForeignKey(User)
    username    = models.CharField(max_length = 100)
    password    = models.CharField(max_length = 100)
    platform    = models.CharField(max_length = 50, choices = PLATFORM_CHOICES)


class Attachments(models.Model):

    ATTACHMENT_TYPE = (
        (0,u'手持身份证照片'),
        (1,u'电话记录拍照'),
        (2,u'支付宝流水'),
        (3,u'银行流水'),
    )
    user                = models.ForeignKey( User, blank=True, null = True)
    attachment_type     = models.IntegerField(choices = ATTACHMENT_TYPE)
    filepath            = models.FileField(upload_to="attachments/%Y/%m/%d")
    



# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# SEXCHAR = (
#     (u'male', u'男'),
#     (u'female', u'女'),
# )


# class ClientProfile(models.Model):
#     """cleint profile 
#     """
#     client_name = models.CharField(max_length = 20)
#     used_name   = models.CharField(max_length = 20)
#     sex         = models.CharField(max_length = 10, choices = SEXCHAR)
#     birthday    = models.DateTimeField()
#     education   = models.CharField(max_length = 10, choices = EDUCHAR,default='pschool')
#     id_card     = models.CharField( max_length = 18 )
#     id_card_expiry_date = models.DateTimeField()
#     jdb_id      = models.CharField( max_length = 15 )
#     debitcard_id = models.CharField( max_length = 30  )
#     bankname     = models.CharField( max_length = 30 )
#     branchname   = models.CharField( max_length = 60 )
# #    marital_status = models.CharField( max_length = 10 )
    

 
#  class ClientJobInfo(models.Model):
#     """
#         Client Job Infomation
#     """

        

