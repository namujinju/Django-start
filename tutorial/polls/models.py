from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # max_legnth는 필수
    pub_date = models.DateTimeField('date published')
    # 선택적인 첫번째 위치 인수를 전달하여 사람이 읽기 좋은(human-readable) 이름을 지정할 수도 있습니다.

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # 각각의 Choice 가 하나의 Question 에 관계된다
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
