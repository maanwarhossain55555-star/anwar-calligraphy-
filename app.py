<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arabic Calligraphy Generator</title>
    <link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Aref+Ruqaa:wght@700&family=Reem+Kufi&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 50px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
            width: 80%;
        }
        textarea {
            width: 100%;
            height: 100px;
            font-size: 20px;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 8px;
            border: 1px solid #ccc;
            text-align: right;
        }
        button {
            padding: 12px 30px;
            font-size: 18px;
            background-color: #2c3e50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background-color: #34495e;
        }
        #output-area {
            margin-top: 40px;
            padding: 20px;
            min-height: 150px;
            border: 2px dashed #ddd;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #fff;
        }
        .calligraphy-text {
            /* আপনার ছবির মতো ঘন স্টাইল পাওয়ার জন্য ফন্ট */
            font-family: 'Amiri Quran', serif; 
            font-size: 80px;
            line-height: 1.6;
            color: #000;
            word-spacing: 15px;
            /* ক্যালিগ্রাফিক লুকের জন্য টেক্সট শ্যাডো ব্যবহার করা যায় */
            text-shadow: 1px 1px 0px #eee;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>আরবি ক্যালিগ্রাফি জেনারেটর</h2>
    <textarea id="userInput" placeholder="এখানে আরবি লিখুন..."></textarea>
    <br>
    <button onclick="generateCalligraphy()">ক্যালিগ্রাফি তৈরি করুন</button>

    <div id="output-area">
        <div id="result" class="calligraphy-text"></div>
    </div>
</div>

<script>
    function generateCalligraphy() {
        const input = document.getElementById('userInput').value;
        const resultDiv = document.getElementById('result');
        
        if(input.trim() === "") {
            alert("অনুগ্রহ করে কিছু লিখুন");
            return;
        }
        
        // ইনপুটটি রেজাল্ট বক্সে দেখানো
        resultDiv.innerText = input;
    }
</script>

</body>
</html>
