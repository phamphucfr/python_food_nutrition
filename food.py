""" instancier une classe Food disposant des propriétés suivantes:
   . name
   . calories
   . fat (lipides)
   . carbss (glucides)
   . protein (protéines)
   les valeurs associées à ces propriétés se feront sur une base de 100 grammes
**Projet réalisé par Phuc PHAM NGOC et Fanjavola RAHANTAHARIMANANA
"""

import os
import csv
from bs4 import BeautifulSoup
import requests

URL_PREFIX = "https://www.infocalories.fr/calories/calories-"
TABLE_LINE = "-------------------------------------------------------------------------"
CSV_FILE = "foods_calories.csv"

class Food :
    """ classe food"""
     # propriétés (variables définies dans une classe)
    name = ''
    calories = 0
    fat = 0.0
    carbs = 0.0
    protein = 0.0

    # méthodes (fonctions définies dans une classe)
    def __init__(self, name:str) -> None:
        """Constructor for new food"""
        # Création d'une nouvelle instance avec un nom
        food_page = name.replace(' ','-').casefold()
        try:
            html_page = self.check_food_presence(food_page)
        except ValueError:
            print(f"[-] Aliment {name} n'est pas trouvé dans notre base de données")
            exit(2) # pylint: disable=consider-using-sys-exit
        food_dict = self.extract_data_from_html(html_page)
        self.name = name
        self.calories = int(food_dict["calories"])
        self.carbs = float(food_dict["carbs"])
        self.fat = float(food_dict["fat"])
        self.protein = float(food_dict["protein"])

    def show_calories_full(self):
        """afficher les infos nutri de l'aliment dans Terminal"""
        print(TABLE_LINE)
        print("name".ljust(30)+
            "calories(KCal)".ljust(15)+
            "fat".ljust(10)+
            "carbs".ljust(10)+
            "protein".ljust(10))
        print(self.name.ljust(30)+
            str(self.calories).ljust(15)+
            str(self.fat).ljust(10)+
            str(self.carbs).ljust(10)+
            str(self.protein).ljust(10))
        print(TABLE_LINE)

    def check_fat(self) -> bool:
        """check if the food is too fat or not"""
        if self.fat > 0.2:
            is_fat = True
        else: 
            is_fat = False
        return is_fat

    def save_to_csv(self):
        """save calories food infos in the csv file"""
        header = ["'Name'", "'Calories(Kcal)'", "'Fat(g)'", "'Carbs(g)'", "'Protein(g)'"]
        row = [f"{self.name}", self.calories, self.fat, self.carbs, self.protein]
        if os.path.exists(CSV_FILE):
            # Cas où le fichier est déjà généré, on ajoute nouvelle ligne
            with open (CSV_FILE,'a',newline = '',encoding='UTF8') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = ';')
                my_writer.writerow(row)
        else:
            # Cas où le fichier n'est pas encore créé
            with open (CSV_FILE,'w',newline = '',encoding='UTF8') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = ';')
                my_writer.writerow(header)
                my_writer.writerow(row)

    def extract_data_from_html(self, html_page: str) -> dict:
        """extract data from html page"""
        soup = BeautifulSoup(html_page, 'html.parser')

        div_block = soup.find("div", attrs={'id': 'diva'})
        b_block = div_block.find_all("b")
        values = []
        for val in b_block:
            val = str(val).strip("<b></b>") # pylint: disable=bad-str-strip-call
            if "g" in val:
                val = val.strip("g").replace(',','.')
            if " Kcal" in val:
                val = val.strip(" Kcal").replace(',','.')
            values.append(val)
        # On retourne les valeurs extraites sous forme d'un dictionnaire Python
        food_dict = {'calories':values[0], 'protein':values[1], 'carbs': values[2], 'fat':values[3]}
        return food_dict


    def check_food_presence(self, food_name: str) -> str:
        """check calories food"""
        req_food = requests.get(f"{URL_PREFIX}{food_name}.php")
        if req_food.status_code == 404:
            # si return code 404 de la requete GET
            raise ValueError("Food not found in database")
        return req_food.text