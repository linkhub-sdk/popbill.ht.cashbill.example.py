# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTCashbillService,PopbillException

htCashbillService =  HTCashbillService(testValue.LinkID,testValue.SecretKey)
htCashbillService.IsTest = testValue.IsTest

try:
    print("=" * 15 + "팝빌 URL 확인" + "=" * 15)

    '''
        사용자가 팝빌 홈페이지에 로그인 하지 않고도 이용할 수 있는 팝빌로그인/포인트충전 페이지의 URL을 반환합니다.
        * 반환되는 URL은 보안 정책에 의해 30초의 유효시간을 갖고 있습니다.
    '''

    # LOGIN : 팝빌 로그인 URL, CHRG : 포인트충전 URL
    TOGO = "LOGIN"

    url = htCashbillService.getPopbillURL(testValue.testCorpNum,testValue.testUserID,TOGO)

    print("URL : %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
