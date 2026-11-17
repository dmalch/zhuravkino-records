from corpus.statuses import SLEPTSOV_TI_PEASANT_GIRL, SLEPTSOV_TI_PEASANT_MALE
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (ECON_PEASANT_GIRL, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

avdalovo_marriages_1773 = marriage_records(
    "ГАРО", "627", "255", "15", "Авдалово", "Николая Чудотворца",
    1773,
    *page("?",
          *marriage_month(Month.JANUARY,
                          marriage(1, 20,
                                   groom=person("Федот", "Ларионов", status=SLEPTSOV_TI_PEASANT_MALE), groom_age=18, groom_marriage_num=1,
                                   bride=person("Фекла", "Антонова", status=SLEPTSOV_TI_PEASANT_GIRL), bride_age=17, bride_marriage_num=1),
                          marriage(2, 27,
                                   groom=person("Симон", "Максимов", residence="Журавкино"), groom_age=22, groom_marriage_num=1,
                                   bride=person("Акилина", "Константинова", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=20, bride_marriage_num=1),
                          ),
          *marriage_month(Month.APRIL,
                          marriage(3, 14,
                                   groom=person("Семен", "Тихонов", residence="Журавкино"), groom_age=17, groom_marriage_num=1,
                                   bride=person("Евдокия", "Михайлова", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=19, bride_marriage_num=1),
                          ),
          *marriage_month(Month.NOVEMBER,
                          marriage(4, 3,
                                   groom=person("Семен", "Леонтьев", residence="Журавкино"), groom_age=18, groom_marriage_num=1,
                                   bride=person("Улита", "Артемьева", residence="Журавкино", status=YASAK_PEASANT_GIRL), bride_age=17, bride_marriage_num=1),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=ECON_PEASANT_GIRL
    ),
)
