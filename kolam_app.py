import streamlit as st
import google.generativeai as genai
import matplotlib.pyplot as plt
import json
import time
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# -------------------------------
# Configure Gemini
# -------------------------------
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🎨 AI-Powered Kolam Generator")

festival = st.selectbox("Festival", ["Pongal", "Diwali", "Daily", "Unknown"])
motif = st.selectbox("Motif", ["Lotus", "Peacock", "Star", "Abstract"])
symmetry = st.selectbox("Symmetry", ["Radial", "Rotational", "Reflectional"])
complexity = st.selectbox("Complexity", ["Simple", "Medium", "Complex"])
grid_size = st.slider("Grid Size", 3, 15, 7)

if st.button("Generate Kolam"):
    # -------------------------------
    # Prompt Gemini
    # -------------------------------
    prompt = f"""
    You are a Kolam design master. Based on these options:
    Festival: {festival}, Motif: {motif}, Symmetry: {symmetry}, Complexity: {complexity}, Grid Size: {grid_size}
    Generate drawing instructions in JSON format with fields:
    - dots: list of [x,y] integer positions
    - curves: list of curves (each curve = list of [x,y] points)
    - motifs: list of objects {{ "type": motif_name, "pos": [x,y] }}
    - symmetry: symmetry type
    Always include pos for motifs.
    """
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )

    try:
        instructions = json.loads(response.text)
    except Exception as e:
        st.error(f"Error parsing Gemini response: {e}")
        st.text(response.text)
        st.stop()

    # -------------------------------
    # Drawing Flow
    # -------------------------------
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    ax.axis("off")

    # Sequential drawing (single canvas)
    placeholder = st.empty()

    # Step 1: Draw dots
    for dot in instructions.get("dots", []):
        ax.plot(dot[0], dot[1], "ko")
        placeholder.pyplot(fig)
        time.sleep(0.2)

    # Step 2: Draw curves
    for curve in instructions.get("curves", []):
        if len(curve) >= 2:
            x, y = zip(*curve)
            ax.plot(x, y, "b-")
            placeholder.pyplot(fig)
            time.sleep(0.5)

    # Step 3: Place motifs
    for motif in instructions.get("motifs", []):
        pos = motif.get("pos", [grid_size // 2, grid_size // 2])
        mtype = motif.get("type", "").lower()
        symbol = "🌸" if "lotus" in mtype else "🦚" if "peacock" in mtype else "⭐"
        ax.text(pos[0], pos[1], symbol, fontsize=20, ha='center')
        placeholder.pyplot(fig)
        time.sleep(0.5)

    st.success(f"✅ {instructions.get('symmetry', 'Unknown')} symmetry Kolam generated!")
