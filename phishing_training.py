import time

def show_message(message):
    print("\n" + message)
    time.sleep(1.5)

def phishing_intro():
    show_message("📧 Welcome to Phishing Awareness Training!")
    show_message("Phishing is a cyber attack where attackers trick you into revealing sensitive info.")
    show_message("They often disguise themselves as trusted entities (banks, IT support, etc.)")

def how_to_recognize():
    show_message("🔍 How to Recognize Phishing Emails:")
    show_message("- Look for urgent or threatening language ('Your account will be closed')")
    show_message("- Check the sender's email address (does it look legit?)")
    show_message("- Hover over links: Do they go to suspicious or unknown domains?")
    show_message("- Grammar/spelling mistakes")

def fake_websites():
    show_message("🌐 Fake Websites:")
    show_message("- Often mimic real sites with slight domain changes (e.g., amaz0n.com)")
    show_message("- HTTPS doesn’t always mean safe!")
    show_message("- Check for misspelled brand names and odd layouts")

def social_engineering():
    show_message("🎭 Social Engineering Tactics:")
    show_message("- Pretexting: attacker pretends to be someone you trust")
    show_message("- Baiting: fake rewards or free stuff")
    show_message("- Tailgating: following employees into restricted areas")

def best_practices():
    show_message("✅ Best Practices:")
    show_message("- Don’t click suspicious links or download unknown attachments")
    show_message("- Verify requests by contacting the source directly")
    show_message("- Enable 2FA (Two-Factor Authentication)")
    show_message("- Report phishing attempts to your IT department")

def quiz():
    score = 0

    print("\n🧠 Quiz Time!")

    q1 = input("\n1. You get an email from your bank asking to confirm your password. What should you do?\n"
               "a) Click the link and enter your details\n"
               "b) Call your bank using a known number to verify\n"
               "c) Reply to the email asking for confirmation\nYour answer: ").strip().lower()
    if q1 == "b":
        score += 1

    q2 = input("\n2. A site looks like PayPal but the URL is 'paypa1.com'. Safe or suspicious?\n"
               "a) Safe\nb) Suspicious\nYour answer: ").strip().lower()
    if q2 == "b":
        score += 1

    q3 = input("\n3. You see spelling mistakes and urgency in an email. What might this indicate?\n"
               "a) Nothing important\nb) A phishing attempt\nYour answer: ").strip().lower()
    if q3 == "b":
        score += 1

    show_message(f"✅ You scored {score}/3")

def main():
    phishing_intro()
    how_to_recognize()
    fake_websites()
    social_engineering()
    best_practices()
    quiz()
    show_message("🎉 Training complete! Stay alert and stay safe online.")

if __name__ == "__main__":
    main()
