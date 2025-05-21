from django.db import models
from django.urls import reverse

class my_site(models.Model):

    page_title = models.CharField(verbose_name = 'Заголовок страницы', max_length=255, default="Заголовок" )

    page_nav = models.CharField(verbose_name='Ссылка', max_length=255, default="Ссылка")

    page_nav_position = models.IntegerField(verbose_name = 'Приоритет ссылки в навигации (0 - исключить)', default=1, help_text="большее - число правее, 0 - исключить из навигации")

    page_content = models.TextField(verbose_name = 'Основное содержание страницы',
    default = '<a id="top_of _page" href="#h1" class="card-link">на начало</a>   <h6 class="card-subtitle mb-2 text-body-secondary ">   <a id="h1">Я</a></h6>   <p class="card-text">ФИО: Мэри <br/> Номер телефона: +88 888-888-88-88 <br/> Электронка: 88@77.ru <br/> Резюме: <br/> Выпускник старшей школы, знаю три языка, не умею играть на виалончели, умею писать левой рукой и стоять на одной ноге. </p><br/>  <img src="/static/images/me.png"  height="30px">    <a href="#top_of _page" class="card-link>вернуься в начало</a>')

    current_date = models.DateTimeField(verbose_name = "Дата Записи", auto_now=True)

    class Meta:
        verbose_name = 'Текущая страница'
        verbose_name_plural = 'Все мои страницы'
        ordering = ('-page_nav_position',)

    def __str__(self):
        return f"pk: {self.pk};  item_title: {self.page_title}"



