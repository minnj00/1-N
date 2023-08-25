from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set = 
    # 두 클래스가 양방향을 연결되어 있음.


# 댓글이라는 기능은 어떤 게시물에 종속되어 있음. 따로 댓글 기능만이 존재할 수 없음.
# 댓글 기능은 또 어떤 데이터를 담아야하는지 생각을 해보면 ..
# 먼저 웹상에 데이터가 어떤 형식으로 저장되어 있는지
# 9:25 쯤 캡쳐 참고
# 데이터 베이스에는 글자나 숫자만 취급 -> 여러개의 데이터를 한번에 넣을 수 없음!
# 댓글 테이블 따로 만든다고 한다면 이 댓글 컬럼이 어느 게시물에 종속이 되는지 알 수 없음.
# comment 테이블에 article_id라는 컬럼을 만들어 어떤 게시물에 속해있는지 표현 가능 
class Comment(models.Model):
    # id 도 자동으로 만들어주는 컬럼
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 모델과 모델을 연결해주는 기능을 함. 인자(어떤모델과 연결할지, delete설정) 
    # article_id 는 자동으로 만들어주는 컬럼
# PK(primary key or id): 고유한 값 (주민등록번호)
# FK(foreign key): 다른 테이블에 있는 id -> 지금 여기서는 article_id 에 해당하는 key 
# django 사이트 relationship field에서 자세한 문서 확인 
# 게시물을 삭제할 때 댓글도 같이 삭제할지 or 분석할 때 사용할 수 있는 데이터인데 유지할지
# 이를 위한 설정
# - cascade, set_null, set_default 