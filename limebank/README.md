# LimeBank
==========
### Intrduction
   以下为 Yang 和 Ting 第一次电话沟通后的记录，由于整个行业处于婴儿阶段，发展和变化较快，我们也不确定未来这个系统变成什么，所以这个项目需要尽可能的快速迭代。所有功能都需着 **最小化，让用户能够快速感知变化** 的前提下进行。

### What is LimeBank?
   LimeBank 不是一个真的银行，旨在帮助类似 _关行长_ 这样的在借贷宝、支付宝上以 微额贷款 开展业务的人，可以快速实现用户审核、收集用户信息等工作。

   目前不涉及任何有关 钱 的操作流在这里，只是单纯的用户相关信息。

### Current Working On
   1. Regestration \[ DONE \]
   1. Client Profile \[ TODO \]
     * [字段列表](https://gitlab.systemadm.in/LimeBank/django-limebank/tree/master/docs/client_profile_fields.md)

### Develpment planning
   未来预期 能够通过足够多的用户数据，为我们找出有价值的模型。
   * 基本方向：
  	 * 借出方 通过线下审核，将信息记录在系统当中
  	 * 协助 借出方 线下审核机制，将线下相关人员聚集在这个系统上
  	 * 借入方 的信用评级
  	 * 支持 **借出方** 共享或分享 **借入方** 的信用评级

### 当前 线下审核机制
   1. 用户 -> 借钱请求 -> 关行长
   1. 关行长 -> 发送 Word 文档 -> 用户
   1. 用户 -> 完成 -> Word 文档
   1. 关行长 -> 通知 -> 线下相关审核人员
   1. 线下相关审核人员 -> 电话询问  -> Word 文档中提交的相关联系人
   1. 线下相关审核人员 -> 反馈调查结果 -> 关行长
   1. 关行长 -> 决定额度并开始执行放款 -> 用户

   * [Word 文档1: 借贷宝平台借款服务申请表-1.doc](https://gitlab.systemadm.in/LimeBank/django-limebank/blob/master/docs/%E5%80%9F%E8%B4%B7%E5%AE%9D%E5%B9%B3%E5%8F%B0%E5%80%9F%E6%AC%BE%E6%9C%8D%E5%8A%A1%E7%94%B3%E8%AF%B7%E8%A1%A8-1.doc)
   * [Word 文档2: 借贷宝平台借款服务申请表-2.doc](https://gitlab.systemadm.in/LimeBank/django-limebank/blob/master/docs/%E5%80%9F%E8%B4%B7%E5%AE%9D%E5%B9%B3%E5%8F%B0%E5%80%9F%E6%AC%BE%E6%9C%8D%E5%8A%A1%E7%94%B3%E8%AF%B7%E8%A1%A8-2.doc)





#### 补充对于已有客户

放款计划：

	* 放款对象   
	* 放款对象手机号
	* 放款额度
	* 收款日期
	

  


#### 一些系统依赖包

ocr system 
yum install automake.noarch
yum install libtool.x86_64
download :leptonica  
http://www.leptonica.com/download.html

make & make install

git clone https://github.com/tesseract-ocr/tesseract

make & make install

python module:

pytesseract

https://pypi.python.org/pypi/pytesseract/0.1.6


PIL-1.1.7.tar.gz

http://effbot.org/media/downloads/PIL-1.1.7.tar.gz

ICU lib
yum install icu.x86_64 libicu.x86_64 libicu-devel.x86_64

pango lib
yum install pango-devel.x86_64 pango.x86_64
