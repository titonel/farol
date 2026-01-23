#!/bin/bash

echo "========================================"
echo "  RESETANDO BANCO DE DADOS AME CONTROL"
echo "========================================"
echo ""
echo "ATENCAO: Este script ira deletar o banco de dados existente!"
echo "Todos os dados serao perdidos."
echo ""
read -p "Pressione ENTER para continuar ou Ctrl+C para cancelar..."

echo ""
echo "[1/3] Deletando banco de dados antigo..."
if [ -f db.sqlite3 ]; then
    rm db.sqlite3
    echo "OK - Banco de dados deletado"
else
    echo "INFO - Nenhum banco de dados encontrado"
fi

echo ""
echo "[2/3] Executando migracoes..."
python manage.py migrate

echo ""
echo "[3/3] Pronto para criar superusuario!"
echo "Execute: python manage.py createsuperuser"
echo ""
