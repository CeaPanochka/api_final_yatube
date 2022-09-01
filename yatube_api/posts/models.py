from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    class Meta:
        verbose_name = 'Группа'

    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Slug', unique=True, max_length=50)
    description = models.TextField('Описание')

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    class Meta:
        verbose_name = 'Пост'

    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор',
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True,
        verbose_name='Изображение',
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True,
        verbose_name='Группа',
    )

    def __str__(self):
        return self.text[:100]


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор',
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Пост',
    )
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    class Meta:
        verbose_name = 'Подписка'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )
