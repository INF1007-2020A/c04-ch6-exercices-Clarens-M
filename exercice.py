#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        for i in range (0, 10):
            a = input("Entrez un nombre entier, décimal ou un mot")
            values.append(a)

    return values.sort()


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot1 = str(input("Entrez le premier mot: "))
        mot2 = str(input("Entrez le second mot: "))
        words.append(mot1, mot2)
        count = 0
        anagramme = False
        for c in word[0]:
            if c in word[1] or c.upper() in word[1] or c.lower() in word:
                count += 1
        if count == len(word[1]):
            anagramme= True

    return anagramme


def contains_doubles(items: list) -> bool:
    doubles = False
#    count = 0
#    for c in items:
#        for i in range(0, len(items)):
#            if items[i] == c:
#                count += 1
#            
#    if count != 0:
#        doubles = True
    ensemble = set(items)
    if len(ensemble) != len(items):
        doubles = True
    return doubles


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best = dict()
    for key, value in student_grades.items():
        moyenne = sum(value)/len(value)
        
        if len(best) == 0:
            best = {key: moyenne}
            g = key
        if list(best.keys())[0] < moyenne:
            best = {key: moyenne}
            g = key
            
        
        
    return best{g}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    palier = 0
    count = 0
    dico = {}
    for c in sentence:
        if c == " ":
            continue
        else:
            dico[c] = sentence.count(c)

    sorted_keys = sorted(dico, key=dico.__getitem__, reverse = True)
    for key in sorted_keys:
        if dico[key] > 5: 
            print(f"Le caractère {key} revient {dico[key]} fois."
    #       Retourner le tableau de lettres
    
    return dico


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom_recette = str(input("Entrez le nom d'une recette que vous voulez ajouter: ")
    livre = {}
    nombre = int(input("Entrez le nombre d'ingrédients: "))
    ingrédients = []
    for i in range(0, nombre):
        b = str(input("Nom de l'ingrédient: "))
        ingrédients.append(b)
    livre[nom_recette] = ingrédients
    return livre


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    demande = str(input("Quelle recette voulez-vous connaitre: "))
    if demande in livre:
        return(livre[demande])
    else:
        print("Les recettes du livres sont :")
        print(list(ingrédients.keys()))


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
