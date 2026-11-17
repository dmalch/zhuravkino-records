from verso.ru.dsl import (Month, Relationship, marriage, marriage_month, marriage_records, person,
                          relative)
from verso.ru.dsl.statuses import YASAK_PEASANT_MAIDEN, YASAK_PEASANT_MALE

other_marriages_1835 = marriage_records(
    "ЦГАРМ", "57", "1", "404", "Анаево", "Покровская",
    1835,
    *marriage_month(Month.APRIL,
        marriage(13, 21,
                 groom=person("Артем", "Васильев", status=YASAK_PEASANT_MALE, residence="Пичевка"),
                 bride=person("Дарья", "Максимова", last_name_orig="Дырина", status=YASAK_PEASANT_MAIDEN, residence="Журавкино", last_name_in_book=False),
                 witness1=person("Тимофей", "Федоров", last_name_orig="Жданов", status=YASAK_PEASANT_MALE, residence="Пичевка"),
                 witness2=person("Федосей", "Федоров", last_name_orig="Жданов", status=YASAK_PEASANT_MALE, residence="Пичевка"),
                 witness3=person("Иван", "Автономов", last_name_orig="Реткин", status=YASAK_PEASANT_MALE, residence="Пичевка"),
                 witness4=person("Андрей", "Родионов", last_name_orig="Жданов", status=YASAK_PEASANT_MALE, residence="Пичевка"),
                 relatives=[relative(person("Максим", "Федоров", last_name_orig="Дырин", residence="Журавкино", status=YASAK_PEASANT_MALE), Relationship.FATHER, "невеста")],
                 page="477"),
    ),
)
