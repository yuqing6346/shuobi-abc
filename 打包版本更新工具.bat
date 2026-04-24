@echo off
chcp 65001 >nul
echo ========================================
echo   打包版本更新工具
echo   保留学习数据，仅更新代码文件
echo ========================================
echo.

:: 检查是否存在新代码文件
if not exist app.py.new (
    echo [提示] 使用说明：
    echo.
    echo 1. 从GitHub下载最新代码文件到当前目录
    echo    - 下载并重命名为: app.py.new
    echo    - 下载并重命名为: word_bank.py.new
    echo    - 下载并重命名为: game_state.py.new
    echo.
    echo 2. 或者，将新代码文件夹路径拖到窗口按回车
    echo.
    set /p SOURCE_DIR=请输入新代码所在文件夹路径（留空取消）: 
    if "!SOURCE_DIR!"=="" (
        echo 已取消
        pause
        exit /b 0
    )
) else (
    set SOURCE_DIR=.
)

:: 去除引号
set SOURCE_DIR=%SOURCE_DIR:"=%

:: 检查源目录
if not exist "%SOURCE_DIR%\app.py" (
    echo [错误] 在 %SOURCE_DIR% 中未找到 app.py
    pause
    exit /b 1
)

echo.
echo 📂 源代码目录: %SOURCE_DIR%
echo 📂 当前目录: %CD%
echo.
echo 即将更新以下文件：
echo   - app.py
echo   - word_bank.py
echo   - game_state.py
echo   - requirements.txt
echo.
echo 📦 以下数据文件将保留（不会被覆盖）：
echo   - game_save.json
echo   - review_list.json
echo   - error_records.json
echo.

set /p CONFIRM=确认更新？(Y/N): 
if /i not "%CONFIRM%"=="Y" (
    echo 已取消
    pause
    exit /b 0
)

echo.
echo [1/3] 备份当前代码...
set BACKUP_DIR=_code_backup_%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set BACKUP_DIR=%BACKUP_DIR: =0%
mkdir "%BACKUP_DIR%" 2>nul

copy app.py "%BACKUP_DIR%\" >nul 2>nul && echo ✓ 已备份 app.py
copy word_bank.py "%BACKUP_DIR%\" >nul 2>nul && echo ✓ 已备份 word_bank.py
copy game_state.py "%BACKUP_DIR%\" >nul 2>nul && echo ✓ 已备份 game_state.py
echo.

echo [2/3] 更新代码文件...
copy /y "%SOURCE_DIR%\app.py" . >nul && echo ✓ 已更新 app.py || echo ✗ 更新 app.py 失败
copy /y "%SOURCE_DIR%\word_bank.py" . >nul && echo ✓ 已更新 word_bank.py || echo ✗ 更新 word_bank.py 失败
copy /y "%SOURCE_DIR%\game_state.py" . >nul && echo ✓ 已更新 game_state.py || echo ✗ 更新 game_state.py 失败
copy /y "%SOURCE_DIR%\requirements.txt" . >nul 2>nul && echo ✓ 已更新 requirements.txt
echo.

echo [3/3] 检查学习数据...
if exist game_save.json (
    echo ✓ game_save.json 保留
) else (
    echo ℹ game_save.json 不存在
)
if exist review_list.json (
    echo ✓ review_list.json 保留
) else (
    echo ℹ review_list.json 不存在
)
if exist error_records.json (
    echo ✓ error_records.json 保留
) else (
    echo ℹ error_records.json 不存在
)
echo.

echo ========================================
echo ✓ 更新完成！
echo ========================================
echo.
echo 旧代码备份在: %BACKUP_DIR%
echo 学习数据已保留，可以直接运行！
echo.
echo 下一步：
echo   1. 运行: pip install -r requirements.txt （更新依赖）
echo   2. 双击"启动.bat"运行程序
echo.
pause
