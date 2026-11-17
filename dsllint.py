#!/usr/bin/env python3
"""Вход линтера DSL для плагинов VS Code и IntelliJ: они ищут файл с этим именем вверх по каталогам."""
import sys

from verso.ru.linters.dsllint import main

sys.exit(main())
