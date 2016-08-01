# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CorpInfo, HTCashbillService, PopbillException

htCashbillService =  HTCashbillService(testValue.LinkID,testValue.SecretKey)
htCashbillService.IsTest = testValue.IsTest

corpInfo = CorpInfo (
                ceoname = "대표자성명_0801",
                corpName = "상호_0801",
                addr = "주소_0729",
                bizType = "업태_0729",
                bizClass = "종목_0729"
                )
try:
    print("=" * 15 + " 회사정보 수정 " + "=" * 15)

    result = htCashbillService.updateCorpInfo(testValue.testCorpNum, corpInfo, testValue.testUserID)

    print("처리결과 : [%d] %s" % (result.code,result.message) )
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
