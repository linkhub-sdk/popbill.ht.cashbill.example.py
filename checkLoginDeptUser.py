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
팝빌에 등록된 현금영수증 부서사용자 계정정보를 이용하여 홈택스 로그인을 테스트합니다.
- https://docs.popbill.com/htcashbill/python/api#CheckLoginDeptUser
'''

try:
    print("=" * 15 + " 부서사용자 로그인 테스트 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    result = htCashbillService.checkLoginDeptUser(CorpNum)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
