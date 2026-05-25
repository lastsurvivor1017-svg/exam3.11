import uuid


def generate_reference():

    return str(uuid.uuid4())[:12]


def process_payment():

    return "success"