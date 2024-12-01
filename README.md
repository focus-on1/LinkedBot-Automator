### **FocusBot - 🚀 Automatisation LinkedIn 🤖**

---

#### **✨ Description**
**FocusBot** est votre assistant d'automatisation intelligent pour **LinkedIn** ! 🕵️‍♂️ Avec des technologies avancées comme **Selenium** et **Telegram**, il analyse, génère et publie des réponses adaptées pour maximiser votre visibilité tout en optimisant votre temps. 🎯 Plus besoin de passer des heures à interagir : **FocusBot** rend vos contributions sur LinkedIn à la fois **constructives** et **pertinentes**. 💡  

---

#### **🌟 Fonctionnalités principales**
- 🔐 **Connexion automatique** sécurisée à LinkedIn via Selenium.  
- 🧐 **Analyse intelligente** des publications pour identifier leur pertinence.  
- 💬 **Génération automatique de réponses** personnalisées via un bot Telegram.  
- 🚫 **Filtrage des doublons** pour éviter toute redondance.  
- ✨ **Nettoyage avancé des réponses** pour garantir un ton professionnel et fluide.  
- 📂 **Historique des interactions** sauvegardé dans un fichier JSON.  
- 🌍 **Support multilingue** : réponses générées dans la langue détectée.  

---
![image](https://github.com/user-attachments/assets/745350c2-d1be-4aa2-9fdd-9928256d9c35)

#### **💻 Technologies utilisées**
- **Python** 🐍 : Langage principal.  
- **Selenium** 🌐 : Automatisation des actions LinkedIn.  
- **Telethon** 📱 : Communication entre Telegram et le bot.  
- **JSON** 📄 : Gestion des données stockées.  
- **Pyperclip** 📋 : Manipulation pratique du presse-papiers.  

---

#### **🛠️ Prérequis**
1. **Python 3.9+** installé.  
2. **Navigateur Chrome** (ou tout autre compatible Selenium).  
3. Installez les dépendances requises :  
   ```bash
   pip install selenium telethon pyperclip
   ```  
4. Configurez un **bot Telegram** ([guide officiel ici](https://core.telegram.org/bots)).  
5. Fournissez vos identifiants LinkedIn valides.  
6. Téléchargez et configurez **Chrome WebDriver** dans le PATH.  
7. Ajoutez le bot suivant à votre compte Telegram pour intercepter et traiter les requêtes :  
   👉 **@Free_of_ChatGPT_bot**  

---

#### **📥 Installation et configuration**
1. **Clonez le dépôt GitHub** :
   ```bash
   git clone https://github.com/focus-on1/LinkedBot-Automator.git
   cd LinkedBot-Automator
   ```  

2. **Configurez le bot Telegram** :  
   Dans le fichier `bot.py`, renseignez vos `api_id`, `api_hash` et `bot_username`.  

3. **Ajoutez vos identifiants LinkedIn** :  
   Modifiez la fonction `login_linkedin()` dans le script principal :  
   ```python
   login_linkedin("votre-email", "votre-mot-de-passe")
   ```  

---

#### **🚀 Lancement de FocusBot**
1. **Activez votre bot Telegram**. ✅  
2. Exécutez le script :  
   ```bash
   python bot.py
   ```  
3. Surveillez les logs dans le terminal pour suivre les actions. 📊  
4. Personnalisez le message généré par le bot dans `prompt_message` en ajoutant vos préférences.  
   👉 Astuce : utilisez la **fonction de tri des commentaires** pour garantir leur pertinence. 👍  

---

#### **📂 Structure des fichiers**
- **bot.py** : Script principal.  
- **history.json** : Sauvegarde de l’historique des interactions.  
- **README.md** : Documentation complète.  

---

#### **🚧 Prochaines évolutions**
- 🌐 Intégration de plateformes sociales supplémentaires (ex. : Twitter, Instagram).  
- 🖥️ Développement d’une **interface graphique (GUI)** pour une personnalisation intuitive.  
- ⚡ Réduction des temps d’exécution pour une meilleure efficacité.  
- 🤖 Gestion avancée des erreurs pour des publications complexes.  

---

#### **⚠️ Avertissement**
L’automatisation sur LinkedIn doit toujours respecter leurs conditions d’utilisation. ⚖️ Utilisez **FocusBot** avec précaution pour éviter toute sanction de compte.  

---

#### **🔗 Auteur**
- **Alias** : **Cyber Focus** 🕶️  
- **Contact** : [Envoyez-moi un message !](https://t.me/lighitmook)  
- **Mission** : Aider les professionnels à gagner en visibilité et à rester pertinents dans leurs interactions. 🌟  

---

Avec **FocusBot**, économisez du temps, améliorez votre visibilité et interagissez de manière stratégique et professionnelle. 🌟💼  

💬 Vos retours sont essentiels pour continuer d’améliorer cet outil !  
🚀 **Soyez Focus, soyez Cyber !**
