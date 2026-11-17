from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (ECON_PEASANT_GIRL, YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE,
                                   YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE)

avdalovo_marriages_1782 = marriage_records(
    "ГАРО", "627", "298", "12", "Авдалово", "Николая Чудотворца",
    1782,
    *page("28об",
          *marriage_month(Month.JANUARY,
                          marriage(1, 21,
                                   groom=person("Михаил", "Никитин", residence="Журавкино"), groom_age=17, groom_marriage_num=1,
                                   bride=person("Федосья", "Гаврилова", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=19, bride_marriage_num=1),
                          ),
          *marriage_month(Month.APRIL,
                          marriage(2, 17,
                                   groom=person("Илья", "Артемьев", residence="Журавкино", status=YASAK_PEASANT_BOY), groom_age=15, groom_marriage_num=1,
                                   bride=person("Прасковья", "Артемьева", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=16, bride_marriage_num=1),
                          ),
          ),
    *page("29",
          *marriage_month(Month.MAY,
                          marriage(3, 9,
                                   groom=person("Гаврила", "Гаврилов", residence="Журавкино"), groom_age=17, groom_marriage_num=1,
                                   bride=person("Мавра", "Абрамова", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=20, bride_marriage_num=1),
                          ),
          *marriage_month(Month.OCTOBER,
                          marriage(4, 24,
                                   groom=person("Антон", "Моисеев", residence="Журавкино"), groom_age=19, groom_marriage_num=1,
                                   bride=person("Марфа", "Антипова", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=18, bride_marriage_num=1),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=ECON_PEASANT_GIRL
    ),
)
