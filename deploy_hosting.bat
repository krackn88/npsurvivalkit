@echo off
echo 🩺 NP Survival Toolkit - Free Hosting Setup
echo ===========================================
echo.
echo Choose your hosting option:
echo.
echo 1. GitHub Pages (Free, requires GitHub account)
echo 2. Netlify (Free, drag & drop deployment)
echo 3. Vercel (Free, easy deployment)
echo 4. Show all files ready for upload
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo 📁 GitHub Pages files ready in: github-pages\
    echo.
    echo Next steps:
    echo 1. Create GitHub repository: npsurvivalkit
    echo 2. Upload files from github-pages\ folder
    echo 3. Enable GitHub Pages in Settings ^> Pages
    echo 4. Your site: https://[YOUR_USERNAME].github.io/npsurvivalkit
    echo.
    explorer github-pages
)

if "%choice%"=="2" (
    echo.
    echo 🌐 Netlify Deployment:
    echo 1. Go to netlify.com
    echo 2. Sign up for free account
    echo 3. Drag github-pages\ folder to deploy area
    echo 4. Your site will be live instantly!
    echo.
    explorer github-pages
)

if "%choice%"=="3" (
    echo.
    echo ⚡ Vercel Deployment:
    echo 1. Go to vercel.com
    echo 2. Sign up for free account
    echo 3. Import from GitHub or drag & drop
    echo 4. Deploy in seconds!
    echo.
    explorer github-pages
)

if "%choice%"=="4" (
    echo.
    echo 📁 Files ready for upload:
    explorer github-pages
)

echo.
echo 🎯 Your NP Survival Toolkit is ready to go live!
echo 💰 Start earning affiliate commissions today!
echo.
pause
