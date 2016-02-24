#!/bin/bash
make gettext
sphinx-intl update -p _build/locale -l fr
