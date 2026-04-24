@echo off
chcp 65001 >nul
echo ================================
echo    代码自动更新工具
echo ================================
echo.

:: 检查是否在Git仓库中
git rev-parse --git-dir >nul 2>&1
if errorlevel 1 (
    echo [错误] 当前目录不是Git仓库！
    echo 请先按照README中的步骤初始化Git仓库
    pause
    exit /b 1
)

:: 检查网络连接
echo [1/4] 检查网络连接...
ping github.com -n 1 -w 1000 >nul 2>&1
if errorlevel 1 (
    echo [警告] 无法连接到GitHub，请检查网络
    pause
    exit /b 1
)
echo ✓ 网络正常

:: 获取当前分支
echo.
echo [2/4] 获取当前分支...
for /f "tokens=*" %%i in ('git branch --show-current') do set BRANCH=%%i
echo ✓ 当前分支: %BRANCH%

:: 暂存本地修改（如果有）
echo.
echo [3/4] 检查本地修改...
git diff --quiet
if errorlevel 1 (
    echo ! 检测到本地有未提交的修改
    echo ! 将自动暂存这些修改（不会丢失）
    git stash save "自动暂存 - %date% %time%"
    echo ✓ 已暂存本地修改
) else (
    echo ✓ 工作区干净
)

:: 拉取最新代码
echo.
echo [4/4] 拉取最新代码...
git pull origin %BRANCH%
if errorlevel 1 (
    echo [错误] 代码拉取失败！
    echo 可能原因：
    echo 1. 网络不稳定
    echo 2. 远程仓库配置错误
    echo 3. 存在冲突
    pause
    exit /b 1
)

echo.
echo ================================
echo ✓ 代码更新成功！
echo ================================
echo.
echo 提示：如果您之前有本地修改，它们已被暂存
echo 使用 'git stash pop' 可以恢复这些修改
echo.
pause
