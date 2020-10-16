#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

def order(values: list = None) -> bool:
    #if values is None:
        # TODO: Demander les valeurs ici
        values = [input("Entrez...") for _ in range(10)]
        return values == sorted(values)
    #ou bien 
    #return values == values.sort


def anagrams(words: list = None) -> bool:
    liste1, liste2 = [], []
    if words is None:
        # TODO: Demander les mots ici
        chaine1, chaine2 = input(), input()
        liste1, liste2 = sorted(list(chaine1)), sorted(list(chaine2))

    return liste1 == liste2

def anagrams2(words: list = None) -> bool:
    if words is None:
        words = [input() for _ in range(2)]

    sorted_words = set()
    for word in words:
        sorted_words.add(sorted(str(word)))

    return len(sorted_words) == 1

def anagrams3(words: list = None) ->bool:
    if words is None:
        words = [input() for _ in range(2)]

    word_dicts = [{}, {}]
    for i, word in enumerate(words):
        for letter in word:
            if letter in word_dicts[i]:
                word_dicts[i][letter] += 1
            else:
                word_dicts[i][letter] = 1

    return word_dicts[0] == word_dicts[1]

def anagrams4(words: list = None) -> bool:
    if words is None:
        words = [Counter(input()) for _ in range(2)]

    return words[0] == words[1]

def anagrams5(words: list = None) -> bool:
    if words is None:
        words = [input() for _ in range(2)]
    
    word_dicts = [{},{}]

    return word_dicts[0] == word_dicts[1]

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

def best_grades2(student_grades: dict) -> tuple:
    sorted_grades = sorted(list(student_grades.items()), key = lambda s: -sum(s[1]) / len(s[1]))
    average = sum(sorted_grades[0][1]) / len(sorted_grades[0][1])

    return sorted_grades[0], average

def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    hist = {}
    for char in sentence:
        if char in hist:
            hist[char] += 1
        else:
            hist[char] = 1
    frequency_threshold = 5
    most_frequent_chars = [key for key, value in hist.items() if value > frequency_threshold and key != " "]

    return hist, most_frequent_chars

    #sentence = input("Donnez une phrase: ")
    #histogram(sentence)

def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    name = input("veuillez entrer le nom de la recette: ")
    ingredients = input("veuillez énumérer ses ingrédients:")
    dict_recipes = {name, ingredients}

    dict_recipes["name"] += name 

    message = "Votre recette a été enregistrée."
    return message


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name_recipe = input()
    recipe = ""

    return recipe


def main() -> None:
    #print(f"On essaie d'ordonner les valeurs...")
    #print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    #print("On enregistre les recettes...")
    #recipes = get_recipes()

    #print("On affiche une recette au choix...")
    #print_recipe(recipes)


if __name__ == '__main__':
    main()
