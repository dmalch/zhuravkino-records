from corpus.statuses import (SLEPTSOV_GM_PEASANT_FEMALE, SLEPTSOV_GM_PEASANT_MALE,
                             SLEPTSOV_TI_PEASANT_MALE)
from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

avdalovo_deaths_1784 = death_records(
    "ГАРО", "627", "298", "17", "Авдалово", "Николая Чудотворца",
    1784,
    *page("343об",
          *death_month(Month.FEBRUARY,
                       death(1, Gender.FEMALE, 15, None,
                             deceased=person("Агрипина", "Алексеева", residence="Журавкино"), age=55,
                             relatives=[relative(person("Мартин", "Константинов" ), Relationship.HUSBAND)],
                             source_age_error="«55» сверено по скану (л. 343об: обе «5» как «5» графы номеров, не «3»); "
                                              "20 в РС 1762 (двор 58, «Агафья Михайлова») и 42 в 1782 по РС 1795 "
                                              "(двор 56, «Аграфена Михайлова», единственная жена Мартына, «умре въ "
                                              "1786») — р. ок. 1740; отчество «Алексѣева» тоже описка причта"),
                       ),
          *death_month(Month.MAY,
                       death(2, Gender.MALE, 10, None,
                             deceased=person("Сергей", "Иевлев", status=SLEPTSOV_TI_PEASANT_MALE, comment="отчество неразборчиво написано"), age=82),
                       ),
          *death_month(Month.OCTOBER,
                       death(3, Gender.FEMALE, 20, None,
                             deceased=person("Григерья", "Михайлова", residence="Журавкино", status=SLEPTSOV_GM_PEASANT_FEMALE), age=47,
                             relatives=[relative(person("Федот", "Федотов", status=SLEPTSOV_GM_PEASANT_MALE), Relationship.HUSBAND)]),
                       death(4, Gender.MALE, 27, None,
                             deceased=person("Егор", "Васильев", residence="Журавкино"), age=49),
                       ),
          *death_month(Month.DECEMBER,
                       death(5, Gender.MALE, 14, None,
                             deceased=person("Дмитрий", "Леонтиев", residence="Журавкино"), age=40),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
