from verso.ru.dsl import Month, marriage, marriage_month, marriage_records, person
from verso.ru.dsl.statuses import MESHCHANIN, PEASANT_MALE, PEASANT_WIDOW

# Авдаловка въ московской книгѣ 1913 г. — ЦГА Москвы 2125-2-2 (Пречистенскій сорокъ, Антипіевская ц.), найдено
# по OCR Яндексъ.Архива, прочитано по оригиналу 07.11.2026; reviewed=False. Обыскная книга той же свадьбы —
# 2125-3-22 (сканъ 15), паспортъ невѣсты — 2125-3-21 (сканъ 54).
# Поручители: первые двое — со стороны жениха, вторые — невѣсты.

other_marriages_1913_moscow_antipievskaya = marriage_records(
    "ЦГА Москвы", "2125", "2", "2", "Москва", "Антипиевская",
    1913,
    *marriage_month(Month.NOVEMBER,
        marriage(28, 3,
                 groom=person("Павелъ", "Сергѣевъ", last_name_orig="Карасевъ", status=PEASANT_MALE, comment="Рязанской губ., Ряжскаго у., Косьмо-Даміанской вол., дер. Павловки"),
                 groom_marriage_num=2, groom_age=31,
                 bride=person("Наталія", "Михайлова", last_name_orig="Лагунова", status=PEASANT_WIDOW, residence="Авдалово"),
                 bride_marriage_num=2, bride_age=30,
                 witness1=person("Григорій", "Іоанновъ", last_name_orig="Зуевъ", status=PEASANT_MALE, comment="Московской губ., Подольскаго у., Молодинской вол., с. Молоди"),
                 witness2=person("Василій", "Александровъ", last_name_orig="Хлѣбниковъ", status=MESHCHANIN),
                 witness3=person("Николай", "Михайловъ", last_name_orig="Шепелевъ", status=MESHCHANIN, comment="г. Коломны"),
                 witness4=person("Василій", "Димитріевъ", last_name_orig="Чумарковъ", status=PEASANT_MALE, comment="Подольскаго у., Десенской вол., дер. Лапшинки"),
                 comment="Яндексъ.Архивъ 2125-2-2, сканъ 199; вѣнчалъ свящ. Александръ Казанскій"),
    ),
    reviewed=False,
)
