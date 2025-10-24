from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField("Заголовок страницы", max_length=200)
    slug = models.SlugField("URL", unique=True)
    content = models.TextField("Содержимое страницы")
    image = models.ImageField("Изображение", upload_to="pages/", blank=True, null=True)

    created_at = models.DateTimeField("Дата создания", default=timezone.now)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "О редакции"
        verbose_name_plural = "О редакции"

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name} - {self.subject}"


class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=100, verbose_name="Должность")
    photo = models.ImageField(upload_to='team_photos/', verbose_name="Фото")
    bio = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class VirtualTour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название тура")
    video = models.FileField(upload_to='virtual_tours/', verbose_name="Видео")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    image = models.ImageField(upload_to='gallery/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Картинка")
    content = models.TextField(verbose_name="Текст новости")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="Ссылка (slug)")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name="Новость")
    name = models.CharField(max_length=100, verbose_name="Имя")
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return f"Комментарий от {self.name}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_at']