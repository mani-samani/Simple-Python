contacts = {
    "number": 4,
    "students":
        [
            {"name": "Mani Samani", "email": "mani.e.samani@gmail.com"},
            {"name": "Harry Potter", "email": "harry@potter.com"},
            {"name": "Hermione Granger", "email": "hermione@granger.com"},
            {"name": "Ron Weasley", "email": "ron@weasley.com"}
        ]
}

for student in contacts["students"]:
    print(student["email"])
