
# /****************************************
#  *         CYBER FOCUS SCRIPT          *
#  *       POST LINKEDIN AUTOMATION     *
#  ****************************************/

import time
import re
import pyperclip
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from telethon import TelegramClient, sync

#  _______     ______  ______ _____    ______ ____   _____ _    _  _____
# / ____\ \   / /  _ \|  ____|  __ \  |  ____/ __ \ / ____| |  | |/ ____|
#| |     \ \_/ /| |_) | |__  | |__) | | |__ | |  | | |    | |  | | (___
#| |      \   / |  _ <|  __| |  _  /  |  __|| |  | | |    | |  | |\___ \
#| |____   | |  | |_) | |____| | \ \  | |   | |__| | |____| |__| |____) |
# \_____|  |_|  |____/|______|_|  \_\ |_|    \____/ \_____|\____/|_____/
# /****************************************
#  *       SELENIUM-TELEGRAM-linkedin  *
#  ****************************************/

###########################################################

###########################################################

# Informations de connexion Telegram
api_id = 'APIID'  # specifie votre API telegrame 
api_hash = 'APIHASH'
bot_username = 'Free_of_ChatGPT_bot' #specification du bot telegrame chatgpt que nous allons utilise 

# Initialiser le client Telegram
client = TelegramClient('session_name', api_id, api_hash) # connection avec la session de votre compte telegrame 
client.start() 

# Initialiser le WebDriver
driver = webdriver.Chrome()

# fichier avec tout les reponse et les status de reponse ainsi que les post 
history_file = 'history.json'  

############################################

"""ceux ci sont les fonction de base qui vons permettre le bon fonctionement et une logique dans la recherche de commentaire 
il permette non seulement d'avoir une optimisation niverau doublon pour ne pas repondre plusieur fois au meme commentaire
mais egalement l'enrgistrement des post de la date et de la reponse de chatgpt pour pouvoir ameliore le prompt"""

try:
    with open(history_file, 'r', encoding='utf-8') as f: 
        history = json.load(f)
except FileNotFoundError:
    history = []


# FONCTION qui permet d'enrgisitre les commetaire leur statut 
def save_to_history(post_text, status,cleaned_response):

    history.append({
        "post_text": post_text,
        "comment_date": datetime.now().isoformat(),  
        "ia_reponse" : cleaned_response,
        "status": status
    })
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4)


def cheak_doublon(post_text):
    for i in history:
        if i['post_text'] == post_text:
            return True
    return False 


def login_linkedin(email, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)

    # Remplir les champs de connexion
    champs_email = driver.find_element(By.ID, "username")
    champs_email.send_keys(email)

    password_champs = driver.find_element(By.ID, "password")
    password_champs.send_keys(password)

    # Cliquer sur le bouton "S'identifier"
    login_button = driver.find_element(By.XPATH, "//button[@aria-label='S’identifier']")
    login_button.click()
    time.sleep(5)  # Attendre que la page de feed se charge

#####################################################
                # CLEAR
##################################################

"""ceux  code et essentiel il permet de nettoye la reponse du bot telegame car comme nous utilison un bot qui donne des 
reponse gratuite il y'a quelque information en + dans la reponse que nous voulons pas integre nous somme oblige 
de filtre cela avec re"""


def clean_telegram_response(response_text):
    # Enlever les URL
    cleaned_text = re.sub(r'http\S+', '', response_text)
    
    # Enlever tout texte en chinois suivi de `？` ou `：`
    cleaned_text = re.sub(r'[\u4e00-\u9fff]？', '', cleaned_text)  # Supprime les caractères chinois suivis de `？`
    cleaned_text = re.sub(r'[\u4e00-\u9fff]：', '', cleaned_text)  # Supprime les caractères chinois suivis de `：`
    
    # Enlever tout texte en chinois (restant)
    cleaned_text = re.sub(r'[\u4e00-\u9fff]+', '', cleaned_text)
    
    # Enlever les mentions de sponsors et autres textes indésirables
    cleaned_text = re.sub(r'赞助商.*$', '', cleaned_text, flags=re.MULTILINE)
    cleaned_text = re.sub(r'不会用.*$', '', cleaned_text, flags=re.MULTILINE)
    
    # Supprimer les symboles `?` et `:`
    cleaned_text = cleaned_text.replace('?', '').replace(':', '')

    # Retirer le texte commençant par 'AI' ou 'IA' à la fin
    cleaned_text = re.sub(r'AI.*$', '', cleaned_text, flags=re.MULTILINE)
    cleaned_text = re.sub(r'IA.*$', '', cleaned_text, flags=re.MULTILINE)
    
    # Nettoyer les espaces en trop
    cleaned_text = cleaned_text.strip()
    
    return cleaned_text



##################################################################
                    # BOUCLE PRINCIPALE 
#################################################################
 
def extract_and_comment_posts():
    while True:  # Boucle infinie pour le traitement en continu
        posts = driver.find_elements(By.CSS_SELECTOR, "div.feed-shared-update-v2") # on intialise la div  des post en general 
        
        # boucle qui permet parcourir les post via la div posts
        for post in posts:
            try:
                # Extraire le texte de la publication
                post_text_element = post.find_element(By.CSS_SELECTOR, "div.update-components-text.relative.update-components-update-v2__commentary")
                post_text = post_text_element.text 
                print("Contenu de la publication :")
                print(post_text) # print le text de la publication 
                
                # Vérifier si ce post a déjà été commenté
                if cheak_doublon(post_text):
                    print("Ce post a déjà été commenté. Passage au suivant.")
                    continue
                
                # Préparer le prompt et envoyer au bot Telegram

                """ceux prompt peut etre modifie et personalise pour votre situation et votre caractere esseye de cree un prompt qui et pas trops long car
                par la suite cela sera complique d'integre le post telegramena des limite de caracter et surtout ne pas enleve la fonction qui permet de filtre
                les post qui ne sont pas pertinant cette condition et importante dans l'optimisation des commentaire """

                prompt_message = f"Réponds aux posts LinkedIn comme le ferait un étudiant en BTS Cybersécurité. Les réponses doivent être naturelles, courtes, pertinentes et adaptées au contexte du post ajoute une valeur ajoute au post un + que le post n'a pas relevé si cela et possible pour ceux démarque des autre evite d'ajoute des emogie a la fin  . Si le post est court, peu clair, ou n'a pas de sens, répond simplement avec un '👍'. Respecte absolument la langue du post original : si le post est en anglais, réponds en anglais ; si le post est en français, réponds en français ; pour toute autre langue, fais de même. Ne néglige jamais cette règle de langue..  \n\n---------------------\nPOST : {post_text}"
                bot_response = client.send_message(bot_username, prompt_message)
                time.sleep(10)  # Attendre 10 secondes pour minimiser les requêtes

                # Récupérer la réponse du bot

                response = client.get_messages(bot_username, limit=1)[0].message #recupre le dernier message envoye du bot free chatcgpt
                cleaned_response = clean_telegram_response(response) # on clean la reponse on enleve tout les caracter speciaux etc
                print("Réponse du bot :")
                print(cleaned_response)

                """cette condition permet de faire en sorte de filtre si le contenue et juge comme non pertinent pour 
                une reponse alors chatgpt donera un pouce ceux pouce signfie passe au post suivent"""

                if cleaned_response == "👍":
                    print("La réponse du bot est un pouce. Enregistrement sans commentaire.")
                    # Enregistrer le post dans l'historique avec un statut False
                    save_to_history(post_text, status=False, cleaned_response=cleaned_response)
                    continue  # Passer au prochain post

                # Copier la réponse dans le presse-papiers, y compris les émojis et les caractères spéciaux   
                pyperclip.copy(cleaned_response)
                
                # Publier le commentaire sur LinkedIn
                comment_button = post.find_element(By.CSS_SELECTOR, "button.social-actions-button.comment-button")
                comment_button.click()
                time.sleep(2)  # Attendre que la boîte de commentaire apparaisse
                
                comment_box = post.find_element(By.CSS_SELECTOR, "div.ql-editor.ql-blank[contenteditable='true']")
                comment_box.click()
                comment_box.send_keys(Keys.CONTROL, 'v')  # Coller le contenu du presse-papiers
                
                time.sleep(2)  # Attendre un peu avant de cliquer sur "Publier"
                
                publish_button = post.find_element(By.XPATH, "//button//span[text()='Publier']")
                publish_button.click()
                time.sleep(2)  # Attendre que le commentaire soit publié
                
                # Enregistrer le commentaire dans l'historique avec un statut True
                save_to_history(post_text, status=True, cleaned_response=cleaned_response)
                
                # Attendre avant de passer au post suivant
                print("Attente avant de vérifier le prochain post...")
                time.sleep(15)  # Attendre 15 secondes avant de traiter le prochain post
                
            except Exception as e:
                print(f"Erreur lors du traitement du post : {e}")
        
        # Rafraîchir la page LinkedIn après chaque cycle de traitement
        print("Rafraîchissement de la page LinkedIn...")
        
        time.sleep(5)  # Attendre que la page se recharge avant de continuer
        
        # Attendre avant de recommencer à traiter les posts
        print("Attente avant de vérifier les nouveaux posts...")
        time.sleep(30)  # Pause de 30 secondes avant de vérifier à nouveau les posts

def main():
    try:
        login_linkedin("MAIL", "MDP")
        extract_and_comment_posts()  # Commencer la boucle continue
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
