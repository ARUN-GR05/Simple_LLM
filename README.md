# Simple_LLM 🚀

A simple transformer-based language model with a modern **FastAPI backend** and **Next.js frontend**, ready for deployment on Vercel.

## 📌 Overview

This project demonstrates:
- **Transformer Architecture**: Self-attention, embeddings, and tokenization
- **Backend API**: FastAPI with text generation endpoints
- **Frontend UI**: Modern React interface with Tailwind CSS
- **Production Ready**: Containerized and deployable to Vercel

## 📂 Project Structure

```
Simple_LLM/
├── backend/                 # Python FastAPI server
│   ├── app.py              # Main API (endpoints, model init)
│   ├── model.py            # Transformer model & tokenizer
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile          # Docker configuration
│   ├── .env.example        # Environment template
│   └── .gitignore
├── frontend/               # Next.js React app
│   ├── app/
│   │   ├── page.tsx       # Main UI (chat interface)
│   │   ├── layout.tsx     # App layout
│   │   └── globals.css    # Tailwind styles
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── .env.local.example # Frontend environment
│   ├── tailwind.config.js
│   └── .gitignore
├── simple_LLM.ipynb        # Original Jupyter notebook
├── DEPLOYMENT.md           # Deployment guide
├── vercel.json             # Vercel config
├── setup.bat               # Windows setup script
├── setup.sh                # Linux/Mac setup script
└── README.md
```

## 🚀 Quick Start (Local Development)

### Prerequisites
- **Python 3.11+** (for backend)
- **Node.js 18+** (for frontend)
- **npm** or **yarn**

### 1️⃣ Clone & Navigate
```bash
git clone https://github.com/ARUN-GR05/Simple_LLM.git
cd Simple_LLM
```

### 2️⃣ Setup Frontend
```bash
cd frontend
npm install
# Create .env.local
echo NEXT_PUBLIC_API_URL=http://localhost:8000 > .env.local
```

### 3️⃣ Setup Backend
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4️⃣ Run Everything

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
# Runs on http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
# Runs on http://localhost:3000
```

Open http://localhost:3000 in your browser! 🎉

## 🌐 Deploy to Vercel + Cloud Backend

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for step-by-step instructions.

**Quick Summary:**
1. Deploy backend to **Render** or **Railway** (free)
2. Deploy frontend to **Vercel** (free)
3. Connect them via environment variables

## 📊 API Endpoints

### `POST /generate`
Generate text based on a prompt.

**Request:**
```json
{
  "prompt": "The cat sat on",
  "max_length": 20,
  "temperature": 0.7
}
```

**Response:**
```json
{
  "prompt": "The cat sat on",
  "generated_text": "the mat and slept.",
  "full_text": "The cat sat on the mat and slept."
}
```

### `GET /health`
Check API status.

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 14, React 18, TypeScript, Tailwind CSS |
| **Backend** | FastAPI, Uvicorn |
| **ML** | PyTorch, NumPy |
| **Deployment** | Docker, Vercel, Render/Railway |

## 📚 What You'll Learn

- ✅ Transformer architecture (attention, embeddings)
- ✅ Building REST APIs with FastAPI
- ✅ Modern React with Next.js
- ✅ Full-stack deployment
- ✅ Environment variables & secrets
- ✅ CORS & API integration

## 🔧 Configuration

### Backend `.env`
```bash
FASTAPI_ENV=development
API_PORT=8000
API_HOST=0.0.0.0
```

### Frontend `.env.local`
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **CORS Error** | Already configured in backend (`CORSMiddleware`) |
| **Module not found** | Run `npm install` (frontend) or `pip install -r requirements.txt` (backend) |
| **Port already in use** | Kill process on port 3000/8000 or change ports |
| **Model fails to load** | Ensure `torch` is installed correctly |

## 🚀 Performance Tips

- **Temperature**: Lower (0.1) = deterministic, Higher (2.0) = creative
- **Max tokens**: 20-50 recommended for reasonable speed
- **CPU inference**: Suitable for hobby/demo projects
- **Production**: Consider GPU runtime or model quantization

## 📖 Further Reading

- [PyTorch Docs](https://pytorch.org/docs/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Next.js Guide](https://nextjs.org/docs)
- [Vercel Deployment](https://vercel.com/docs)

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add model improvements
- Enhance the UI
- Add more features
- Submit issues & PRs

## 📝 License

MIT License - feel free to use this for learning and projects!

## 👤 Author

**Arun GR**

---

⭐ **Found this helpful?** Please star the repository to support the project!

Made with ❤️ for the LLM community
