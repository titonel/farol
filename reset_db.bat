@echo off
echo ========================================
echo  RESETANDO BANCO DE DADOS AME CONTROL
echo ========================================
echo.
echo ATENCAO: Este script ira deletar o banco de dados existente!
echo Todos os dados serao perdidos.
echo.
pause

echo.
echo [1/3] Deletando banco de dados antigo...
if exist db.sqlite3 (
    del db.sqlite3
    echo OK - Banco de dados deletado
) else (
    echo INFO - Nenhum banco de dados encontrado
)

echo.
echo [2/3] Executando migracoes...
python manage.py migrate

echo.
echo [3/3] Pronto para criar superusuario!
echo Execute: python manage.py createsuperuser
echo.
pause
