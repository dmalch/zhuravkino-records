from verso.ru.dsl import Gender, Month, death, death_month, death_records, person
from verso.ru.dsl.causes_of_death import CHILDBIRTH
from verso.ru.dsl.statuses import SOLDIER_WIFE

# Журавкинка въ книгѣ чужого прихода 1890 г. — ЦГАРМ 57-3-110 (сводная книга Темниковскаго уѣзда, разделъ
# «Стандрово (1890)»), найдено по OCR Яндексъ.Архива, прочитано по скану 07.11.2026; reviewed=False.

other_deaths_1890_standrovo = death_records(
    "ЦГАРМ", "57", "3", "110", "Стандрово", "Покровская",
    1890,
    *death_month(Month.AUGUST,
        death(59, Gender.FEMALE, 15, 17,
              deceased=person("Ефросинья", "Ѳеофанова", last_name_orig="Баранова", status=SOLDIER_WIFE, residence="Журавкино", comment="жена солдата Сергея Захарова Баранова"),
              age=40,
              cause_of_death=CHILDBIRTH,
              comment="Яндексъ.Архивъ 57-3-110, сканъ 154. Въ 1891 г. въ той же церкви крещенъ сынъ журавкинца "
                      "Сергія Захарова Бирлина и жены его Домны — можетъ быть, тотъ же вдовецъ (other_births_1891)"),
    ),
    reviewed=False,
)
