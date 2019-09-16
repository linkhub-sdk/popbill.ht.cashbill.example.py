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

'''
검색조건을 사용하여 수집결과를 조회합니다.
- 응답항목에 관한 정보는 "[홈택스연동(현금영수증) API 연동매뉴얼]
  > 3.2.1. Search (수집 결과 조회)" 을 참고하시기 바랍니다.
'''
try:
    print("=" * 15 + " 홈택스 매출/매입 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob)시 발급받은 작업아이디
    JobID = "019012912000000001"

    # 문서형태 배열, N-일반 현금영수증, C-취소 현금영수증
    TradeType = ["N", "C"]

    # 거래구분 배열, P-소득공제용, C-지출증빙용
    TradeUsage = ["P", "C"]

    # 페이지번호
    Page = 1

    # 페이지당 목록개수, 최대값 1000
    PerPage = 10

    # 정렬방향 D-내림차순, A-오름차순
    Order = "D"

    response = htCashbillService.search(CorpNum, JobID, TradeType, TradeUsage,
                                        Page, PerPage, Order, UserID)

    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    for info in response.list:
        print("\n=======현금영수증 정보=======>")
        print("ntsconfirmNum (국세청승인번호) : %s " % info.ntsconfirmNum)
        print("tradeDate (거래일자) : %s " % info.tradeDate)
        print("tradeDT (거래일시) : %s " % info.tradeDT)
        print("tradeUsage (거래유형) : %s " % info.tradeUsage)
        print("tradeType (현금영수증 형태) : %s " % info.tradeType)
        print("supplyCost (공급가액) : %s " % info.supplyCost)
        print("tax (부가세) : %s " % info.tax)
        print("serviceFee (봉사료) : %s " % info.serviceFee)
        print("totalAmount (거래금액) : %s " % info.totalAmount)
        print("invoiceType (매입/매출) : %s " % info.invoiceType)

        print("\n발행자 정보>")
        print("franchiseCorpNum (발행자 사업자번호) : %s " % info.franchiseCorpNum)
        print("franchiseCorpName (발행자 상호) : %s " % info.franchiseCorpName)
        print("franchiseCorpType (발행자 사업자유형) : %s " % info.franchiseCorpType)

        print("\n거래처 정보>")
        print("identityNum (거래처 식별번호) : %s " % info.identityNum)
        print("identityNumType (식별번호유형) : %s " % info.identityNumType)
        print("customerName (고객명) : %s " % info.customerName)
        print("cardOwnerName (카드소유자명) : %s " % info.cardOwnerName)
        print("deductionType (공제유형) : %s " % info.deductionType) + '\n'
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
