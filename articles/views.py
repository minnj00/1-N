from django.shortcuts import render, redirect
from .models import Article, Comment 
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context ={
        'articles': articles,
    }
    
    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    comment_form = CommentForm()

    # comment 목록 조회 
    # 1. 첫번째 방법
    # comment_list = Comment.objects.filter(article=article)

    # 2. 두번째 방법 (Comment에 article이 연결되있기 때문에 그 반대도 연결되어 있음)
    # 현재 article이라는 변수에는 현재 특정 id에 해당하는 article 정보가 저장되어 있음.
    # comment_list = article.comment_set.all()

    # 3. 세번쨰 방법
    # html 코드에서 article.comment_set.all 로 직접 변수 입력
    # -> 이 방법이 data 관개설정을 잘 이용하는 방법 


    # context 딕셔너리 안의 key와 html 안의 변수의 이름이 같아야 함.
    context = {
        'article': article,
        'comment_form': comment_form,
        # 'comment_list': comment_list,
    }

    return render(request, 'detail.html', context)



# 코드를 짤 때 코드가 진행되는 순서대로 작성하면서 진행 반복
# -> 오류가 났을 때 순서대로 수정해볼 수 있음.
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'form.html' , context)
    # modelform 어제 코드 보면 update, create html 파일이 완전히 똑같았음
    # 둘다 submit 후에 action칸을 비워놨기 때문에

def comment_create(request, article_id):
    # 사용자가 입력한 정보를 form에 입력 
    comment_form = CommentForm(request.POST)
        
    # 유효성 검사
    if comment_form.is_valid():
        # form 을 저장 => 추가로 넣어야 하는 데이터를 넣기 위해 저장 멈춰!
        comment=comment_form.save(commit=False)

        # 질문: 
        
        # 첫번째 방법.
        # article_id를 기준으로 article obj(article 전체정보들) 를 가져와서 
        # Comment의 article 컬럼(정보가 없음)에 저장
        article = Article.objects.get(id=article_id)
        # # article 컬럼에 추가
        comment.article = article

        # 두번째 방법 : 속도가 좀 더 빠름.
        # comment.article_id = article_id # -> 이렇게 하더라도 article_id에 저장된 값에 따라 장고 컬럼 article에 article_id에 해당하는 정보를 넣어줌
        # 저장
        comment.save()
        return redirect('articles:detail', id=article_id)
def comment_delete(request, article_id, id):
    comment=Comment.objects.get(id=id)

    comment.delete()

    return redirect('articles:detail', id=article_id)