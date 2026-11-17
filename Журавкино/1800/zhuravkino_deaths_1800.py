from corpus.statuses import SLEPTSOV_TI_PEASANT_MALE
from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.causes_of_death import NATURAL
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

zhuravkino_deaths_1800 = death_records(
    "ГАТО", "1049", "10", "90", "Журавкино", "Николая Чудотворца",
    1800,
    *page("18об",
          *death_month(Month.JANUARY,
                       death(1, Gender.MALE, 10, None,
                             deceased=person("Осип", "Егоров"), age=50),
                       ),
          *death_month(Month.FEBRUARY,
                       death(2, Gender.MALE, 28, None,
                             deceased=person("Каллиник"), age=80),
                       # «29 го», а не 28: над записью № 2 стоит «Февраля 28 числа»,
                       # над № 3 — «29 го», и вторая цифра — девятка с хвостом, не
                       # двупетельная восьмёрка того же писца. 1800 г. по юлианскому
                       # календарю високосный (вековых исключений нет). Сверено по
                       # скану 22.09.2026 при 7×, кадр 4 альбома «1799-1800 (ГАТО
                       # 1049-10-90)»; окно сохранено в Журавкино/scans.toml.
                       death(3, Gender.MALE, 29, None,
                             deceased=person("Елисей", "Ильин"), age=40),
                       ),
          *death_month(Month.MARCH,
                       death(4, Gender.MALE, 3, None,
                             deceased=person("Иван", "Борисов", residence="Авдалово", status=SLEPTSOV_TI_PEASANT_MALE), age=79),
                       death(5, Gender.FEMALE, 26, None,
                             deceased=person("Екатерина", "Афанасьева"),
                             comment="возраст не указан"),
                       ),
          *death_month(Month.JUNE,
                       death(5, Gender.MALE, 10, None,
                             deceased=person("Гаврила", "Иванов"), age=70),
                       ),
          ),
    *page("227об",
          archive="ЦГАРМ", fund="57", inventory="6", case="36", church="Николаевская",
          *death_month(Month.OCTOBER,
                       death(1, Gender.MALE, 15, None,
                             deceased=person("Леонтий", "Иванов"), age=80),
                       ),
          *death_month(Month.NOVEMBER,
                       death(1, Gender.FEMALE, 20, None,
                             deceased=person("Агрепина", "Моисеева", status="новокрещеная"), age=78),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
