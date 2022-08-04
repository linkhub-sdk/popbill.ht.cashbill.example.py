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
수집 상태 확인(GetJobState API) 함수를 통해 상태 정보가 확인된 작업아이디를 활용하여 수집된 현금영수증 매입/매출 내역의 요약 정보를 조회합니다.
- 요약 정보 : 현금영수증 수집 건수, 공급가액 합계, 세액 합계, 봉사료 합계, 합계 금액
- https://docs.popbill.com/htcashbill/python/api#Summary
'''

try:
    print("=" * 15 + " 수집결과 요약정보 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 수집요청(requestJob)시 발급받은 작업아이디
    JobID = "022080216000000004"

    # 문서형태 배열 ("N" 와 "C" 중 선택, 다중 선택 가능)
    # └ N = 일반 현금영수증 , C = 취소현금영수증
    # - 미입력 시 전체조회
    TradeType = ["N", "C"]

    # 거래구분 배열 ("P" 와 "C" 중 선택, 다중 선택 가능)
    # └ P = 소득공제용 , C = 지출증빙용
    # - 미입력 시 전체조회
    TradeUsage = ["P", "C"]

    response = htCashbillService.summary(CorpNum, JobID, TradeType, TradeUsage)

    print("count (수집 결과 건수) : %s " % response.count)
    print("supplyCostTotal (공급가액 합계) : %s " % response.supplyCostTotal)
    print("taxTotal (부가세 합계) : %s " % response.taxTotal)
    print("serviceFeeTotal (봉사료 합계) : %s " % response.serviceFeeTotal)
    print("amountTotal (합계 금액) : %s " % response.amountTotal)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
