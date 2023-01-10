from django.db import models
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '{}'.format(self.title)


class SubCategory(Category):
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return '{}'.format(self.title)


class Topic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return '{}+{}'.format(self.owner, self.title)


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comment_topic')
    text = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_owner')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return '{}+{}'.format(self.topic.title, self.author.username)


class Like(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='like_topic')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_owner')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return '{}+{}'.format(self.topic.title, self.author.username)
