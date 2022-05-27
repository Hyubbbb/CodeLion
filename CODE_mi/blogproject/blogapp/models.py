from datetime import date
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) # 200자 이하로 제약
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금 시간을 추가하겠다 라는 의미

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=200) 
    date = models.DateTimeField(auto_now_add=True) # 자동으로 지금 시간을 추가하겠다 라는 의미
    # 여기까지만 작성하면, 어느 게시글에 해당하는 댓글인지 몰라
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
