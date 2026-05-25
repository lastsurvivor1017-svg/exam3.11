from complaints.models import Complaint


def complaint_by_category():
    data = {}

    complaints = Complaint.objects.all()

    for c in complaints:

        if c.category not in data:
            data[c.category] = 0

        data[c.category] += 1

    return data