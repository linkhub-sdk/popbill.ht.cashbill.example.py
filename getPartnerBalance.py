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
파트너의 잔여포인트를 확인합니다.
- 과금방식이 연동과금인 경우 연동회원 잔여포인트(GetBalance API)를 이용하시기 바랍니다.
- https://docs.popbill.com/htcashbill/python/api#GetPartnerBalance
'''

try:
    print("=" * 15 + "파트너 잔여포인트 확인" + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    balance = htCashbillService.getPartnerBalance(CorpNum)

    print("파트너 잔여포인트 : %d" % balance)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
