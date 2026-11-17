from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import MESHCHANIN, MESHCHANIN_DAUGHTER

other_marriages_1831 = marriage_records(
    "ЦГАРМ", "57", "6", "145а", "Кадом", "Спасо Преображенская",
    1831,
    *marriage_month(Month.JULY,
        marriage(5, 27,
                 groom=person("Кондратий", "Корнеев", last_name_orig="Каменский", status="крестьянин помещицы Анастасии Григорьевны Слепцовой", residence="Журавкино"),
                 groom_age=23,
                 bride=person("Анна", "Егорова", last_name_orig="Букина", status=MESHCHANIN_DAUGHTER, residence="Кадом"),
                 bride_age=20,
                 witness1=person("Иван", "Павлов", last_name_orig="Рожков", status=MESHCHANIN, residence="Кадом"),
                 witness2=person("Петр", "Яковлев", last_name_orig="Цыдинин", status=MESHCHANIN, residence="Кадом"),
                 page="223"
                 ),
    ),
)
