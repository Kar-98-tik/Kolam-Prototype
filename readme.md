# 🎨 AI-Powered Kolam Generator  

An interactive **Streamlit web app** that generates traditional **Indian Kolam designs** using **Google’s Gemini Generative AI**.  
Users provide design parameters, and the AI generates **step-by-step instructions**, visualized in real time.  

---

## 🛠 Technologies Used  
- **[Streamlit](https://streamlit.io/):** Interactive web UI  
- **Google Gemini (Generative AI):** Core AI model to generate Kolam instructions in JSON  
- **Matplotlib:** Incremental drawing & visualization of Kolam  
- **python-dotenv:** Secure storage & loading of API keys  
- **Google Generative AI Python SDK:** Interface with Gemini API  

---

## 🌀 How the Kolam Generation Works  
Users provide input parameters such as:  
- Festival Type  
- Motif  
- Symmetry  
- Complexity  
- Grid Size  

👉 These parameters are used to craft a **prompt** for the Gemini model, which returns JSON with:  
- 📍 Dot coordinates  
- 🔗 Curves connecting dots  
- 🖌 Motif placements  
- ♻️ Symmetry types  

The app **incrementally draws the Kolam**:  
1. **Dots** → Displayed as points  
2. **Curves** → Connecting dots  
3. **Motifs** → Placed at specified positions  

---

## ⚙️ Integration and Configuration of Gemini Model  
- Uses **`google.generativeai` SDK**  
- API key securely loaded from `.env`  
- Model: **`gemini-2.5-flash`**  
- Natural language prompt → JSON response  
- JSON is parsed & rendered with **error handling** for malformed output  

---

## ⏳ Incremental Rendering  
To make the creation **engaging & dynamic**:  
- ⌛ Time delays added between drawing steps  
- 🔄 Streamlit **placeholders** update canvas dynamically  
- 🎥 Users watch the **Kolam being drawn step-by-step** instead of instantly  

---

## 🛡 Error Handling  
- ❌ If JSON parsing fails → Show error message + raw response  
- ⏹ Stops execution to prevent crashes  
- ⚡ Provides **immediate feedback** if AI output is malformed  

---

## 🚀 Deployment  

### 🔹 Local Deployment  
```bash
# Install dependencies
pip install -r requirements.txt  

# Store API key in .env file

# Run locally
streamlit run app.py
