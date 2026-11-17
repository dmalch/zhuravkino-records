from verso.ru.dsl import Gender, Month, birth, birth_month, birth_records, person
from verso.ru.dsl.statuses import KAZENNYJ_PEASANT_MALE, KAZENNYJ_PEASANT_WIFE, PEASANT_GIRL, PEASANT_MALE

# Журавкинцы въ книгѣ чужого прихода 1891 г. — ЦГАРМ 57-4-137 (сводная книга Темниковскаго уѣзда, разделъ
# «Стандрово, Покровская церковь (1891)»), найдено по OCR Яндексъ.Архива, прочитано по скану 07.11.2026;
# reviewed=False.

other_births_1891_standrovo = birth_records(
    "ЦГАРМ", "57", "4", "137", "Стандрово", "Покровская",
    1891,
    *birth_month(Month.OCTOBER,
        birth(75, Gender.MALE, 6, 7,
              child=person("Сергій"),
              father=person("Сергій", "Захаровъ", last_name_orig="Бирлинъ", status=KAZENNYJ_PEASANT_MALE, residence="Журавкино"),
              mother=person("Домна", "Алексеева", status=KAZENNYJ_PEASANT_WIFE),
              god_parent1=person("Димитрій", "Алексеевъ", status=PEASANT_MALE, residence="Стандрово"),
              god_parent2=person("Евдокія", "Моисеева", status=PEASANT_GIRL, residence="Стандрово"),
              comment="Яндексъ.Архивъ 57-4-137, сканъ 617; на полѣ помѣта о выдачѣ выписи «3 Января 1912 г.»"),
    ),
    reviewed=False,
)
