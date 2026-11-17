from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import YASAK_PEASANT_BOY, YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE

other_marriages_1827 = marriage_records(
    "ЦГАРМ", "57", "6", "124", "Анаево", "Покровская",
    1827,
    *marriage_month(Month.OCTOBER,
        marriage(28, 27,
                 groom=person("Григорий", "Фомин", status=YASAK_PEASANT_BOY, residence="Каргашино"),
                 bride=person("Марфа", "Егорова", status=YASAK_PEASANT_GIRL, residence="Журавкино"),
                 witness1=person("Илья", "Абрамов", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 witness2=person("Григорий", "Петров", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 witness4=person("Анисим", "Никитин", status=YASAK_PEASANT_MALE, residence="Каргашино"),
                 page="339"
                 ),
    ),
)
