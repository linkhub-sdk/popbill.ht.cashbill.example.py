# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTCashbillService, PopbillException

htCashbillService =  HTCashbillService(testValue.LinkID,testValue.SecretKey)
htCashbillService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 과금정보 확인 " + "=" * 15)
    '''
        정액제를 이용하는 경우 unitCost(단가) 항목은 월정액 요금을 반환합니다.
        정량제의 경우 unitCost(단가) 항목은 서비스 이용건당 이용단가를 반환합니다.
    '''
    
    response = htCashbillService.getChargeInfo(testValue.testCorpNum, testValue.testUserID)

    print(" unitCost (단가) : %s" % response.unitCost)
    print(" chargeMethod (과금유형) : %s" % response.chargeMethod)
    print(" rateSystem (과금제도) : %s" % response.rateSystem)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
