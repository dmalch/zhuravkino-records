from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_WIFE, PEASANT_FEMALE, PEASANT_MALE

# Журавкинцы въ книгѣ чужого прихода 1887 г. — ЦГАРМ 57-3-79 (сводная книга Наровчатскаго уѣзда, разделъ
# «Теньгушево»), найдено по OCR Яндексъ.Архива, прочитано по скану 07.11.2026; reviewed=False.

other_births_1887_tengushevo = birth_records(
    "ЦГАРМ", "57", "3", "79", "Теньгушево", "Казанская",
    1887,
    *birth_month(Month.MARCH,
        birth(23, Gender.MALE, 3, 4,
              child=person("Василій"),
              father=person("Петръ", "Филипповъ", last_name_orig="Шаровъ", status=KAZENNYJ_PEASANT_MALE, residence="Журавкино", comment="«временно живущій» въ Теньгушевѣ"),
              mother=person("Ольга", "Алексѣева", status=KAZENNYJ_PEASANT_WIFE),
              god_parent1=person("Филимонъ", "Алексѣевъ", last_name_orig="Бѣляевъ", status=PEASANT_MALE, residence="Вадовские Селищи", comment="имя читается неуверенно"),
              god_parent2=person("Елена", "Сергѣева", last_name_orig="Сюндюкова", status=PEASANT_FEMALE, comment="села Бутакова Темниковскаго уѣзда"),
              comment="Яндексъ.Архивъ 57-3-79, сканъ 613; на полѣ помѣта «1899 г. 16 февр.» (выдача выписи)"),
    ),
    reviewed=False,
)
