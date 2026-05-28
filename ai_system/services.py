from map.models import Place



def get_nearest_place(lat, lng, category=None):
    places = Place.objects.all()
    return places.first()


def smart_ai(message):
    msg = message.lower()

    if "hospital" in msg:
        place = get_nearest_place(0,0,"hospital")
        return {
            "answer": f"Nearest hospital is {place.name}",
            "type": "map_location"
        }

    if "taxi" in msg:
        return {
            "answer": "Open taxi system",
            "type": "action"
        }

    return {
        "answer": "I don't understand",
        "type": "text"
    }

def simple_chatbot_response(message):
    message = message.lower()
    if "hospital" in message:
        return "The nearest hospital can be viewed in the Maps section."

    if "taxi" in message:
        return "To get a taxi, go to the Marketplace section."

    if "bill" in message:
        return "Bill payments can be done in the Payments section."

    if "traffic" in message:
        return "Traffic status is shown in the Maps section."

    return "Sorry, your question was not found in the system. Please ask more clearly."


def analyze_complaint(text):
    text = text.lower()

    if "road" in text:
        return {
            "category": "road",
            "priority": "high"
        }

    if "water" in text:
        return {
            "category": "water",
            "priority": "medium"
        }

    if "electricity" in text:
        return {
            "category": "electricity",
            "priority": "high"
        }

    return {
        "category": "general",
        "priority": "low"
    }
