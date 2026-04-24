@echo off
chcp 65001 >nul
echo ========================================
echo   英语听写工具 - 自动打包脚本
echo ========================================
echo.

set PACK_DIR=英语听写工具_打包_%date:~0,4%%date:~5,2%%date:~8,2%

echo [1/5] 创建打包文件夹...
if exist "%PACK_DIR%" (
    echo 文件夹已存在，正在清空...
    rd /s /q "%PACK_DIR%"
)
mkdir "%PACK_DIR%"
echo ✓ 创建完成: %PACK_DIR%
echo.

echo [2/5] 复制核心文件...
copy app.py "%PACK_DIR%\" >nul
copy word_bank.py "%PACK_DIR%\" >nul
copy game_state.py "%PACK_DIR%\" >nul
copy requirements.txt "%PACK_DIR%\" >nul
copy README.md "%PACK_DIR%\" >nul
echo ✓ 核心文件复制完成
echo.

echo [3/5] 复制数据文件（如果存在）...
if exist game_save.json (
    copy game_save.json "%PACK_DIR%\" >nul
    echo ✓ game_save.json
)
if exist error_records.json (
    copy error_records.json "%PACK_DIR%\" >nul
    echo ✓ error_records.json
)
if exist review_list.json (
    copy review_list.json "%PACK_DIR%\" >nul
    echo ✓ review_list.json
)
echo.

echo [4/5] 复制文档文件...
copy 如何添加新词库.md "%PACK_DIR%\" >nul 2>nul
copy 数据清零功能说明.md "%PACK_DIR%\" >nul 2>nul
copy 项目迁移指南.md "%PACK_DIR%\" >nul 2>nul
copy UPDATE_词库统计功能.md "%PACK_DIR%\" >nul 2>nul
copy CHANGELOG.md "%PACK_DIR%\" >nul 2>nul
copy EBBINGHAUS_FEATURE.md "%PACK_DIR%\" >nul 2>nul
copy UPDATE_V2.2.md "%PACK_DIR%\" >nul 2>nul
echo ✓ 文档文件复制完成
echo.

echo [5/5] 创建启动脚本...
(
echo @echo off
echo chcp 65001 ^>nul
echo echo ========================================
echo echo   英语听写工具 - 启动中...
echo echo ========================================
echo echo.
echo echo 正在启动服务，请稍候...
echo python app.py
) > "%PACK_DIR%\启动.bat"
echo ✓ 启动脚本创建完成
echo.

echo ========================================
echo   打包完成！
echo ========================================
echo.
echo 📁 打包文件夹: %PACK_DIR%
echo 📦 包含文件:
dir /b "%PACK_DIR%"
echo.
echo ========================================
echo   下一步操作：
echo ========================================
echo.
echo 1. 将 "%PACK_DIR%" 文件夹复制到 U 盘或压缩成 ZIP
echo 2. 在新电脑上解压到任意位置（如 D:\英语听写工具）
echo 3. 安装 Python 3.8+ （确保勾选 Add to PATH）
echo 4. 打开 CMD，进入解压目录
echo 5. 运行：pip install -r requirements.txt
echo 6. 双击 "启动.bat" 或运行：python app.py
echo 7. 浏览器访问：http://localhost:7860
echo.
echo 详细说明请查看：项目迁移指南.md
echo.
pause
