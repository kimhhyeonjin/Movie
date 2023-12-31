# 8기 FINAL 관통 PJT

## 팀원 정보 및 업무 분담 내역

- 팀장: 이아현, 팀원: 김현진

- 업무 분담 내역
  
  - 이아현
    
    - DRF 서버 로직 구현
    
    - back-end
    
    - CSS
  
  - 김현진
    
    - DRF 서버 로직 구현
    
    - Vue 클라이언트 구현
    
    - 알고리즘 작성
    
    - front-end

## 목표 서비스 구현 및 실제 구현 정도

1. 우선 기본 명세서에 명시된 기능들을 충실하게 수행하는 것을 목표로 했다.

2. 초기 목표는 디즈니 사의 영화들만 추출해서 디즈니 영화 덕후들을 위한 영화
   추천 및 커뮤니티 형성을 목표로 했으나, 디즈니 플러스 OTT와의 차별점을 찾지 못해서 방향을 변경하였다.

3. 유저의 프로필 사진을 변경할 수 있는 기능을 추가하고자 했으나 시간 부족으로 하지 못하였다.

4. 기본 기능 구현이라는 목표는 달성하였으나, 다른 추가적인 기능들을 추가하지 못한 것은 아쉬움이 남는다.

## 데이터베이스 모델링(ERD)

![](README_assets/2022-11-28-17-50-48-Image%20Pasted%20at%202022-11-24%2021-50.png)

## 영화 추천 알고리즘에 대한 기술적 설명

### 검색 알고리즘

- 검색한 단어가 영화의 제목이나 내용에 포함되는 경우 해당 영화를 결과로 보여줄 수 있도록 하였다.

### 추천 알고리즘

- 마음에 드는 영화에 좋아요 버튼을 클릭할 수 있도록 하여 사용자가 좋아요 버튼을 누른 영화 장르를 추천할 수 있도록 하였다.

- 만약 좋아요 버튼을 누른 영화가 없는 경우 랜덤으로 추천할 수 있도록 하였다.

## 서비스 대표 기능에 대한 설명

- 영화 리뷰 기능
  
  - 영화 세부항목에서 원하는 리뷰를 작성, 삭제할 수 있다.

- 검색과 추천 알고리즘

- 게시판 기능
  
  - 게시판 기능을 통해 영화와 관련된 게시글을 작성, 수정, 삭제할 수 있도록 하였으며 본인 또는 다른 사람의 게시글에 댓글을 달 수 있도록 하였다.
  
  - 게시글 작성자를 클릭하면 해당 작성자의 프로필로 이동할 수 있도록 하였다.

- 프로필 기능
  
  - 팔로우 기능을 추가하여 마음에 드는 사용자를 팔로우할 수 있도록 하였다.
  
  - 좋아요 버튼을 클릭한 영화를 볼 수 있도록 하였다.
  
  - 이와 같은 기능을 통해 다른 사용자는 어떤 영화를 좋아하는지 알 수 있고 자신의 취향과 비슷한 사용자를 팔로우할 수 있다.

## 기타(느낀 점, 후기 등)

- 이아현
  
  - 명세서없이 처음부터 모든 프로젝트를 구현하는 것이 많이 어려웠다.
  
  - 그래도 페어와 같이 하나하나 해결해나가면서 서비스가 완성되어가는 것을 보며
    뿌듯함을 느꼈고, 프로젝트를 진행하면서 나의 부족한 점이 많이 보여서 이 부분들을 보강하여 2학기 프로젝트에 참여해야겠다는 생각이 들었다.

- 김현진
  
  - 주어진 ERD나 vue tree 없이 처음부터 끝까지 직접 프로젝트를 진행하면서 실력이 매우 향상되었다.
  
  - 원하던 추가적인 기능을 구현하지 못해 아쉽지만 최선을 다해 뿌듯하다.