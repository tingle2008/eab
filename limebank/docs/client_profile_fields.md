# Model design
===============
* Please see below that the attributes of models if you concerned about the application table how it works.
* If you got any question, don't be shy, ask Yang ASAP.
* DO NOT change any field name, because I've already started to setup the model, please!

## Profile 
   * user           # FK -> auth.models.User
   * name
   * other_name
   * gender
   * education
   * birthday
   * id_address
   * id_number
   * id_expired_date
   * address        # might be same to id_address
   * postcode
   * phone_area_code
   * phone_number
   * mobile
   * email
   * annual_income
   * maximun_credit_line
   * bank_card_number
   * bank_name
   * bank_branch
   * partnership_status  # Single | married | divorced | widowed
   * has_children
   * property_status  # ( with_loan_property | without_loan_property ) | no_property
   * roommate  # parents | family | friend | alone | others

## Job Information
   * user           # FK -> auth.models.User
   * company_name
   * company_address
   * company_phone
   * onboard_date
   * department
   * job_title
   * company_type  # 机关及事业单位 | 国营 | 民营 | 三资企业 | 其他

## Relative Information
   * user           # FK -> auth.models.User
   * relationship  # colleague | friend | father | mother | sibling
   * name
   * company_name
   * address
   * job_title
   * phone_number
 
## Third Platform Account
   * user           # FK -> auth.models.User
   * username
   * password
   * platform   # jiedaibao | alipay 

## Attachments
   * user           # FK -> auth.models.User
   * attachment_type # id_copy_front | id_copy_back | employee_id_copy | company_registration_copy | phone_transaction | bank_transaction | alipay_transaction | national_bank_certification
   * filepath
   
   
## Lend
   * user   # FK -> auth.models.User
   * debit_name    # 借款人姓名(必填)
   * debit_phone   # 借款人电话(可以为空)
   * interest_rate # 借款利率
   * interest_phone # 利息总额
   * lend_date      # 借出日期
   * repay_date     # 还款日期
   * order_id       # 订单id 