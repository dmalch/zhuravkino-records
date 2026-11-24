# Цели репозитория села. Нужен Python 3.14 и (лучше) uv: https://docs.astral.sh/uv/
PY := .venv/bin/python
VERSO := $(PY) -m verso.core.cli
VILLAGE := Журавкино

.PHONY: help bootstrap lint records check site

help:
	@echo "make bootstrap  — .venv и verso"
	@echo "make lint       — линтер DSL (verso dsllint)"
	@echo "make records    — записи в JSON (verso export-records) → records/"
	@echo "make check      — lint и records"
	@echo "make site       — сайт села (verso site) → _site/"

bootstrap:
	@if [ -x $(PY) ]; then echo "==> .venv уже есть"; \
	elif command -v uv >/dev/null 2>&1; then uv venv --python 3.14 .venv; \
	else python3 -m venv .venv; fi
	@if command -v uv >/dev/null 2>&1; then uv pip install --python $(PY) -e .; \
	else $(PY) -m pip install -e .; fi

lint:
	$(VERSO) dsllint --baseline dsllint_baseline.tsv --villages

records:
	$(VERSO) export-records --village "$(VILLAGE)" --strict

check: lint records

site:
	rm -rf _site
	$(VERSO) site --village "$(VILLAGE)" --out _site --strict \
		--title="Журавкино и Авдалово" \
		--repo-url "https://github.com/dmalch/zhuravkino-records" --site-url "https://dmalch.github.io/zhuravkino-records/" \
		--license "CC BY 4.0" --license-url "https://creativecommons.org/licenses/by/4.0/" \
		--revision "$$(git rev-parse --short HEAD 2>/dev/null || echo local)"
