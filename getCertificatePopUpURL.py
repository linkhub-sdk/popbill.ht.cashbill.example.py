# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTCashbillService, PopbillException

htCashbillService = HTCashbillService(testValue.LinkID, testValue.SecretKey)
htCashbillService.IsTest = testValue.IsTest

'''
홈택스 공인인증서 등록 팝업 URL을 반환합니다.
- 반환된 URL은 보안정책에 따라 30초의 유효시간을 갖습니다.
'''

try:
    print("=" * 15 + " 홈택스 공인인증서 등록 팝업 URL " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    url = htCashbillService.getCertificatePopUpURL(CorpNum, UserID)

    print("URL : %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
