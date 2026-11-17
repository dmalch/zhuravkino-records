from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_LEGAL_WIFE, KAZENNYJ_PEASANT_MALE, MAIDEN

# Журавкинцы въ книгахъ чужихъ приходовъ 1866 г. — ЦГАРМ 57-6-498а (сводная книга Спасскаго уѣзда),
# найдены по OCR Яндексъ.Архива (docs/research/2026-10-30-yandex-other-parishes.md), прочитаны по сканамъ
# 07.11.2026; reviewed=False. Внесены только записи, гдѣ журавкинецъ — родитель.

other_births_1866_korgoshino = birth_records(
    "ЦГАРМ", "57", "6", "498а", "Коргошино", "Троицкая",
    1866,
    *birth_month(Month.JULY,
        birth(22, Gender.FEMALE, 16, 17,
              child=person("Марія"),
              father=person("Иванъ", "Игнатіевъ", status=KAZENNYJ_PEASANT_MALE, residence="Журавкино"),
              mother=person("Софія", "Александрова", status=KAZENNYJ_PEASANT_LEGAL_WIFE),
              god_parent1=person("Стефанъ", "Димитріевъ", last_name_orig="Шышкуновъ", status=KAZENNYJ_PEASANT_MALE, residence="Коргошино", comment="отчество у корешка, читается неуверенно"),
              god_parent2=person("Ксенія", "Михаилова", status=MAIDEN, residence="Анаево"),
              comment="Яндексъ.Архивъ, сканъ 99; умерла 21 сентября того же года (other_deaths_1866)"),
    ),
    reviewed=False,
)
