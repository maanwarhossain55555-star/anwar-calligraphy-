import streamlit as st
import google.generativeai as genai

# অ্যাপের কনফিগারেশন
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# CSS দিয়ে সুন্দর ডিজাইন তৈরি (সংশোধিত)
st.markdown("""
    <style>
    .arabic-font { 
        font-size: 40px !important; 
        direction: rtl; 
        text-align: center; 
        font-family: 'Amiri', serif; 
        background-color: #f0f2f6; 
        padding: 20px; 
        border-radius: 15px; 
        border: 2px solid #2e7d32; 
        margin-bottom: 20px;
    }
    .tarkib-container { 
        border: 2px dashed #1b5e20; 
        padding: 20px; 
        border-radius: 10px; 
        background-color: #ffffff; 
    }
    .stButton>button {
        width: 100%;
        background-color: #2e7d32;
        color: white;
        height: 3em;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI Powered)")
st.write("আপনার যেকোনো আরবি বাক্য লিখুন। এটি বড় বা কঠিন হলেও AI এর মাধ্যমে বিশ্লেষণ করা সম্ভব।")

# ইনপুট সেকশন
sentence = st.text_input("আরবি বাক্যটি লিখুন:", placeholder="مثلاً: إِنَّ مَعَ الْعُسْرِ يُسْرًا")

# API Key সেটআপ (এটি পরে সেটিংস থেকে যোগ করতে হবে)
api_key = st.secrets.get("GEMINI_API_KEY")

if st.button("পূর্ণাঙ্গ তারকিব দেখুন"):
    if sentence:
        st.markdown(f'<div class="arabic-font">{sentence}</div>', unsafe_allow_html=True)
        
        if not api_key:
            st.warning("⚠️ অ্যাপের সেটিংসে এখনো API Key সেট করা হয়নি।")
            st.info("আপনার হাতের লেখা নোটের মতো রেজাল্ট পেতে হলে 'Manage app' > 'Settings' > 'Secrets'-এ আপনার API Key বসাতে হবে।")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-pro')
                
                # AI কে ইনস্ট্রাকশন দেওয়া
                prompt = f"""
                Analyze the following Arabic sentence and provide a detailed 'Tarkib' (Syntactic Analysis) in Bengali.
                The output should follow this structure like a traditional Madrasa style:
                1. Break down every word (Ism, Fil, Harf).
                2. Define relationships (Mudaaf, Mudaaf Ilayh, Shart, Jaza, Fail, Maful, etc.).
                3. Final sentence type (Jumla Fi'liyah, Ismiyah, etc.).
                Sentence: {sentence}
                """
                
                with st.spinner('AI তারকib বিশ্লেষণ করছে...'):
                    response = model.generate_content(prompt)
                    st.markdown('<div class="tarkib-container">', unsafe_allow_html=True)
                    st.subheader("বিশ্লেষণ ফলাফল (বাংলায়):")
                    st.write(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"দুঃখিত, একটি সমস্যা হয়েছে: {e}")
    else:
        st.error("দয়া করে একটি আরবি বাক্য লিখুন।")
