# 🚀 QUICK START GUIDE

## ⚠️ Important: You need Node.js installed first!

### Step 1: Install Node.js
1. Go to https://nodejs.org/
2. Download **LTS version** (Long Term Support) 
3. Install it (includes npm automatically)
4. Restart your terminal/VS Code

**Verify installation:**
```bash
node --version
npm --version
```

---

## After Node.js is installed:

### Step 2: Setup Frontend (First Time Only)

Open terminal in `d:\Simple_LLM\frontend`

```bash
npm install
```

This installs:
- React, Next.js, TypeScript
- Tailwind CSS dependencies
- All type definitions

⏱️ Takes 2-5 minutes (one-time)

---

### Step 3: Setup Backend (First Time Only)

Open terminal in `d:\Simple_LLM\backend`

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

⏱️ Takes 1-2 minutes (one-time)

---

### Step 4: Run the App

**Terminal 1 - Backend (from `d:\Simple_LLM\backend`):**
```bash
venv\Scripts\activate
python app.py
```

**Terminal 2 - Frontend (from `d:\Simple_LLM\frontend`):**
```bash
npm run dev
```

🎉 Open browser: http://localhost:3000

---

## What the errors mean:

✗ "Cannot find module 'react'" → Need to run `npm install`
✗ "Cannot find name 'process'" → Need to run `npm install` (installs @types/node)
✗ "JSX element implicitly has type 'any'" → Need to run `npm install`

**All these errors disappear after `npm install`**

---

## Troubleshooting

**"npm: The term is not recognized"**
→ Node.js not installed. Download from nodejs.org

**"python: The term is not recognized"**
→ Python not in PATH. Reinstall Python or add to PATH

**"Port 3000 already in use"**
→ Kill the process or use different port: `npm run dev -- -p 3001`

**"Port 8000 already in use"**
→ Change port in backend/app.py (last line)

---

## One-time command reference:

```bash
# Frontend
cd d:\Simple_LLM\frontend
npm install
npm run dev

# Backend (in new terminal)
cd d:\Simple_LLM\backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

After these one-time setups, you just run `npm run dev` and `python app.py` each time.

---

✅ Ready? Download Node.js and come back!
