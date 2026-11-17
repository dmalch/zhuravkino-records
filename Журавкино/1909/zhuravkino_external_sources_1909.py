from verso.ru.dsl import EventDate, Month, criminal_record, external_source_records, person
from verso.ru.dsl.statuses import PEASANT_MALE

# Судимость («Ведомости справок о судимости 1870–1927», familio.org /catalogs/vss/).
# Челомеев Никита Ильин — Боково-Майданская волость, Спасский уезд, Тамбовская губ.
# UNCERTAIN whether «с. Журовки» is our с. Журавкино (same волость, but the printed
# settlement name differs) — to be verified on reconciliation.
zhuravkino_external_sources_1909 = external_source_records(
    "Журавкино",
    criminal_record(
        person("Никита", "Ильинъ", "Челомѣевъ", status=PEASANT_MALE, residence="Журавкино"),
        age=17,  # → birth year derived: 1909 − 17 = 1892
        record_number=72493,
        date=EventDate(1909, Month.MARCH, 14),
        source_url="https://viewer.rsl.ru/ru/rsl01005469227?page=213",
        scan_file="scans/sudimost_nikita_chelomeev_1909.jpg",
        original_text=(
            "72493. ЧЕЛОМЕЕВ, НИКИТА ИЛЬИН. К. Спасск. у., Боково-Майданск. в., "
            "с. Журовки, 17 л.; — Тамбовск. О. С., 140 и 1 ч. 1647 У., тюр. 1 г. "
            "Исп. 14 Марта 909."
        ),
        bibliography=(
            "Ведомость справок о судимости / изд. М-ва юстиции. — СПб.: Тип. "
            "Правительствующего Сената, 1872–1929. (РСЛ: rsl01005469227, скан с. 213.)"
        ),
        comment=(
            "Преступление: кража (ч. 1 ст. 1647 Уложения о наказаниях — статья из "
            "раздела о краже; ст. 1644 определяет кражу как тайное похищение "
            "чужого движимого имущества без насилия). Ст. 140 — общие правила; "
            "вероятно, смягчение по несовершеннолетию (осуждённому 17 лет). "
            "Суд: Тамбовский окружной суд. "
            "Наказание: тюрьма 1 год. Исполнено 14 марта 1909 г. "
        ),
    ),
)
