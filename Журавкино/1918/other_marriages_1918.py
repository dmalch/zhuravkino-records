from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE

# Журавкинки въ книгѣ с. Каргашина 1918 г. — ЦГАРМ 57-8-138 (дѣло «Зарубкино, 1912–1918», разделъ 1918 г. по
# оглавленію Яндекса; годъ въ шапкѣ у корешка), найдено по OCR Яндексъ.Архива, прочитано по оригиналамъ 07.11.2026;
# reviewed=False. Вѣнчалъ свящ. Дм. Кочетовъ.
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1918_kargashino = marriage_records(
    "ЦГАРМ", "57", "8", "138", "Каргашино", "",
    1918,
    *marriage_month(Month.FEBRUARY,
        marriage(16, 2,
                 groom=person("Леонтій", "Ивановъ", last_name_orig="Карасевъ", status=PEASANT_MALE, residence="Каргашино"),
                 groom_marriage_num=1, groom_age=22,
                 bride=person("Анна", "Григорьева", last_name_orig="Шарова", status=PEASANT_GIRL, residence="Журавкино"),
                 bride_age=18,
                 witness1=person("Степанъ", last_name_orig="Бейгуловъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness2=person("Димитрій", "Ивановъ", last_name_orig="Карасевъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness3=person("Алексѣй", "Ивановъ", last_name_orig="Сорокинъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness4=person("Михаилъ", last_name_orig="Карасевъ", status=PEASANT_MALE, residence="Каргашино"),
                 comment="Яндексъ.Архивъ 57-8-138, сканъ 501"),
        marriage(37, 23,
                 groom=person("Ѳедоръ", "Петровъ", last_name_orig="Лопаевъ", status=PEASANT_MALE, residence="Каргашино"),
                 groom_marriage_num=1, groom_age=22,
                 bride=person("Домна", "Петрова", last_name_orig="Панфилова", status=PEASANT_GIRL, residence="Журавкино"),
                 bride_marriage_num=1, bride_age=23,
                 witness1=person("Никита", last_name_orig="Лопаевъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness2=person("Павелъ", last_name_orig="Лопаевъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness3=person("Михей", "Андреевъ", last_name_orig="Шумбасовъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness4=person("Владиміръ", last_name_orig="Лопаевъ", status=PEASANT_MALE, residence="Каргашино"),
                 comment="Яндексъ.Архивъ 57-8-138, сканъ 503"),
        marriage(38, 23,
                 groom=person("Матвѣй", "Максимовъ", last_name_orig="Аношкинъ", status=PEASANT_MALE, residence="Каргашино"),
                 groom_marriage_num=1,
                 bride=person("Васса", "Иванова", last_name_orig="Бункина", status=PEASANT_GIRL, residence="Журавкино"),
                 bride_marriage_num=1, bride_age=20,
                 witness1=person("Евѳимъ", last_name_orig="Аношкинъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness2=person("Димитрій", last_name_orig="Карасевъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness3=person("Димитрій", "Михайловъ", last_name_orig="Шадиловъ", status=PEASANT_MALE, residence="Каргашино"),
                 witness4=person("Павелъ", last_name_orig="Севастьяновъ", status=PEASANT_MALE, residence="Каргашино"),
                 comment="Яндексъ.Архивъ 57-8-138, сканъ 503; лѣта жениха не вписаны"),
    ),
    reviewed=False,
    civil=False,
)
