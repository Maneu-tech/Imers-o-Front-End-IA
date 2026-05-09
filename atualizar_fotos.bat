@echo off
REM Script para atualizar as fotos da apresentação
REM Clique duas vezes para executar

echo.
echo ============================================================
echo   Atualizando fotos da apresentacao...
echo ============================================================
echo.

cd /d "c:\Users\mateu\Downloads\fotos maezinha"

REM Tentar com Python
python update_fotos.py
if %errorlevel% equ 0 goto sucesso

REM Se Python falhou, tentar com py
py update_fotos.py
if %errorlevel% equ 0 goto sucesso

REM Se py falhou, tentar com Node.js
node update.js
if %errorlevel% equ 0 goto sucesso

REM Se nada funcionou, mostrar erro
echo.
echo ============================================================
echo   ERRO: Nao consegui executar os scripts!
echo ============================================================
echo.
echo   Certificar-se de que um dos seguintes esta instalado:
echo   - Python (python.org)
echo   - Node.js (nodejs.org)
echo.
echo   Ou execute manualmente no terminal:
echo   python update_fotos.py
echo.
pause
exit /b 1

:sucesso
echo.
echo ============================================================
echo   SUCESSO! Fotos atualizadas!
echo ============================================================
echo.
echo   Abra o arquivo index.html no navegador para ver
echo   a apresentacao com suas fotos.
echo.
pause
exit /b 0
