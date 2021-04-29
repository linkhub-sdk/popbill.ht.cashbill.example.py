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
htCashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
해당 사업자의 파트너 연동회원 가입여부를 확인합니다.
- https://docs.popbill.com/htcashbill/python/api#CheckIsMember
'''

try:
    print("=" * 15 + " 연동회원 가입여부 확인 " + "=" * 15)

    # 조회할 사업자번호, '-' 제외 10자리
    CorpNum = "1234567890"

    result = htCashbillService.checkIsMember(CorpNum)

    print("가입여부 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
