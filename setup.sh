#!/bin/bash
# Quick setup script for Simple LLM

echo "🚀 Setting up Simple LLM..."

# Frontend setup
echo "📦 Installing frontend dependencies..."
cd frontend
npm install
cd ..

# Backend setup (optional)
echo "🐍 Backend setup (manual):"
echo "1. Create Python virtual environment:"
echo "   python -m venv backend/venv"
echo "2. Activate it:"
echo "   On Windows: backend\\venv\\Scripts\\activate"
echo "   On macOS/Linux: source backend/venv/bin/activate"
echo "3. Install dependencies:"
echo "   pip install -r backend/requirements.txt"

echo ""
echo "✅ Setup complete! Next steps:"
echo "1. Install frontend: npm install (in frontend/)"
echo "2. Copy backend/.env.example to backend/.env"
echo "3. Copy frontend/.env.local.example to frontend/.env.local"
echo "4. Run: npm run dev (in frontend/)"
echo "5. In another terminal, run backend: python app.py"
