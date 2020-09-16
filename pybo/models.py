from django.db import models

# Create your models here.
# ----- edit -----
class Question(models.Model):
    subject = models.CharField(max_length=200) # 질문의 제목
    content = models.TextField() # 질문의 내용
    create_date = models.DateTimeField() # 질문을 작성한 일시

    # ----- edit -----
    def __str__(self):
        return self.subject
    # -

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문 (어떤 질문의 답변인지 알아야하므로 질문 속성이 필요)
    content = models.TextField() # 답변의 내용
    create_date = models.DateTimeField() # 답변을 작성한 일시
# -
