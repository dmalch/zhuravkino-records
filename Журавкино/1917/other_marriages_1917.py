from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import PEASANT_GIRL, PEASANT_MALE

# Авдаловка въ московской книгѣ 1917 г. — ЦГА Москвы 2126-2-122 (Крестовоздвиженская ц. Сретенскаго сорока),
# найдено по OCR Яндексъ.Архива, прочитано по оригиналу 07.11.2026; reviewed=False.
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1917_moscow_krestovozdvizhenskaya = marriage_records(
    "ЦГА Москвы", "2126", "2", "122", "Москва", "Крестовоздвиженская",
    1917,
    *marriage_month(Month.MAY,
        marriage(32, 24,
                 groom=person("Иванъ", "Ивановъ", last_name_orig="Колитовъ", status=PEASANT_MALE, comment="«ефрейторъ 3-й роты 12-го желѣзнодорожнаго баталіона изъ крестьянъ Тамбовской губ., " "Спасскаго у., Майданской волости и села» — село не названо"),
                 groom_marriage_num=1, groom_age=29,
                 bride=person("Софія", "Николаева", last_name_orig="Калинкина", status=PEASANT_GIRL, residence="Авдалово"),
                 bride_age=22,
                 witness1=person("Андрей", "Козьминъ", last_name_orig="Кузнецовъ", status=PEASANT_MALE, comment="Рязанской губ."),
                 witness2=person("Михаилъ", "Егоровъ", last_name_orig="Удачинъ", status=PEASANT_MALE, comment="Ярославской губ., Мышкинскаго у."),
                 witness3=person("Владиміръ", "Валеріановъ", last_name_orig="Дудкевичъ", status=PEASANT_MALE, comment="Могилевской губ."),
                 witness4=person("Иванъ", "Петровъ", last_name_orig="Картошкинъ", status=PEASANT_MALE, comment="Калужской губ., Мещовскаго у."),
                 comment="Яндексъ.Архивъ 2126-2-122, сканъ 194; вѣнчалъ свящ. Василій Смирновъ"),
    ),
    reviewed=False,
)
