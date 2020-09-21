"""
django에서 모델을 수정한 다음에는, 반드시 makemigration 과 migrate 를 실행시켜주어야 한다.
"""


from django.db import models
# ----- edit
from django.contrib.auth.models import User
# -

# Create your models here.
# ----- edit -----
class Question(models.Model):
    subject = models.CharField(max_length=200) # 질문의 제목
    content = models.TextField() # 질문의 내용
    create_date = models.DateTimeField() # 질문을 작성한 일시
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # null 값을 허용하는 속성 값을 넣어주는 방법도 존재한다.

    # ----- edit -----
    modify_date = models.DateTimeField(null=True, blank=True)
    # - null=True, 와 blank=True를 사용하면 어떤 조건으로든 값을 비워둘 수 있다는 것을 의미한다.
    voter = models.ManyToManyField(User) # voter 추가

    # ----- edit -----
    def __str__(self):
        return self.subject
    # -

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문 (어떤 질문의 답변인지 알아야하므로 질문 속성이 필요)
    content = models.TextField() # 답변의 내용
    create_date = models.DateTimeField() # 답변을 작성한 일시
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # ----- edit -----
    modify_date = models.DateTimeField(null=True, blank=True)
    # -

# -

# ----- edit -----
class Comment(models.Model):
    """
    속성     설명
    ------------------------
    author	댓글 작성자
    content	댓글 내용
    create_date	댓글 작성일시
    modify_date	댓글 수정일시
    question	댓글의 질문
    answer	댓글의 답변
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
# -