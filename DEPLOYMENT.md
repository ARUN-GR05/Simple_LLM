# 🚀 Simple LLM - Deployed!

A simple transformer-based language model deployed on Vercel.

## 📁 Project Structure

```
Simple_LLM/
├── backend/              # Python FastAPI server
│   ├── app.py           # API endpoints
│   ├── model.py         # LLM model & tokenizer
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile       # For local Docker testing
├── frontend/            # Next.js React app
│   ├── app/
│   │   ├── page.tsx     # Main UI
│   │   ├── layout.tsx   # Layout
│   │   └── globals.css  # Tailwind styles
│   └── package.json     # Node dependencies
├── vercel.json          # Deployment config
└── simple_LLM.ipynb    # Original notebook
```

## 🛠️ Setup Instructions

### 1. **Install Dependencies**

**Frontend:**
```bash
cd frontend
npm install
```

**Backend (optional - for local testing):**
```bash
cd backend
pip install -r requirements.txt
```

### 2. **Environment Variables**

Create `frontend/.env.local`:
```
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

For local development:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. **Run Locally**

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

## 📤 Deploy to Vercel

### **Step 1: Create Backend (Flask/FastAPI on Render/Railway)**

Choose one platform:

**Option A: Deploy on Render (FREE)**
1. Go to [render.com](https://render.com)
2. Click "New" → "Web Service"
3. Connect your GitHub repo
4. Set build command: `cd backend && pip install -r requirements.txt`
5. Set start command: `cd backend && python app.py`
6. Deploy and copy the URL

**Option B: Deploy on Railway (FREE with card)**
1. Go to [railway.app](https://railway.app)
2. Create new project → Deploy from GitHub
3. Select the backend folder
4. Set PORT to 8000
5. Deploy

### **Step 2: Deploy Frontend on Vercel**

1. Go to [vercel.com](https://vercel.com)
2. Click "Add New" → "Project"
3. Import your GitHub repo
4. **Framework: Next.js**
5. **Root Directory: frontend**
6. Add Environment Variable:
   - Key: `NEXT_PUBLIC_API_URL`
   - Value: `https://your-backend.onrender.com` (or your backend URL)
7. Click "Deploy"

## 🔌 API Endpoints

- `GET /` - Health check
- `GET /health` - Status
- `POST /generate` - Generate text
  ```json
  {
    "prompt": "The cat",
    "max_length": 20,
    "temperature": 0.7
  }
  ```

## 🎨 Features

- ✅ Real-time text generation
- ✅ Adjustable temperature (randomness)
- ✅ Max length control
- ✅ Beautiful UI with Tailwind CSS
- ✅ Responsive design
- ✅ Error handling

## 📋 Required Dependencies

**Frontend:**
- Next.js 14
- React 18
- Tailwind CSS
- Axios

**Backend:**
- FastAPI
- PyTorch
- Pydantic
- Uvicorn

## 🌐 Live Demo

Frontend: `https://your-app.vercel.app`
Backend API: `https://your-backend.onrender.com`

## 📝 Notes

- The model runs on CPU (suitable for low-traffic apps)
- For production: Consider using GPU runtime or model quantization
- Temperature: 0.1 (deterministic) → 2.0 (creative)
- Max length: 5-50 tokens recommended

## 🐛 Troubleshooting

**CORS Error?**
→ Already handled in `backend/app.py` with `CORSMiddleware`

**Connection refused?**
→ Check `NEXT_PUBLIC_API_URL` in `.env.local`

**Model not found?**
→ Backend initializes model on startup automatically

## 📚 Learn More

- [PyTorch Docs](https://pytorch.org)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Next.js Docs](https://nextjs.org)
- [Vercel Deployment](https://vercel.com/docs)

---

**Ready to deploy?** Push to GitHub and follow the deployment steps above! 🎉
