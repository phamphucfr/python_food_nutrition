# python_prject_food_nutrition
une application python permettant de collecter des données nutritionnelles obtenues depuis une source Internet publique


*** Projet InfoNutri ***

Vous êtes chargés de créer une application python permettant de collecter des données nutritionnelles
obtenues depuis une source Internet publique.

Source: https://www.infocalories.fr/

Votre programme devra:
- prendre en entrée l'aliment dont on souhaite connaître les infos nutritionnelles (exemple: tomate).
- réaliser une requête http sur le site source
- explorer la réponse afin de récupérer les informations utiles
- gérer le cas où l'aliment demandé n'est pas trouvé (404)
- instancier une classe Food disposant des propriétés suivantes:
  . name
  . calories
  . fat (lipides)
  . carbs (glucides)
  . protein (protéines)
  les valeurs associées à ce propriétés se feront sur une base de 100 grammes
- prévoir une méthode affichant dans le terminal les informations complètes d'un aliment, ex:
  
  ---------------------------------------
  name    calories  fat   carbs   protein
  tomate  21        0.3   4.6     0.8
  ---------------------------------------
  
- prévoir une méthode permettant d'enregistrer les infos dans un fichier csv
- prévoir une méthode boolénne indiquant si un aliment est gras ou pas
  (vrai, par exemple,siles lipides sont supérieurs à 20%)

- optionnellement, permettre au programme de prendre plusieurs aliments en entrée 
à partir un fichier listant des noms


Votre projet sera constitué d'un module principal et d'un module de test
Votre module de test testera le bon fonctionnement d'une ou deux méthodes de votre module principal

Assurez vous de la qualité du code (pylint)


#-----------------------------#
-- Modalités --
Temps: 3h30
Travail en équipe de 2
Rendre le travail sous forme d'un zip ou d'une url 
vers un dépôt git contenant les sources
#-----------------------------#
