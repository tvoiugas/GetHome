import django_filters
from .models import Tag


class EstateFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        label='тег', field_name="tags", queryset=Tag.objects.all(), widget=django_filters.widgets.LinkWidget)
from random import choice, choices
import django_filters
from .models import Tag, Estate
from django.forms.fields import IntegerField


ESTATE_TYPE_CHOICES_FILTER = [
    ('H', 'Дом'),
    ('F', 'Квартира')
]

TOWNS_CHOICES_FILTER = [
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

class EstateFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        label='тег', field_name="tags", queryset=Tag.objects.all(), widget=django_filters.widgets.LinkWidget)
    estate_type = django_filters.ChoiceFilter(choices=ESTATE_TYPE_CHOICES_FILTER)
    location = django_filters.ChoiceFilter(choices=TOWNS_CHOICES_FILTER)
    
    class Meta:
        model = Tag
        fields = []

