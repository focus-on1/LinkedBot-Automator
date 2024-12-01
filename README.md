### **FocusBot - 🚀 Automatisation LinkedIn 🤖**

---

#### **✨ Description**
**FocusBot** est votre assistant d'automatisation intelligent pour **LinkedIn** ! 🕵️‍♂️ Grâce à des technologies comme **Selenium** et **Telegram**, cet outil analyse, répond et commente automatiquement des publications LinkedIn pour maximiser votre visibilité. Il économise du temps tout en apportant des interactions **constructives** et **pertinentes** à vos réseaux. 🎯  

---

#### **🌟 Fonctionnalités**
- 🔐 **Connexion automatique** à LinkedIn via Selenium.
- 🧐 **Analyse intelligente** des posts pour déterminer leur pertinence.
- 💬 **Génération de réponses adaptées** via un bot Telegram.
- 🚫 **Filtrage des doublons** pour éviter les répétitions inutiles.
- ✨ **Nettoyage des réponses** pour des interactions claires et professionnelles.
- 📂 **Historique des interactions** stocké dans un fichier JSON.
- 🌍 **Support multilingue** : réponses dans la langue des publications.

---

#### **💻 Technologies utilisées**
- **Python** 🐍 : Langage principal.
- **Selenium** 🌐 : Automatisation des interactions LinkedIn.
- **Telethon** 📱 : Communication avec Telegram.
- **JSON** 🗂️ : Stockage des données.
- **Pyperclip** 📋 : Gestion efficace du presse-papiers.

---

#### **🛠️ Prérequis**
1. **Python 3.9+** installé.  
2. **Navigateur Chrome** (ou compatible Selenium).  
3. Installer les dépendances via `pip` :  
   ```bash
   pip install selenium telethon pyperclip
   ```  
4. **Compte Telegram** avec bot ([guide ici](https://core.telegram.org/bots)).  
5. Identifiants LinkedIn valides.  
6. **WebDriver Chrome** téléchargé et configuré dans le PATH.  

---

#### **📥 Installation**
1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/focus-on1/LinkedBot-Automator.git
   cd LinkedBot-Automator
   ```  

2. **Configurer Telegram** :  
   Remplissez les champs `api_id`, `api_hash` et `bot_username` avec vos informations.  

3. **Ajouter vos identifiants LinkedIn** :  
   Dans le script `bot.py` :  
   ```python
   login_linkedin("votre-email", "votre-mot-de-passe")
   ```  

---

#### **🚀 Utilisation**
1. Activez votre bot Telegram. ✅  
2. Lancez le script principal :  
   ```bash
   python bot.py
   ```  
3. Suivez les **logs en temps réel** dans le terminal. 📊  
4. Personnalisez le prompt `prompt_message` selon vos besoins. Intégrez toujours la **fonction de tri** des commentaires pour filtrer ceux qui sont pertinents. 👍  

---

#### **📂 Structure des fichiers**
- **bot.py** : Script principal.  
- **history.json** : Historique des interactions (généré automatiquement).  
- **README.md** : Documentation complète.  

---

#### **🚧 Améliorations futures**
- 🌐 Intégration d'autres plateformes sociales (Twitter, Instagram).  
- 🖥️ Création d'une interface graphique (GUI) pour personnaliser les prompts.  
- ⚡ Optimisation des temps d’exécution.  
- 🤖 Détection des erreurs pour les publications complexes.  

---

#### **⚠️ Avertissement**
L’automatisation sur LinkedIn doit respecter leurs conditions d’utilisation. ⚖️ Utilisez cet outil **de manière responsable** pour éviter des restrictions ou suspensions de votre compte.  

---

#### **🔗 Auteur**
- **Alias** : **Cyber Focus** 🕶️  
- **Contact** : [Me contacter sur Telegram](https://t.me/lighitmook)  
- **Mission** : Faciliter et améliorer votre **visibilité** sur LinkedIn tout en restant **pertinent** ! 🌟  

---

Avec **FocusBot**, prenez le contrôle de votre visibilité sur LinkedIn, engagez intelligemment et gagnez du temps. 🌟💼  

💬 _Vos retours sont précieux pour rendre cet outil encore meilleur !_  

🚀 **Soyez Focus, soyez Cyber !**
