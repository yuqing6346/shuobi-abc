@echo off
chcp 65001 >nul
echo ========================================
echo   智能更新脚本 - 保留数据更新代码
echo ========================================
echo.

:: 检查是否在Git仓库中
if not exist .git (
    echo [错误] 当前目录不是Git仓库！
    echo.
    echo 此脚本用于有Git仓库的开发版本。
    echo 对于打包版本，请使用"覆盖式更新.bat"
    pause
    exit /b 1
)

:: 备份数据文件
echo [1/4] 备份学习数据...
set BACKUP_DIR=_data_backup_%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set BACKUP_DIR=%BACKUP_DIR: =0%
mkdir "%BACKUP_DIR%" 2>nul

if exist game_save.json (
    copy game_save.json "%BACKUP_DIR%\" >nul
    echo ✓ 已备份 game_save.json
)
if exist review_list.json (
    copy review_list.json "%BACKUP_DIR%\" >nul
    echo ✓ 已备份 review_list.json
)
if exist error_records.json (
    copy error_records.json "%BACKUP_DIR%\" >nul
    echo ✓ 已备份 error_records.json
)
echo.

:: 检查网络
echo [2/4] 检查网络连接...
ping github.com -n 1 -w 1000 >nul 2>&1
if errorlevel 1 (
    echo [警告] 无法连接到GitHub
    pause
    exit /b 1
)
echo ✓ 网络正常
echo.

:: 获取当前分支
echo [3/4] 拉取最新代码...
for /f "tokens=*" %%i in ('git branch --show-current') do set BRANCH=%%i
echo 当前分支: %BRANCH%

:: 暂存本地修改
git diff --quiet
if errorlevel 1 (
    echo ! 检测到本地修改，自动暂存...
    git stash save "自动暂存 - %date% %time%"
)

:: 拉取代码
git pull origin %BRANCH%
if errorlevel 1 (
    echo [错误] 代码拉取失败！
    pause
    exit /b 1
)
echo ✓ 代码更新成功
echo.

:: 恢复数据文件
echo [4/4] 恢复学习数据...
if exist "%BACKUP_DIR%\game_save.json" (
    copy "%BACKUP_DIR%\game_save.json" . >nul
    echo ✓ 已恢复 game_save.json
)
if exist "%BACKUP_DIR%\review_list.json" (
    copy "%BACKUP_DIR%\review_list.json" . >nul
    echo ✓ 已恢复 review_list.json
)
if exist "%BACKUP_DIR%\error_records.json" (
    copy "%BACKUP_DIR%\error_records.json" . >nul
    echo ✓ 已恢复 error_records.json
)
echo.

echo ========================================
echo ✓ 更新完成！数据已保留
echo ========================================
echo.
echo 备份保存在: %BACKUP_DIR%
echo.
pause
