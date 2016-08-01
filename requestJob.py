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
    '''
    수집 요청시 발급받은 작업아이디의 유효시간은 1시간 입니다.
    수집 요청(requestJob) > 작업 상태 확인(getJobState) > 조회(search)
    *** 홈택스 현금영수증 조회 프로세스 ***
    1) 수집 요청
    2) 작업상태 확인(getJobState) API를 호출하여, 결과코드(errorCode)가 1(수집 성공)인지 확인
    3) 해당되는 작업아이디를 사용하여 조회(search) API를 호출
    '''

    print("=" * 15 + " 수집 요청 " + "=" * 15)

    # 현금영수증 유형, SELL-매출 현금영수증, BUY-매입 현금영수증
    Type = "SELL"

    # 시작일자, 표시형식(yyyyMMdd)
    SDate = "20160701"

    # 종료일자, 표시형식(yyyyMMdd)
    EDate = "20160901"

    jobID = htCashbillService.requestJob(testValue.testCorpNum, Type, SDate, EDate, testValue.testUserID)
    
    print( "작업아이디(jobID) : " + jobID)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
