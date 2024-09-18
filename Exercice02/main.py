students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
    'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

user_input = input("Entrez le nom de l’étudiant : ")

if user_input in students.keys():
    print(f'Notes de {user_input}')
    moyenne = 0
    for keys in students[user_input]:
        moyenne += students[user_input][keys]
        print(f'{keys} : {students[user_input][keys]}')
    moyenne /= len(students[user_input])
    print(f'moyenne : {moyenne}')
else:
    print(f"L'étudiant {user_input} n'existe pas dans la liste")
