from django import forms
from .models import Article
from .models import Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # fields -> Article 이 가지고 있는 모든 column 들을 입력 받을 거야!
        fields='__all__'

# ModelForm: 해당하는 모델에 어울리는 input태그를 만들어줌
# Meta: 그 외의 정보들을 다 넣어주는 클래스 ArticleForm 클래스에 넣어서 그에 맞는 폼을 만드는 데 도움을 줌.
# 메타정보: 그 사진의 정보들, 사진 찍은 날짜, 장소, 같이 찍은 사람


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        # fields='__all__'
        # content만 보여줄거야 
        # fields = ('content',)
        exclude = ('article',)

        # fields => 추가할 필드 이름 목록
        # exclude => 제외할 필드 이름 목록