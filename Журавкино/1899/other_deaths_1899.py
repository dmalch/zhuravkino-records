from verso.ru.dsl import Gender, Month, death, death_month, death_records, person

# Журавкинка въ книгѣ чужого прихода 1899 г. — ЦГАРМ 57-7-39 (Мордовскій Пимбуръ), найдено по OCR
# Яндексъ.Архива, прочитано по скану 07.11.2026; reviewed=False. Церковь въ заголовкѣ книги не названа.

other_deaths_1899_mordovsky_pimbur = death_records(
    "ЦГАРМ", "57", "7", "39", "Мордовский Пимбур", "",
    1899,
    *death_month(Month.MARCH,
        death(24, Gender.FEMALE, 30, 31,
              deceased=person("Ольга", "Васильева", last_name_orig="Купленская", status="жена священника", residence="Журавкино"),
              cause_of_death="естественной смерти",
              comment="Яндексъ.Архивъ 57-7-39, сканъ 120; графа лѣтъ ушла въ корешокъ"),
    ),
    reviewed=False,
)
