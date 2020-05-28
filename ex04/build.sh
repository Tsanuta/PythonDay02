# !/bin/bash

# demander a pip de mettre a jour / installer les modules setuptools et wheel pour la creation des packages
python -m pip install --user --upgrade setuptools wheel

# Creation du package present dans l'espace courant  grace au fichier setup.py et du module bdist_wheel
python setup.py sdist --formats=gztar
