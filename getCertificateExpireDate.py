# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import HTCashbillService, PopbillException

htCashbillService = HTCashbillService(testValue.LinkID, testValue.SecretKey)
htCashbillService.IsTest = testValue.IsTest
htCashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff
htCashbillService.UseStaticIP = testValue.UseStaticIP

'''
등록된 홈택스 공인인증서의 만료일자를 확인합니다.
- https://docs.popbill.com/htcashbill/python/api#GetCertificateExpireDate
'''

try:
    print("=" * 15 + " 홈택스 공인인증서 만료일시 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    expireDate = htCashbillService.getCertificateExpireDate(CorpNum, UserID)

    print("공인인증서 만료일시 : %s" % expireDate)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
