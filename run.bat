@echo off
REM === Move to extension folder ===
cd /d %~dp0

REM === Install dependencies if missing ===
if not exist node_modules (
    echo Installing dependencies...
    npm install
)

REM === Compile TypeScript ===
echo Compiling extension...
npm run compile

REM === Launch VSCode with extension debugging ===
echo Starting VSCode with extension...
code . --extensionDevelopmentPath=%cd%

pause
