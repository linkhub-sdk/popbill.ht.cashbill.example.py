# -*- coding: utf-8 -*-

'''
 팝빌 홈택스 현금영수증 연계 API Python SDK Example

 - Python SDK 연동환경 설정방법 안내 : https://docs.popbill.com/htcashbill/tutorial/python
 - 업데이트 일자 : 2020-07-16
 - 연동 기술지원 연락처 : 1600-9854 / 070-4304-2991
 - 연동 기술지원 이메일 : code@linkhub.co.kr

 <테스트 연동개발 준비사항>
 1) 23, 26번 라인에 선언된 링크아이디(LinkID)와 비밀키(SecretKey)를
    링크허브 가입시 메일로 발급받은 인증정보를 참조하여 변경합니다.
 2) 팝빌 개발용 사이트(test.popbill.com)에 연동회원으로 가입합니다.
 3) 홈택스 연동서비스를 이용하기 위해 팝빌에 인증정보를 등록 합니다. (인증방법은 부서사용자 인증 / 공인인증서 인증 방식이 있습니다.)
    - 팝빌로그인 > [홈택스연동] > [환경설정] > [인증 관리] 메뉴에서 [홈택스 부서사용자 등록] 혹은
      [홈택스 공인인증서 등록]을 통해 인증정보를 등록 합니다.
    - 홈택스연동 인증 관리 팝업 URL(GetCertificatePopUpURL API) 반환된 URL에 접속 하여
      [홈택스 부서사용자 등록] 혹은 [홈택스 공인인증서 등록]을 통해 인증정보를 등록 합니다.
'''

# 링크아이디
LinkID = 'TESTER'

# 비밀키
SecretKey = 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I='

# 연동환경 설정값, 개발용(True), 상업용(False)
IsTest = True

# 팝빌회원 사업자번호
testCorpNum = "1234567890"

# 팝빌회원 아아디
testUserID = "testkorea"

# 발급토큰 IP 제한기능 활성화 여부 (권장-True)
IPRestrictOnOff = True

# 팝빌 API 서비스 고정 IP 사용여부(GA), true-사용, false-미사용, 기본값(false)
UseStaticIP = False
