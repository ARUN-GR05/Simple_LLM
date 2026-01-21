@echo off
REM Quick setup script for Simple LLM on Windows

echo 🚀 Setting up Simple LLM...

REM Frontend setup
echo 📦 Installing frontend dependencies...
cd frontend
call npm install
cd ..

echo.
echo ✅ Setup complete! Next steps:
echo 1. Frontend dependencies installed
echo 2. Setup backend virtual environment:
echo    python -m venv backend\venv
echo 3. Activate it:
echo    backend\venv\Scripts\activate
echo 4. Install backend dependencies:
echo    pip install -r backend\requirements.txt
echo 5. Create backend\.env file with API settings
echo 6. Run frontend: npm run dev (in frontend\)
echo 7. Run backend in another terminal: python app.py (in backend\)
echo.
echo 📚 For deployment, see DEPLOYMENT.md
