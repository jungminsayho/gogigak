# 📌 고기각


## 프로젝트 소개

- 정육각 사이트 클론 프로젝트
- 약 2주 간의 짧은 프로젝트 기간으로 인해 필수 기능과 빠른 시일 내에 구현 가능한 기능에 초점을 맞췄습니다. 
- 개발은 초기 세팅부터 전부 직접 구현했으며, 아래 데모 영상에서 보이는 부분은 모두 프론트엔드와 백엔드가 연결하여 실제 사용할 수 있는 서비스 수준으로 개발한 것입니다.

### 개발 인원 및 기간

- 개발기간 : 2021/7/05 ~ 2021/7/16
- 개발 인원 총 6명
   -  프론트엔드 : 박관용, 이재현, 장운서
   -  백엔드 : 서정민, 이준영, 최현정

### 데모 영상

<a href="https://www.youtube.com/watch?v=rDNmt8StgnA">데모영상 클릭</a>

<br>

## 적용 기술 및 구현 기능

### 적용 기술

> - Back-End : Python, Django, MySQL, Bcrypt, pyJWT
> - Common : AWS(EC2,RDS), RESTful API


### 협업 도구
Slack / Git + GitHub / Trello, Notion를 이용해 일정관리, 현황을 관리하였습니다. 


### Backend 구현 기능

#### <서정민>
- 제품 상세페이지 엔드포인트 구현
- 제품 리스트 필터링 기능
    - 카테고리 별
    - 판매순/리뷰순/가격순
- 제품에 대한 Review 작성/읽기/삭제 기능
- 비로그인/로그인 상태 별 Review 읽기 기능
    - 2개의 로그인 decorator를 이용
    - 로그인 상태의 경우, 본인 Review에 한하여 삭제버튼 구현

#### <이준영>
- 장바구니, 구매 페이지 엔드포인트 구현
- 장바구니 기능 구현
   - 제품 추가/삭제 기능
   - 제품 수량 변경 기능
- 제품의 재고, 판매량 관리
- 장바구니를 통한 제품 구매 기능
   - 쿠폰 사용 기능
   - 트랜잭션 구현

#### <최현정>
- 회원가입 기능 
   - 패스워드 해쉬
   - 밸리데이션
- 로그인 기능
   - 패스워드 검증, 
   - 토큰 기간 설정 및 발행
- 마이페이지 엔드포인트 구현
   - 주문 내역
   - 쿠폰 정보
- 신선배송 가능여부 확인 기능


<br>


## Reference

- 이 프로젝트는 [정육각](https://www.jeongyookgak.com/index) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
