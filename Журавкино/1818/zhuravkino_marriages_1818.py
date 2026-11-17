from corpus.statuses import (SLEPTSOV_AI_PEASANT_BOY, SLEPTSOV_AI_PEASANT_GIRL,
                             SLEPTSOV_AI_PEASANT_MALE)
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

zhuravkino_marriages_1818 = marriage_records(
    "ЦГАРМ", "57", "6", "96", "Журавкино", "Николаевская",
    1818,
    *page("202об",
          *marriage_month(Month.JANUARY,
                          marriage(1, 20,
                                   groom=person("Григорий", "Федоров", status=YASAK_PEASANT_BOY),
                                   bride=person("Пелагея", "Васильева", residence="Каргашино"),
                                   witness1=person("Иван", "Андреев"),
                                   witness2=person("Никита", "Семенов"),
                                   witness3=person("Георгий", "Амельянов")),
                          ),
          *marriage_month(Month.FEBRUARY,
                          marriage(2, 9,
                                   groom=person("Антон", "Егоров", status=YASAK_PEASANT_BOY),
                                   bride=person("Марья", "Ильина"),
                                   witness1=person("Феоктист", "Климонов"),
                                   witness2=person("Иван", "Андреев")),
                          marriage(3, 10,
                                   groom=person("Филип", "Архипов", status=SLEPTSOV_AI_PEASANT_BOY),
                                   bride=person("Лукерья", "Тимофеева", status=SLEPTSOV_AI_PEASANT_GIRL),
                                   witness1=person("Тит", "Костентинов", status=SLEPTSOV_AI_PEASANT_MALE),
                                   witness2=person("Сергей", "Егоров", status=SLEPTSOV_AI_PEASANT_MALE)),
                          marriage(4, None,
                                   groom=person("Евдоким", "Киреев", status=SLEPTSOV_AI_PEASANT_BOY),
                                   bride=person("Вера", "Иванова", status=SLEPTSOV_AI_PEASANT_GIRL),
                                   witness1=person("Иван", "Титов", status=SLEPTSOV_AI_PEASANT_MALE),
                                   witness2=person("Ион", "Тимофеев", status=SLEPTSOV_AI_PEASANT_MALE)),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
