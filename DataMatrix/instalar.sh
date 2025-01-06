#!/bin/bash

# Actualizar la lista de paquetes
sudo apt-get update

sudo apt-get install -y libpq-dev python3-dev   # necesaria para psycopg

# para PyQt
sudo apt-get install -y libxcb-cursor0
sudo apt-get install libdmtx0b
sudo apt-get install -y libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-shape0 libxcb-xfixes0



SCRIPT_DIR=$(dirname "$0")

RUTA_RELATIVA="$SCRIPT_DIR"
VENV_DIR="$SCRIPT_DIR/venv"

source "$VENV_DIR/bin/activate"

# Confirmar que el entorno virtual está activado
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Entorno virtual activado en $VIRTUAL_ENV"
else
    echo "Fallo al activar el entorno virtual"
    exit 1
fi

pip install --upgrade pip
pip install -r "$SCRIPT_DIR/requirements.txt"
