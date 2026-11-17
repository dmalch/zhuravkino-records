from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (ECON_PEASANT_GIRL, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

avdalovo_marriages_1793 = marriage_records(
    "ГАВО (Воронеж)", "281", "1", "31", "Авдалово", "Николая Чудотворца",
    1793,
    *page("292об",
          *marriage_month(Month.JUNE,
                          marriage(1, 14,
                                   groom=person("Григорий", "Тимофеев", residence="Журавкино"), groom_age=18, groom_marriage_num=1,
                                   bride=person("Марья", "Климова", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=19, bride_marriage_num=1),
                          ),
          *marriage_month(Month.SEPTEMBER,
                          marriage(2, 11,
                                   groom=person("Ефим", "Ефимов", residence="Журавкино"), groom_age=17, groom_marriage_num=1,
                                   bride=person("Степанида", "Яковлева", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=16, bride_marriage_num=1),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=ECON_PEASANT_GIRL
    ),
)
