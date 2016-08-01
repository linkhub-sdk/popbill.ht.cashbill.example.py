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
    print("=" * 15 + "수집결과 요약정보 조회 " + "=" * 15)
    '''
        수집 결과에 대한 요약정보를 반환합니다.
        count : 결과건수
        supplyCostTotal : 공급가액 합계
        taxTotal : 세액 합계
        serviceFeeTotal : 봉사료 합계
        amountTotal : 합계 금액
    '''

    # 수집요청(requestJob)시 발급받은 작업아이디
    JobID = "016080114000000008"

    # 문서형태 배열, N-일반 현금영수증, M-취소 현금영수증
    TradeType = ["N", "C"]

    # 거래용도 배열, P-소득공제용, C-지출증빙용
    TradeUsage = ["P", "C"]

    response = htCashbillService.summary(testValue.testCorpNum, JobID, TradeType, TradeUsage, testValue.testUserID)

    print("count (수집결과 건수) : %s " % response.count)
    print("supplyCostTotal (공급가액 합계) : %s " % response.supplyCostTotal)
    print("taxTotal (세액 합계) : %s " % response.taxTotal)
    print("serviceFeeTotal (봉사료 합계) : %s " % response.serviceFeeTotal)
    print("amountTotal (합계 금액) : %s " % response.amountTotal)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
