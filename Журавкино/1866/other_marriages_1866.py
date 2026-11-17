from verso.ru.dsl import (Month, Relationship, marriage, marriage_month, marriage_records, person,
                          relative)
from verso.ru.dsl.statuses import (DEACON, DYACHOK, DYACHOK_SON, KAZENNYJ_PEASANT_DAUGHTER,
                                   KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MAIDEN,
                                   KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_WIDOW, PRIEST,
                                   PRIEST_DAUGHTER_MAIDEN, RETIRED_SOLDIER, SEXTON, UNTER_OFFICER)

# Журавкинцы въ книгахъ чужихъ приходовъ 1866 г. — ЦГАРМ 57-6-498 и 57-6-498а (сводныя книги Спасскаго
# уѣзда), найдены по OCR Яндексъ.Архива (docs/research/2026-10-30-yandex-other-parishes.md), прочитаны по
# сканамъ 07.11.2026; reviewed=False. Внесены только браки, гдѣ журавкинецъ — женихъ или невѣста.
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1866_novye_vyselki = marriage_records(
    "ЦГАРМ", "57", "6", "498", "Новые Выселки", "Покровская",
    1866,
    *marriage_month(Month.JULY,
        marriage(15, 24,
                 groom=person("Кондратій", "Михаиловъ", last_name_orig="Топаевъ", status=UNTER_OFFICER, residence="Новые Выселки", comment="отставной, выслужившій 15-лѣтній срокъ, проживающій въ селѣ Новыхъ Выселкахъ"),
                 groom_marriage_num=2, groom_age=36,
                 bride=person("Анна", "Егорова", status=KAZENNYJ_PEASANT_FEMALE, residence="Журавкино"),
                 bride_marriage_num=2, bride_age=21,
                 witness1=person("Даніилъ", "Родіоновъ", last_name_orig="Бочковъ", status=RETIRED_SOLDIER, residence="Новые Выселки", comment="въ записи № 19 той же книги — «Бычковъ»"),
                 witness2=person("Николай", "Лаврентіевъ", status=KAZENNYJ_PEASANT_MALE, residence="Новые Выселки"),
                 witness3=person("Матвѣй", "Евдокимовъ", status=KAZENNYJ_PEASANT_MALE, residence="Новые Выселки"),
                 witness4=person("Симеонъ", "Дорофеевъ", status=KAZENNYJ_PEASANT_MALE, residence="Новые Выселки"),
                 comment="Яндексъ.Архивъ 57-6-498, сканъ 130; лѣта жениха вписаны блѣдно («36»)"),
    ),
    reviewed=False,
)

other_marriages_1866_mankiryaevo = marriage_records(
    "ЦГАРМ", "57", "6", "498а", "Манкиряево", "Николаевская",
    1866,
    *marriage_month(Month.JANUARY,
        marriage(5, 23,
                 groom=person("Романъ", "Епифановъ", status=KAZENNYJ_PEASANT_MALE, residence="Манкиряево"),
                 groom_marriage_num=1, groom_age=20,
                 bride=person("Татіана", "Яковлева", last_name_orig="Попова", status=KAZENNYJ_PEASANT_MAIDEN, residence="Журавкино"),
                 bride_marriage_num=1, bride_age=18,
                 witness1=person("Никита", "Петровъ", status=KAZENNYJ_PEASANT_MALE, residence="Манкиряево"),
                 witness2=person("Гавріилъ", "Максимовъ", status=KAZENNYJ_PEASANT_MALE, residence="Манкиряево"),
                 witness3=person("Спиридонъ", "Іосифовъ", status=KAZENNYJ_PEASANT_MALE, residence="Манкиряево"),
                 witness4=person("Прокопій", "Симеоновъ", status=KAZENNYJ_PEASANT_MALE, residence="Манкиряево"),
                 relatives=[relative(person("Епифанъ", "Емельяновъ", status=KAZENNYJ_PEASANT_MALE, residence="Манкиряево", comment="умершій"), Relationship.FATHER, "жених"),
                            relative(person("Яковъ", "Николаевъ", last_name_orig="Поповъ", status=KAZENNYJ_PEASANT_MALE, residence="Журавкино", comment="умершій"), Relationship.FATHER, "невеста")],
                 comment="Яндексъ.Архивъ 57-6-498а, сканъ 199"),
    ),
    reviewed=False,
)

other_marriages_1866_anaevo = marriage_records(
    "ЦГАРМ", "57", "6", "498а", "Анаево", "Покровская",
    1866,
    *marriage_month(Month.AUGUST,
        marriage(15, 26,
                 groom=person("Алексѣй", "Ѳеодоровъ", last_name_orig="Молчановъ", status=DYACHOK_SON, residence="Журавкино", comment="окончившій курсъ Тамбовской семинаріи"),
                 groom_marriage_num=1, groom_age=21,
                 bride=person("Александра", "Петрова", status=PRIEST_DAUGHTER_MAIDEN),
                 bride_marriage_num=1, bride_age=16,
                 witness1=person("Иванъ", last_name_orig="Цвѣтковъ", status=DYACHOK, comment="города Шацка, церковь не дочитана"),
                 witness2=person("Александръ", last_name_orig="Богородицкій", status=DEACON, residence="Журавкино"),
                 witness3=person("Егоръ", "Павловъ", status=DYACHOK, residence="Анаево"),
                 witness4=person("Ефимъ", "Стефановъ", status=SEXTON, residence="Боковой Майдан"),
                 relatives=[relative(person("Ѳеодоръ", "Никитинъ", status=DYACHOK, residence="Журавкино"), Relationship.FATHER, "жених"),
                            relative(person("Петръ", last_name_orig="Виноградовъ", status=PRIEST, comment="умершій"), Relationship.FATHER, "невеста")],
                 comment="Яндексъ.Архивъ 57-6-498а, сканъ 260; вѣнчалъ священникъ Боковаго Майдана Іоаннъ Шумлянскій. "
                         "Женихъ — по всей видимости, тотъ Алексѣй Молчановъ, что съ 1866 г. священникъ въ Анаевѣ "
                         "(подписи въ книгахъ 1866 и 1900 гг.)"),
    ),
    *marriage_month(Month.OCTOBER,
        marriage(24, 23,
                 groom=person("Григорій", "Даниловъ", status=KAZENNYJ_PEASANT_MALE, residence="Анаево"),
                 groom_marriage_num=1, groom_age=18,
                 bride=person("Мавра", "Семенова", status=KAZENNYJ_PEASANT_DAUGHTER, residence="Журавкино"),
                 bride_marriage_num=1, bride_age=17,
                 witness1=person("Василій", "Кондратьевъ", residence="Коргошино"),
                 witness2=person("Василій", "Никитинъ", residence="Анаево"),
                 witness3=person("Василій", "Михаиловъ", status=KAZENNYJ_PEASANT_MALE, residence="Крюковка"),
                 witness4=person("Иванъ", "Андреевъ", status=KAZENNYJ_PEASANT_MALE, residence="Крюковка"),
                 relatives=[relative(person("Даніилъ", "Прокопіевъ", status=KAZENNYJ_PEASANT_MALE, residence="Анаево", comment="умершій"), Relationship.FATHER, "жених"),
                            relative(person("Евдокія", "Сергеева", status=KAZENNYJ_PEASANT_WIDOW, residence="Журавкино"),
                                     Relationship.MOTHER, "невеста")],
                 comment="Яндексъ.Архивъ 57-6-498а, сканъ 262; мѣсяцъ — по заголовку «Октябрь» на сканѣ 261"),
    ),
    reviewed=False,
)
