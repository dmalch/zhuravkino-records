from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

avdalovo_marriages_1784 = marriage_records(
    "ГАРО", "627", "298", "17", "Авдалово", "Николая Чудотворца",
    1784,
    *page("343",
          *marriage_month(Month.JULY,
                          marriage(1, 8,
                                   groom=person("Кирил", "Аврамов", residence="Журавкино"), groom_age=26, groom_marriage_num=1,
                                   bride=person("Татьяна", "Федорова", residence="Журавкино"), bride_age=24, bride_marriage_num=1),
                          marriage(2, 10,
                                   groom=person("Иван", "Феодоров", residence="Журавкино", status=YASAK_PEASANT_BOY), groom_age=21, groom_marriage_num=1,
                                   bride=person("Анна", "Федорова", residence="Журавкино"), bride_age=18, bride_marriage_num=1),
                          marriage(3, 10,
                                   groom=person("Яковъ", "Ильинъ", residence="Журавкино"), groom_age=22, groom_marriage_num=1,
                                   bride=person("Елена", "Леонтиева", residence="Журавкино"), bride_age=17, bride_marriage_num=1),
                          ),
          *marriage_month(Month.OCTOBER,
                          marriage(4, 20,
                                   groom=person("Тарасий", "Дмитриев", residence="Журавкино", status=YASAK_PEASANT_BOY), groom_age=20, groom_marriage_num=1,
                                   bride=person("Параскева", "Сергеева", residence="Журавкино"), bride_age=19, bride_marriage_num=1),
                          marriage(5, 20,
                                   groom=person("Михаил", "Николаев", residence="Журавкино", status=YASAK_PEASANT_BOY), groom_age=16, groom_marriage_num=1,
                                   bride=person("Праскева", "Кондратьева", residence="Журавкино"), bride_age=15, bride_marriage_num=1),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
