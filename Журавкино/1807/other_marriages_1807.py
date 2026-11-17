from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, page, person
from verso.ru.dsl.statuses import YASAK_PEASANT_BOY, YASAK_PEASANT_GIRL

other_marriages_1807 = marriage_records(
    "ЦГАРМ", "57", "6", "63а", "Анаево", "Покровская",
    1807,
    *page("230",
          *marriage_month(Month.FEBRUARY,
                          marriage(5, 4,
                                   groom=person("Михаил", "Карпов", status=YASAK_PEASANT_BOY, residence="Анаево"),
                                   bride=person("Домника", "Никифорова", status=YASAK_PEASANT_GIRL, residence="Журавкино"),
                                   page="33")),
          *marriage_month(Month.SEPTEMBER,
                          marriage(12, 23,
                                   groom=person("Игнатий", "Герасимов", status=YASAK_PEASANT_BOY, residence="Анаево"),
                                   bride=person("Агрипина", "Семенова", status=YASAK_PEASANT_GIRL, residence="Журавкино"),
                                   page="33")),
          ),
)
