from verso.ru.dsl import RecordDefaults, marriage, marriage_month, marriage_records, page, person
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE

zhuravkino_marriages_1796 = marriage_records(
    "ГАРО", "627", "298", "32", "Журавкино", "Николая Чудотворца",
    1796,
    *page("570",
          *marriage_month(None,
                          marriage(1, 30,
                                   groom=person("Иван", "Нестеров"), groom_age=20, groom_marriage_num=1,
                                   bride=person("Ирина", "Максимова"), bride_age=15, bride_marriage_num=1),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
