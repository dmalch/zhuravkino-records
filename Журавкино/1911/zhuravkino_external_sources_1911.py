from verso.ru.dsl import EventDate, Month, criminal_record, external_source_records, person
from verso.ru.dsl.statuses import PEASANT_MALE

# Судимость («Ведомости справок о судимости 1870–1927», familio.org /catalogs/vss/).
# Булаев Егор Петров — с. Жеравкина, Майдановская волость, Спасский уезд,
# Тамбовская губ.
zhuravkino_external_sources_1911 = external_source_records(
    "Журавкино",
    criminal_record(
        person("Егоръ", "Петровъ", "Булаевъ", status=PEASANT_MALE, residence="Журавкино"),
        age=50,  # → birth year derived: 1911 − 50 = 1861
        record_number=92044,
        date=EventDate(1911, Month.FEBRUARY, 25),
        source_url="https://viewer.rsl.ru/ru/rsl01005491878?page=27",
        scan_file="scans/sudimost_egor_bulaev_1911.jpg",
        original_text=(
            "92044. БУЛАЕВ, ЕГОР ПЕТРОВ, 50 л. К. Тамбов. г., Спасск. у., "
            "Майдановск. в., с. Жеравкина; — З. Н. 4 уч. Шацк. у., 10 Февр. 911, "
            "170 М., тюр. 8 м. Исп. 25 Февр. 911."
        ),
        bibliography=(
            "Ведомость справок о судимости / изд. М-ва юстиции. — СПб.: Тип. "
            "Правительствующего Сената, 1872–1929. (РСЛ: rsl01005491878, скан с. 27.)"
        ),
        comment=(
            "Преступление: кража (ст. 170 Устава о наказаниях, налагаемых мировыми "
            "судьями, — кража при отягчающих обстоятельствах; ст. 169 того же "
            "Устава карала простую кражу имущества ценой до 300 руб. заключением "
            "на 3–6 месяцев). "
            "Суд: земский начальник 4-го участка Шацкого уезда (приговор 10 февраля 1911 г.). "
            "Наказание: тюрьма 8 месяцев. Исполнено 25 февраля 1911 г."
        ),
    ),
)
