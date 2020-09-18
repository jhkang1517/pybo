# ----- edit -----
from django import forms
from pybo.models import Question, Answer, Comment

"""
장고의 폼은 일반 폼(forms.Form) 과 모델 폼(forms.ModelForm)이 있는데, 모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면
연결된 모델의 데이터를 저장할 수 있게 된다. 모델 폼은 class Meta 라는 내부 (Inner)
"""

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # ----- edit -----
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }
# -

# ----- edit -----
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }
# -

# ----- edit -----
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
# -