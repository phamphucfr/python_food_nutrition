"""check_calories_food.py
Cette application python permet la collecte des données nutritionnelles
obtenues depuis une source Internet publique.
Source: https://www.infocalories.fr/
Projet réalisé par Phuc PHAM NGOC et Fanjavola RAHANTAHARIMANANA
"""
import argparse
from food import Food


def main():
    """main program"""
    parser = argparse.ArgumentParser("Vérifier les infos nutritionnelles d'un aliment")
    # les paramètres -f et -l doivent s'exclure mutuellement
    group = parser.add_mutually_exclusive_group(required=True)
    # nargs='*' permet de prendre en compte plusieurs string pour un seul argument sous form list
    group.add_argument('-f', '--foodname', dest="foodname", nargs='*',
        help="Nom de l'aliment à vérifier")
    group.add_argument('-l', '--foods_file', dest="foods_file",
        help="Fichier contenant la liste de plusieurs aliments à vérifier (Optionnel)")
    args = parser.parse_args()


    if args.foodname:
        # cas de Fruit de la passion
        if len(args.foodname) > 1:
            food_name = ' '.join(args.foodname)
        # cas général: nom en un seul string
        else:
            food_name = args.foodname[0]

    food_object = Food(food_name)
    food_object.show_calories_full()
    food_object.save_to_csv()

main()
