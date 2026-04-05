import streamlit as st
import streamlit.components.v1 as components

# পেজ কনফিগারেশন
st.set_page_config(page_title="Thuluth Grunge Calligraphy", layout="centered")

# ইন্টারফেসের জন্য CSS
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; text-align: right; }
    .main { background-color: #0e1117; }
    h1 { color: #ffffff; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>Premium Grunge Calligraphy</h1>", unsafe_allow_html=True)

# আরবি টেক্সট ইনপুট
user_input = st.text_area("আরবি টেক্সট লিখুন:", placeholder="مثال: اَلْحَامِعَةُ الْغَفُوْرِيَّة...", height=120)

# ক্যালিগ্রাফি ও ডাউনলোড লজিক (HTML/CSS/JS)
html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Aref+Ruqaa:wght@700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body {{ 
            background-color: #0e1117; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
        }}
        
        #canvas-area {{
            /* ডার্ক ব্যাকগ্রাউন্ড, আপনার ছবির মতো */
            background: #000000;
            padding: 80px 100px;
            border-radius: 12px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border: 2px solid #222;
            width: auto;
            max-width: 95%;
            margin-top: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}

        .grunge-text {{
            /* 'Aref Ruqaa' ফন্ট Grunge ক্যালিগ্রাফির জন্য সেরা */
            font-family: 'Aref Ruqaa', serif;
            font-size: 110px;
            color: #FFFFFF;
            line-height: 1.3;
            text-align: center;
            letter-spacing: -2px;
            margin: 0;
            
            /* -- Grunge / Texture এফেক্ট -- */
            /* এটিই হলো আপনার কাঙ্ক্ষিত "খসখসে" লুক দেওয়ার মূল CSS */
            background-image: url('https://raw.githubusercontent.com/Anwar-Bin-Amin/arabic-thuluth-generator/main/texture_mask.png'); /* একটি টেক্সচার ইমেজ ব্যবহার করা হয়েছে */
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent; /* মূল রং transparent হবে যাতে টেক্সচার দেখা যায় */
            -webkit-text-fill-color: transparent;
            
            /* একটি হালকা শ্যাডো ৩D এফেক্ট দেওয়ার জন্য */
            text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.1);
        }}

        .download-btn {{
            margin-top: 30px;
            margin-bottom: 50px;
            padding: 15px 35px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }}
        .download-btn:hover {{ background-color: #45a049; }}
    </style>
</head>
<body>

    <div id="canvas-area">
        <div class="grunge-text">{user_input}</div>
    </div>

    <button class="download-btn" onclick="downloadCalligraphy()">HD ডাউনলোড করুন (Photo)</button>

    <script>
        function downloadCalligraphy() {{
            const area = document.getElementById('canvas-area');
            html2canvas(area, {{ 
                scale: 3, // হাই কোয়ালিটির জন্য
                backgroundColor: "#000000" 
            }}).then(canvas => {{
                let link = document.createElement('a');
                link.download = 'thuluth_grunge_calligraphy.png';
                link.href = canvas.toDataURL("image/png");
                link.click();
            }});
        }}
    </script>
</body>
</html>
"""

# জেনারেট বাটন
if st.button("ক্যালিগ্রাফি ডিজাইন দেখুন"):
    if user_input:
        components.html(html_template, height=650, scrolling=True)
    else:
        st.error("দয়া করে আগে কিছু লিখুন!")

st.markdown("---")
st.info("💡 **টিপস:** হুবহু আপনার দেওয়া ছবির মতো রেজাল্ট পেতে হলে টাইপ করার সময় হরকত বা চিহ্ন (যের, জবর, পেশ) ব্যবহার করুন। 'Aref Ruqaa' ফন্টটি Grunge ক্যালিগ্রাফির জন্য এই চিহ্নগুলোকে পেলেই কেবল পূর্ণাঙ্গ রূপ দেয়।")
