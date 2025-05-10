
import streamlit as st
import pytesseract
from PIL import Image
import numpy as np
from collections import Counter

# Optional: Set path to tesseract if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def mock_generate_description(text):
    return f"{text} is a second-hand clothing item. It is in good condition and suitable for daily wear. Great for casual outfits."

def mock_price_analysis():
    prices = [12000, 15000, 11000, 13000, 10000, 9000, 15000, 14000, 16000, 10500]
    median_price = np.median(prices)
    recommended_price = round(median_price * 0.95)
    return {
        "Average Price": round(np.mean(prices)),
        "Median Price": round(median_price),
        "Most Common Price": Counter(prices).most_common(1)[0][0],
        "Price Range": (min(prices), max(prices)),
        "Recommended Selling Price": recommended_price
    }

st.title("Used Clothing Auto Description & Price Suggestion (English OCR)")

uploaded_file = st.file_uploader("Upload a clothing image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Recognizing text..."):
        extracted_text = pytesseract.image_to_string(image, lang="eng").strip()
        st.success("Extracted Text:")
        st.write(extracted_text)

    with st.spinner("Generating description..."):
        description = mock_generate_description(extracted_text)
        st.markdown("**Auto-generated Description:**")
        st.write(description)

    with st.spinner("Analyzing market price..."):
        prices = mock_price_analysis()
        st.markdown("**Suggested Pricing Info:**")
        st.write(prices)
