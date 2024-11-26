from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify
from flask_mail import Mail, Message
import imaplib
import email
from groq import Groq

client = Groq(api_key="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")





app = Flask(__name__)
app.secret_key = "your_secret_key"

app.config['MAIL_SERVER'] = 'imap.mail.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'iam@matveev.website'
app.config['MAIL_PASSWORD'] = 'Gep100/;'
mail = Mail(app)

messages = [
    {"from": "nikita@example.com", "body": "Привет, как дела?", "timestamp": "2024-11-25 14:00"},
    {"from": "user2@example.com", "body": "Тестовое сообщение", "timestamp": "2024-11-25 14:05"}
]
# Пример данных пользователей
users = {
    "admin": "admin",
    "user1": "mypassword"
}

@app.route('/gpt/message', methods=['POST'])
def gpt_message():
    # Получаем сообщение от клиента
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Запрос к GPT
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "ты бот помощьник для работников компании ООО Гедаэффект. Тебя Зовут GedaGPT. Гедаэффект - это инжинеринговая компани ,которая занимается автоматизацией производства."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        gpt_response = completion.choices[0].message.content
        return jsonify({'response': gpt_response.replace('\\n', '<br>')})
    
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

@app.route("/mail/messages", methods=["GET"])
def get_messages():
    # Возврат сообщений (в реальном проекте подключить IMAP для получения данных)
    return jsonify(messages)

@app.route("/mail/send", methods=["POST"])
def send_mail():
    data = request.json
    recipient = data.get("recipient")
    subject = data.get("subject", "Без темы")
    body = data.get("body")

    if not recipient or not body:
        return jsonify({"error": "Recipient and body are required"}), 400

    try:
        msg = Message(subject=subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
        msg.body = body
        mail.send(msg)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def is_authorized():
    return request.cookies.get("username") is not None

@app.route("/")
def home():
    if is_authorized():
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            response = make_response(redirect(url_for("dashboard")))
            response.set_cookie("username", username, max_age=60*60*24)
            return response
        else:
            flash("Неверное имя пользователя или пароль", "danger")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not is_authorized():
        return redirect(url_for("login"))
    
    username = request.cookies.get("username")
    return render_template("dashboard.html", username=username)

@app.route("/gpt")
def gpt():
    if not is_authorized():
        return redirect(url_for("login"))
    
    username = request.cookies.get("username")
    return render_template("gpt.html", username=username)

@app.route("/mail", methods=["GET"])
def mail_page():
    if not is_authorized():
        return redirect(url_for("login"))
    username = request.cookies.get("username")
    return render_template("chats.html", username=username)

@app.route("/logout")
def logout():
    if is_authorized():
        response = make_response(redirect(url_for("home")))
        response.delete_cookie("username")
        return response
    else:
        redirect(url_for("home"))



@app.route('/reset')
def reset():
    pass

if __name__ == "__main__":
    app.run(debug=True)
