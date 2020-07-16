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

'''
홈택스 현금영수증 부서사용자 계정을 등록합니다.
- https://docs.popbill.com/htcashbill/python/api#RegistDeptUser
'''

try:
    print("=" * 15 + " 부서사용자 계정등록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 홈택스 부서사용자 계정아이디
    DeptUserID = "deptuserid"

    # 홈택스 부서사용자 계정비밀번호
    DeptUserPWD = "deptuserpwd"

    result = htCashbillService.registDeptUser(CorpNum, DeptUserID, DeptUserPWD)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
