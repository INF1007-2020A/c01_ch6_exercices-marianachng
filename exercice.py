#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        values = [input("Entrez...") for _ in range(10)]
    return values == sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        pass

    return False


def contains_doubles(items: list) -> bool:
    uniques = set(items)
    return len(items) == len(uniques)

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    list_student, list_grades = [], []
    nom, note = None, None

    for student in student_grades:
        student_grades[student] = sum(student_grades[student]) / len(student_grades[student])
        list_student.append(student)
        list_grades.append(student_grades[student])

    for student in range(len(list_student)):
        if list_grades[student] > list_grades[student - 1]:
            nom = list_student[student]
            note = list_grades
    
    return nom, note


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    sentence = input("Donnez une phrase: ")
    histogram(sentence)



    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
