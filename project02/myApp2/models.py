from django.db import models

c_choices = (
    (2020, "двадцатый"),
    (2021, "двадцать первый"),
    (2022, "двадцать второй"),
    (2023, "двадцать третий"),
    (2024, "двадцать четвертый"),
)


class StudentModel(models.Model):
    task = models.CharField(
        verbose_name="Образовательная программа",
        default="Востоковедение",
        max_length=255,
    )
    a = models.CharField(
        verbose_name="Имя студента",
        default="Мэри",
        max_length=255,
    )
    b = models.CharField(
        verbose_name="Язык", default="японский" , help_text="мы все учим восточные языки",
        max_length = 255,
    )
    c = models.IntegerField(
        verbose_name="Год поступления",
        choices=c_choices,
        default=3,
    )
    result = models.CharField(
        verbose_name="Результат",
        default="Результат не определен",
        max_length=255,
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения(save)", auto_now=True
    )

    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"self.id:{self.id}; self.task:{self.task}"

    class Meta:
        verbose_name = "Таблица_студентов"
        verbose_name_plural = "Таблицы_студентов"
        ordering = ("-pk", )






















