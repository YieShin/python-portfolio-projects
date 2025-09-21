import pywhatkit as kit
import datetime

# Demo WhatsApp Auto-Reply
def send_auto_reply():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1  # send 1 minute later

    phone_number = "+60123456789"  # <-- replace with test number
    message = (
        "Hello 👋\n"
        "Thanks for reaching out to our business!\n\n"
        "Reply with:\n"
        "1️⃣ Price List\n"
        "2️⃣ Contact Info\n"
        "3️⃣ Working Hours\n"
    )

    kit.sendwhatmsg(phone_number, message, hour, minute)
    print("✅ Auto-reply scheduled in WhatsApp Web!")

if __name__ == "__main__":
    send_auto_reply()