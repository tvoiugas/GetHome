from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django_earthdistance.models import EarthDistanceQuerySet


class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Estate(models.Model):
    TOWNS_CHOICES = [
        ('B', 'Бишкек'), ('AD', 'Ак-Джол'), ('AB', 'Ала-Бука'),
        ('AT', 'Ала-Тоо'), ('AN', 'Аламедин'), ('AU', 'Алмалуу'),
        ('AO', 'Ананьево'), ('AR', 'Араван'), ('ARSH', 'Арашан'),
        ('AI', 'Арчалы'), ('ABI', 'Ат-Башы'), ('BT', 'Бает'),
        ('BV', 'Баетов'), ('BKN', 'Базар-Коргон'), ('BK', 'Байтик'),
        ('BAI', 'Бакай-Ата'), ('BDU', 'Бактуу-Долоноту'), ('BI', 'Балыкчы'),
        ('BN', 'Баткен'), ('BE', 'Беловодское'), ('BKI', 'Беш-Кюнгей'),
        ('BIK', 'Бирдик'), ('BO', 'Боконбаево'), ('BOI', 'Бостери'),
        ('BA', 'Буденовка'),  ('BSU', 'Булан-Соготту'),
        ('VAA', 'Военно-Антоновка'),
        ('GA', 'Гавриловка'), ('GMA', 'Горная Маевка'), ('GEA', 'Григорьевка'),
        ('GLA', 'Гульча'), ('DKN', 'Дароот-Коргон'), ('D', 'Дачное(ГЕС-5)'),
        ('DZH', 'Джал мкр.'), ('DZHA', 'Джалал-Абад'), ('DZHD', 'Джаны-Джер'),
        ('DA', 'Дмитриевка'), ('ZHV', 'Жаркынбаев'), ('ZE', 'Заречное'),
        ('Z', 'Заря'), ('I', 'Ивановка'), ('IA', 'Исфана'),
        ('KAI', 'Кадамжай'), ('KSI', 'Каджи-Сай'), ('KN', 'Казарман'),
        ('KI', 'Каинды'), ('KA', 'Каирма'), ('K', 'Кант'),
        ('KKI', 'Каныш-Кия'), ('KB', 'Кара-Балта'), ('KK', 'Кара-Кульджа'),
        ('KO', 'Кара-Ой'), ('KS', 'Кара-Суу'), ('KKU', 'Кара-Куль'),
        ('KL', 'Каракол'), ('KT', 'Кашат'), ('KSU', 'Кашка-Суу'),
        ('KIN', 'Кемин'), ('KEN', 'Кербен'), ('KOE', 'Кировское'),
        ('KR', 'Кожояр'), ('KTSH', 'Кой-Таш'), ('KDZH', 'Кой-Джар'),
        ('KOI', 'Кок-Ой'), ('KKA', 'Константиновка'), ('KU', 'Корумду'),
        ('KOR', 'Кочкор'), ('KORA', 'Кочкор-Ата'), ('KRA', 'Красная Речка'),
        ('KTU', 'Кунтуу'), ('KAR', 'Кызыл-Адыр'), ('KKIA', 'Кызыл-Кия'),
        ('KLSU', 'Кызыл-Суу'), ('KLTU', 'Кызыл-Туу'), ('LA', 'Лебединовка'),
        ('LE', 'Ленинское'), ('LGE', 'Луговое'), ('MA', 'Маевка'),
        ('MSU', 'Майлуу-Суу'), ('ME', 'Маловодное'), ('MS', 'Манас'),
        ('MI', 'Массы'), ('MN', 'Милянфан'), ('MKA', 'Михайловка'),
        ('M', 'Мыкан'), ('N', 'Нарын'), ('NN', 'Нижний Норус'),
        ('NA', 'Новопавловка'), ('NKA', 'Новопокровка'), ('NT', 'Ноокат'),
        ('NS', 'Норус'), ('OA', 'Орловка'), ('OS', 'Орто-Сай'),
        ('O', 'Ош'), ('PA', 'Покровка'), ('PE', 'Пригородное'),
        ('PN', 'Пульгон'), ('RE', 'Раздольное'), ('SE', 'Садовое (ГЭС-3)'),
        ('SOE', 'Селекционное'), ('SA', 'Семеновка'), ('S', 'Сокулук'),
        ('SK', 'Сретенка'), ('STOE', 'Студенческое'), ('SAK', 'Сузак'),
        ('STA', 'Сулюкта'), ('T', 'Талас'), ('TI', 'Тамчы'),
        ('TMK', 'Таш-Мойнок'), ('TR', 'Темир'), ('TA', 'Теплоключенка'),
        ('TB', 'Тогул Булак'), ('TK', 'Токмок'), ('TL', 'Токтогул'),
        ('TIK', 'Тынчтык'), ('TUP', 'Тюп'), ('U', 'Узген'),
        ('CH', 'Чаек'), ('CHR', 'Чалдавар'), ('CHK', 'Чат Кёль'),
        ('CHT', 'Чок-Тал'), ('CHA', 'Чолпон-Ата'), ('CHSI', 'Чон Сары-Ой'),
        ('CHAK', 'Чон-Арык'), ('CHD', 'Чон-Далы'), ('CHT', 'Чон-Таш'),
        ('CHCHK', 'Чункурчак'), ('SHO', 'Шевченко'), ('SHV', 'Шопоков'),
        ('U', 'Юрьевка'), ('PD', 'пос. Дачный')
    ]

    ESTATE_TYPE_CHOICES = [
        ('H', 'Дом'),
        ('F', 'Квартира')
    ]

    title = models.CharField(_('Название'), max_length=256)
    estate_type = models.CharField(
        _('Вид собственности'), max_length=1,
        choices=ESTATE_TYPE_CHOICES, null=False)
    slug = models.SlugField(max_length=256, blank=True)
    description = models.TextField(_('Описание'))
    location = models.CharField(
        _('Местонахождение'), max_length=5, choices=TOWNS_CHOICES)
    posted_on = models.DateField(_('Опубликовано'), auto_now=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        null=False,
        related_name='estates', verbose_name='Автор')
    price = models.IntegerField(_('Цена'))
    area = models.IntegerField(_('Площадь'))
    photo = models.ImageField(
        _('Изображение'), upload_to='estate_photos/', max_length=255)
    video = models.FileField(_('Видео'), upload_to='estate_videos',
                             null=True, blank=True,
                             validators=[FileExtensionValidator(
                                allowed_extensions=[
                                    'MOV', 'avi', 'mp4', 'webm', 'mkv']
                                )])
    tags = models.ManyToManyField(
        Tag, verbose_name="теги", related_name='estate')

    latitude = models.FloatField(_('Координаты восточной широты'), null=True)
    longitude = models.FloatField(_('Координаты северной долготы'), null=True)

    objects = EarthDistanceQuerySet.as_manager()

    class Meta:
        verbose_name = 'Имущество'
        verbose_name_plural = 'Имущества'
        ordering = ['-id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Estate, self).save(*args, **kwargs)


class Details(models.Model):
    bathrooms = models.IntegerField(
        _('Ванные комнаты'), null=True, blank=True, default=1)
    bedrooms = models.IntegerField(
        _('Спальни'), null=True, blank=True, default=1)
    garages = models.IntegerField(
        _('Гаражи'), null=True, blank=True, default=0)
    floors = models.IntegerField(
        _('Количество этажей'), null=True, blank=True, default=0)
    floor_on = models.IntegerField(_('Этаж'), null=True, blank=True)
    estate = models.OneToOneField(
        Estate, on_delete=models.CASCADE,
        related_name='details', verbose_name='Имущество')

    class Meta:
        verbose_name = 'Детали'
        verbose_name_plural = 'Детали'

    def __str__(self):
        return self.estate.title

    def save(self, *args, **kwargs):
        print(self.estate.estate_type)
        if self.estate.estate_type == 'F':
            self.garages = None
            self.floors = None
        super(Details, self).save(*args, **kwargs)


class Feature(models.Model):
    KIND_CHOICES = [
        ('HF', 'Пол с подогревом'),
        ('PO', 'Двор'),
        ('GN', 'Сад'),
        ('SP', 'Бассейн'),
    ]

    kind = models.CharField(_('Тип'), max_length=3,
                            choices=KIND_CHOICES, null=True)
    estate = models.ForeignKey(Estate, verbose_name='Детали',
                               related_name='features',
                               on_delete=models.CASCADE, default=0)

    class Meta:
        verbose_name = 'Особенности'
        verbose_name_plural = 'Особенности'

    def __str__(self):
        return self.estate.title



