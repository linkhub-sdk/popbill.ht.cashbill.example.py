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
검색조건을 사용하여 수집 결과 요약정보를 조회합니다.
- https://docs.popbill.com/htcashbill/python/api#Summary
'''

try:
    print("=" * 15 + " 수집결과 요약정보 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob)시 발급받은 작업아이디
    JobID = "019011915000000001"

    # 문서형태 배열, N-일반 현금영수증, C-취소 현금영수증
    TradeType = ["N", "C"]

    # 거래구분 배열, P-소득공제용, C-지출증빙용
    TradeUsage = ["P", "C"]

    response = htCashbillService.summary(CorpNum, JobID, TradeType, TradeUsage, UserID)

    print("count (수집 결과 건수) : %s " % response.count)
    print("supplyCostTotal (공급가액 합계) : %s " % response.supplyCostTotal)
    print("taxTotal (부가세 합계) : %s " % response.taxTotal)
    print("serviceFeeTotal (봉사료 합계) : %s " % response.serviceFeeTotal)
    print("amountTotal (합계 금액) : %s " % response.amountTotal)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
