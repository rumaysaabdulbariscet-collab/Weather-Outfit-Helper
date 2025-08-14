import streamlit as st
from datetime import datetime

# ---------------------
# APP CONFIG
# ---------------------
st.set_page_config(page_title="Outfit Helper", page_icon="👗", layout="centered")

st.title("👗 Outfit Helper")
st.write("Get outfit suggestions based on the weather!")

# ---------------------
# WEATHER + OUTFIT LOGIC
# ---------------------
def outfit_tip(temp_c):
    if temp_c < 10:
        return "🧥 It's cold! Wear a coat, scarf, and warm boots."
    elif 10 <= temp_c < 20:
        return "🧶 Slightly chilly — try a sweater or light jacket."
    elif 20 <= temp_c < 30:
        return "👕 Warm weather — t-shirt, jeans, or a summer dress."
    else:
        return "🩳 It's hot! Go for shorts, tank tops, and stay hydrated."

# ---------------------
# USER INPUT
# ---------------------
temp = st.number_input("Enter the current temperature (°C):", value=25)
st.write("**Current temperature:**", temp, "°C")

if st.button("Get Outfit Suggestion"):
    st.success(outfit_tip(temp))

# ---------------------
# OPTIONAL IMAGE UPLOAD
# ---------------------
st.subheader("📸 Upload Your Outfit Pictures")
uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=["jpg", "png", "jpeg"])

if uploaded_files:
    for file in uploaded_files:
        st.image(file, caption=file.name, use_column_width=True)

# ---------------------
# FOOTER
# ---------------------
st.write("---")
st.caption(f"Outfit Helper App • {datetime.now().year}")

