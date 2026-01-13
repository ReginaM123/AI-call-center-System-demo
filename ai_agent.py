def process_message(text):
    text = text.lower()

    if "balance" in text:
        return "Your balance is 1,250 maloti."
    elif "hours" in text:
        return "We are open 24 hours a day."
    elif "agent" in text:
        return "All our human agents are busy. I can assist you."
    else:
        return "I am here to help. Please explain your issue."
