# 📝 STEP-BY-STEP DEPLOYMENT GUIDE

## PART 1: Deploy Backend (5 minutes)

### Step 1.1: Choose where to host backend
Pick ONE:
- **Render** (easiest, free) → https://render.com
- **Railway** (also free) → https://railway.app

### Step 1.2: Deploy on Render (I recommend this)

1. Go to **https://render.com**
2. Click **"New"** button (top right)
3. Select **"Web Service"**
4. Click **"Connect GitHub"**
5. Find and select your **"Simple_LLM"** repo
6. Fill in the form:
   ```
   Name: simple-llm-api
   Root Directory: backend
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```
7. Click **"Create Web Service"**
8. ⏱️ Wait 3-5 minutes for it to build
9. **Copy the URL** (looks like: https://simple-llm-api.onrender.com)
   - You'll see it on the page like "https://simple-llm-api.onrender.com"

✅ **Backend is now live!**

---

## PART 2: Deploy Frontend (5 minutes)

### Step 2.1: Go to Vercel

1. Go to **https://vercel.com**
2. Click **"Sign Up"** (or log in if you have account)
3. Choose **"Continue with GitHub"**
4. Click **"Authorize Vercel"**

### Step 2.2: Create new project

1. Click **"Add New"** button
2. Select **"Project"**
3. Find **"Simple_LLM"** repo → Click **"Import"**

### Step 2.3: Configure project

1. **Project Name**: simple-llm-frontend (or any name)

2. **Framework**: Select **"Next.js"**

3. **Root Directory**: Click the dropdown, select **"frontend"**

4. **Environment Variables** (IMPORTANT!):
   - Click **"Environment Variables"**
   - Add:
     ```
     Key: NEXT_PUBLIC_API_URL
     Value: https://simple-llm-api.onrender.com
     ```
     (Replace with YOUR Render URL from Part 1)

5. Click **"Deploy"**
6. ⏱️ Wait 2-3 minutes
7. When done, click the URL to visit your app!

✅ **Frontend is now live!**

---

## Testing Your App

1. Open: **https://your-app-name.vercel.app**
2. Type a prompt: "The cat"
3. Click "Generate Text"
4. ✅ If it works, you're done!

---

## If Something Goes Wrong

### "API Error" or "Connection Failed"
→ Copy-paste the Render URL correctly in Vercel environment variables

### "Port already in use" error on Render
→ Render auto-handles this, just wait and redeploy

### Can't find GitHub repo
→ Make sure you pushed all code with `git push`

---

## Summary

| Step | Platform | Time | What You Do |
|------|----------|------|-----------|
| 1 | Render | 5 min | Deploy backend, copy URL |
| 2 | Vercel | 5 min | Deploy frontend, paste backend URL |
| 3 | Browser | 1 min | Test at your-app.vercel.app |

---

## Commands Quick Reference

```bash
# Check if code is pushed
cd d:\Simple_LLM
git log --oneline -3

# If not pushed:
git add .
git commit -m "Deploy"
git push
```

---

## Video Alternative

If you prefer video guides:
- Render: Search "Render deploy Python API"
- Vercel: Search "Vercel deploy Next.js"

---

## Questions?

If you get stuck on any step, tell me:
- Which platform (Render/Railway/Vercel)?
- What error do you see?
- Which step are you on?

I'll help! 🚀
