# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import HTCashbillService, PopbillException

htCashbillService = HTCashbillService(testValue.LinkID, testValue.SecretKey)
htCashbillService.IsTest = testValue.IsTest
htCashbillService.IPRestrictOnOff = testValue.IPRestrictOnOff
htCashbillService.UseStaticIP = testValue.UseStaticIP
htCashbillService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
현금영수증 매입/매출 내역 수집요청에 대한 상태 목록을 확인합니다.
- 수집 요청 후 1시간이 경과한 수집 요청건은 상태정보가 반환되지 않습니다.
- https://developers.popbill.com/reference/htcashbill/python/api/job#ListActiveJob
"""

try:
    print("=" * 15 + " 수집 상태 목록 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    response = htCashbillService.listActiveJob(CorpNum)

    listLength = str(len(response))

    for info in response:
        print("jobID (작업아이디) : %s" % info.jobID)
        print("jobState (수집상태) : %s" % info.jobState)
        print("queryType (수집유형) : %s" % info.queryType)
        print("queryDateType (일자유형) : %s" % info.queryDateType)
        print("queryStDate (시작일자) : %s" % info.queryStDate)
        print("queryEnDate (종료일자) : %s" % info.queryEnDate)
        print("errorCode (오류코드) : %s" % info.errorCode)
        print("errorReason (오류메시지) : %s" % info.errorReason)
        print("jobStartDT (작업 시작일시) : %s" % info.jobStartDT)
        print("jobEndDT (작업 종료일시) : %s" % info.jobEndDT)
        print("collectCount (수집개수) : %s" % info.collectCount)
        print("regDT (수집 요청일시) : %s" % info.regDT + "\n")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
