contact = {
    'number': 3,
    'students': [
        {
            'name': 'sara',
            'email': 'sara@gmail.com' 
        },
        {
            'name': 'boo',
            'email': 'boo123@gmail.com' 
        },
        {
            'name': 'zue',
            'email': 'zue123@outlook.com' 
        }
    ]
}

print("Student emails:")

for student in contact['students']:
    print(student['email'])