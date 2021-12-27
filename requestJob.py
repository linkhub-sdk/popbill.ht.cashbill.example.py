# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTCashbillService, PopbillException

htCashbillService =  HTCashbillService(testValue.LinkID, testValue.SecretKey)
htCashbillService.IsTest = testValue.IsTest
htCashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff
htCashbillService.UseStaticIP = testValue.UseStaticIP
htCashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
현금영수증 매출/매입 내역 수집을 요청합니다 .(조회기간 단위 : 최대 3개월)
- 수집 요청후 반환받은 작업아이디(JobID)의 유효시간은 1시간 입니다.
- https://docs.popbill.com/htcashbill/python/api#RequestJob
'''

try:
    print("=" * 15 + " 수집 요청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 현금영수증 유형, SELL-매출 현금영수증, BUY-매입 현금영수증
    Type = "SELL"

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20211201"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20211230"

    jobID = htCashbillService.requestJob(CorpNum, Type, SDate, EDate, UserID)

    print( "작업아이디(jobID) : " + jobID)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
