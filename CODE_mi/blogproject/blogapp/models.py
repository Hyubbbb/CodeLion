from datetime import date
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) # 200자 이하로 제약
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금 시간을 추가하겠다 라는 의미

    def __str__(self):
        return self.title