from verso.ru.dsl import (Gender, Month, Relationship, death, death_month, death_records, person,
                          relative)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_MALE

# Журавкинецъ въ книгѣ чужого прихода 1907 г. — ЦГАРМ 57-5-24 (Лунданъ), найдено по OCR Яндексъ.Архива,
# прочитано по скану 07.11.2026; reviewed=False. Церковь въ заголовкѣ книги не названа.

other_deaths_1907_lundan = death_records(
    "ЦГАРМ", "57", "5", "24", "Лундан", "",
    1907,
    *death_month(Month.OCTOBER,
        death(16, Gender.MALE, 17, 18,
              deceased=person("Василій", status=PEASANT_MALE, residence="Журавкино", comment="отчество и фамилія не записаны"),
              cause_of_death="найденъ мертвымъ",
              comment="Яндексъ.Архивъ 57-5-24, сканъ 160; лѣта «неизвѣстныхъ лѣтъ»; погребенъ «по отношенію Пристава 2-го стана Керенскаго "
                      "уѣзда отъ 18-го Октября 1907 года за № 191»"),
    ),
    reviewed=False,
)

# Авдаловка въ московской книгѣ 1907 г. — ЦГА Москвы 203-782-525 (Крестовоздвиженская ц.; второй экземпляръ —
# 203-782-526, сканъ 823), прочитано по оригиналу 07.11.2026.
other_deaths_1907_moscow_krestovozdvizhenskaya = death_records(
    "ЦГА Москвы", "203", "782", "525", "Москва", "Крестовоздвиженская",
    1907,
    *death_month(Month.JULY,
        death(82, Gender.FEMALE, 1, 3,
              deceased=person("Евдокія", status=PEASANT_DAUGHTER, residence="Авдалово"),
              age="6 мес",
              relatives=[relative(person("Михаилъ", "Прокопіевъ", last_name_orig="Мыськовъ", status=PEASANT_MALE),
                                  Relationship.FATHER)],
              cause_of_death="отъ воспаленія желудка и кишекъ",
              comment="Яндексъ.Архивъ 203-782-525, сканъ 314; «въ домѣ Миронова»; Семеновское кладбище; "
                      "родилась 8 декабря 1906 г. (other_births_1906)"),
    ),
    reviewed=False,
)
