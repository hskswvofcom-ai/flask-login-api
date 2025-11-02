from flask import Flask, request, redirect

app = Flask(__name__)
comments = []

@app.route('/')
def index():
    return """<!DOCTYPE html><html lang="fa"><head><meta charset="UTF-8"><title>گروه هنری داش اسمال</title>
    <style>@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
    *{box-sizing:border-box;}body{margin:0;padding:0;font-family:'Vazirmatn',Tahoma,sans-serif;direction:rtl;
    background:linear-gradient(to bottom right,#fff0f5,#e1bee7);color:#4e342e;display:flex;flex-direction:column;
    justify-content:center;align-items:center;min-height:100vh;text-align:center;}h1{font-size:60px;color:#6a1b9a;
    margin-bottom:10px;text-shadow:2px 2px 5px #fff;}h2{font-size:28px;color:#4e342e;margin-top:5px;}
    .tagline{font-size:20px;color:#7b1fa2;margin-top:15px;font-style:italic;}
    .numbers{font-size:22px;margin:25px 0;background-color:#ffffffcc;padding:20px 30px;border-radius:12px;
    box-shadow:0 0 10px rgba(0,0,0,0.1);font-weight:bold;line-height:2;}
    .btn{margin:10px;padding:15px 30px;font-size:18px;background-color:#8e24aa;color:white;border:none;
    border-radius:10px;cursor:pointer;transition:background-color 0.3s ease;text-decoration:none;display:inline-block;}
    .btn:hover{background-color:#6a1b9a;}
    .instagram-links{margin-top:30px;font-size:18px;color:#5c6bc0;}
    .instagram-links a{color:#5c6bc0;text-decoration:none;margin:0 10px;font-weight:bold;}
    .instagram-links a:hover{text-decoration:underline;}
    footer{margin-top:40px;font-size:14px;color:#888;}
    </style></head><body>
    <h1>گروه هنری داش اسمال</h1><h2>داش اسمال و داش حیدر</h2>
    <div class="tagline">خلق لحظه‌های خاص با هنر ناب ایرانی، از دل تا قاب</div>
    <div class="numbers">📞 داش حیدر: 09018860133<br>📞 داش اسمال: 09151179499</div>
    <a class="btn" href="/comment">📝 ثبت نظر و انتقاد</a>
    <a class="btn" href="/comments">📃 نمایش نظرات کاربران</a>
    <a class="btn" href="tel:09151179499">📅 رزرو وقت هنری</a>
    <div class="instagram-links">📷 اینستاگرام: 
    <a href="https://instagram.com/dash_heydar_mashhad" target="_blank">داش حیدر</a> |
    <a href="https://instagram.com/dashsmal61" target="_blank">داش اسمال</a></div>
    <footer>© 2025 تمامی حقوق محفوظ است | طراحی با عشق توسط داش اسمال</footer></body></html>"""

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        text = request.form.get('text')
        comments.append({'email': email, 'name': name, 'text': text})
        return redirect('/comments')
    return """<html><body style="font-family:Tahoma;direction:rtl;text-align:center;background:#f3e5f5;padding:50px;">
    <h2 style="color:#6a1b9a;">📝 ثبت نظر و انتقاد</h2>
    <form method="post" style="background:#fff;padding:30px;border-radius:15px;max-width:400px;margin:auto;">
        <input type="email" name="email" placeholder="📧 ایمیل شما" required style="width:100%;padding:10px;margin:10px 0;">
        <input type="text" name="name" placeholder="👤 نام شما" required style="width:100%;padding:10px;margin:10px 0;">
        <textarea name="text" rows="5" placeholder="✍️ نظر یا انتقاد شما..." required style="width:100%;padding:10px;margin:10px 0;"></textarea>
        <button type="submit" style="padding:12px 25px;background:#8e24aa;color:white;border:none;border-radius:8px;">📨 ارسال نظر</button>
    </form></body></html>"""

@app.route('/comments')
def show_comments():
    html = """<html><body style="font-family:Tahoma;direction:rtl;text-align:center;background:#ede7f6;padding:50px;overflow-y:auto;max-height:100vh;">
    <h2 style="color:#6a1b9a;">📃 نظرات ثبت‌شده کاربران</h2>"""
    for c in comments:
        html += f"""<div style="background:#fff;padding:20px;margin:20px auto;border-radius:12px;max-width:600px;text-align:right;
        box-shadow:0 0 10px rgba(0,0,0,0.1);max-height:300px;overflow-y:auto;">
        <strong style="color:#6a1b9a;">{c['name']}</strong> ({c['email']})<br>{c['text']}</div>"""
    html += "</body></html>"
    return html