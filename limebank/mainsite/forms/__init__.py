#! -*- coding: utf-8 -*-
#Author: Yang GAO<kingjiyangATgmail.com>
from django.forms.models import formset_factory, modelformset_factory

from mainsite.models import PersonalProfile
from mainsite.models import JobInformation
from mainsite.models import RelativeInformation
from mainsite.models import ThirdPlatformAccount
from mainsite.models import Attachments
from django.forms import ModelForm

#form_fields = map(lambda field: field.attname, PersonalProfile._meta.get_fields())
exclude_fields = ['id', 'user', 'created_at', 'updated_at']

class PersonalProfileForm(ModelForm):
    class Meta:
        model = PersonalProfile
        exclude = exclude_fields
        labels = {
            'name':             u'姓名',
            'other_name':       u'曾用名',
            'gender':           u'性别',
            'education':        u'学历',
            'birthday':         u'出生日期 格式(年-月-日)',
            'id_address':       u'户籍详细地址',
            'id_number':        u'身份证号码',
            'id_expired_date':  u'身份证有效期',
            'address':          u'现住址',
            'postcode':         u'邮编',
            'phone_area_code':  u'电话区号',
            'phone_number':     u'电话号码',
            'mobile':           u'手机号码',
            'email':            u'电子邮箱',
            'annual_income':    u'个人年收入',
            'maximun_credit_line':  u'信用卡最高额度',
            'bank_card_number': u'银行卡号',
            'bank_name':        u'银行名称',
            'bank_branch':      u'银行分支',
            'partnership_status':   u'婚姻状况',
            'has_children':     u'有子女(若无子女请不要够选)',
            'property_status':  u'房产状况',
            'roommate':         u'共同居住者',
        }

        help_texts = {
            'address': u'若与户籍详细地址一致，请留空',
            'id_address': u'必须与身份证一致',
        }


class JobInformationForm(ModelForm):
    """
    """
    class Meta:
            model = JobInformation
            exclude = ['id', 'user']
            labels = {
                    'company_type':     u'公司类型',
                    'company_name':     u'所在单位名称',
                    'company_address':  u'单位地址',
                    'company_phone':    u'单位电话',
                    'onboard_date':     u'入职时间',
                    'job_title':        u'头衔',
            }


class RelativeInformationForm(ModelForm):
    class Meta:
            model = RelativeInformation
            exclude = ['id', 'user']
            labels = {
                    'relationship'    :   u'关系',
                    'name'            :   u'姓名',
                    'company_name'    :   u'单位名称',
                    'address'         :   u'单位地址',
                    'job_title'       :   u'头衔',
                    'phone_number'    :   u'电话号码',
            }

RelativeInformationFormSet = modelformset_factory(RelativeInformation, 
                                        form=RelativeInformationForm, 
                                        extra=1, max_num=7, min_num=5)

class ThirdPlatformAccountForm(ModelForm):
    """
    """
    class Meta:
            model = ThirdPlatformAccount
            exclude = ['id', 'user']
            labels = {
                    'username':         u'用户名',
                    'password':         u'密码',
                    'platform':         u'平台名称',
            }

class AttachmentsForm(ModelForm):
    """
    """
    class Meta:
            model = Attachments
            exclude = ['id', 'user']
            labels = {    
                    'attachments_type' :   u'附件类型',
                    'filepath'         :   u'上传图片',
            }
