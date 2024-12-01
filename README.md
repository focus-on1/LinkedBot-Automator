###  **FocusBot - Automatisation LinkedIn**

---

#### **Description**
FocusBot est un outil d'automatisation conçu pour LinkedIn, intégrant des technologies comme **Selenium** et **Telegram** pour interagir avec des posts LinkedIn de manière intelligente. Il permet de lire des publications, de générer des réponses adaptées via un bot Telegram, et de commenter automatiquement tout en évitant les doublons. Cet outil est spécialement pensé pour maximiser l'engagement sur LinkedIn tout en économisant du temps.

---

#### **Fonctionnalités**
- **Connexion automatique** à LinkedIn via Selenium.
- **Analyse des posts LinkedIn** pour déterminer leur pertinence.
- **Génération de réponses intelligentes** grâce à un bot Telegram.
- **Filtrage des doublons** pour éviter les réponses répétées.
- **Nettoyage des réponses** pour une meilleure lisibilité et un ton professionnel.
- **Historique des interactions** stocké dans un fichier JSON.
- **Réponses multilingues** en fonction de la langue du post.

---

#### **Technologies utilisées**
- **Python** : Langage principal.
- **Selenium** : Automatisation des interactions avec l'interface LinkedIn.
- **Telethon** : Intégration avec Telegram pour obtenir des réponses automatisées.
- **JSON** : Stockage de l’historique des interactions.
- **Pyperclip** : Gestion du presse-papiers pour coller les réponses.

---

#### **Prérequis**
1. **Python 3.9+** installé.
2. Navigateurs compatibles avec Selenium (**Chrome** recommandé).
3. Les dépendances suivantes installées via `pip` :
   ```bash
   pip install selenium telethon pyperclip
   ```
4. Un compte Telegram avec un bot configuré ([documentation officielle](https://core.telegram.org/bots)).
5. Identifiants LinkedIn valides.
6. **WebDriver Chrome** téléchargé et placé dans le PATH du système.

---

#### **Installation**
1. Clonez ou téléchargez ce dépôt :
   ```bash
   git clone https://github.com/focus-on1/LinkedBot-Automator.git
   cd LinkedBot-Automator
   ```

2  Configurez votre fichier Telegram :
   - Remplacez `api_id`, `api_hash` et `bot_username` dans le script par vos informations Telegram.

3 Modifiez vos identifiants LinkedIn dans le code :
   ```python
   login_linkedin("votre-email", "votre-mot-de-passe")
   ```

---

#### **Utilisation**
1. Assurez-vous que votre bot Telegram est actif.
2. Exécutez le script :
   ```bash
   python bot.py
   ```
3. Suivez les logs dans le terminal pour surveiller les actions du bot.

---

#### **Structure du fichier**
- **focusbot.py** : Script principal.
- **history.json** : Fichier contenant l'historique des interactions (généré automatiquement).
- **README.md** : Ce document.

---

#### **Améliorations futures**
- Ajouter la gestion d'autres plateformes sociales.
- Intégrer une interface graphique (GUI) pour personnaliser les prompts.
- Optimiser les temps d’attente pour plus d’efficacité.
- Ajouter une fonctionnalité de détection d’erreurs pour des publications plus complexes.

---

#### **Avertissement**
L’automatisation des interactions sur LinkedIn est soumise à leurs conditions d’utilisation. Utilisez cet outil de manière responsable et assurez-vous de respecter leurs politiques pour éviter des sanctions sur votre compte.

---

#### **Auteur**
- **Alias** : Cyber Focus  
- **Contact** : https://t.me/lighitmook
- **Projet dédié à la communauté des étudiants en cybersécurité et professionnels du réseau.**  

---

Avec **FocusBot**, engagez intelligemment et efficacement sur LinkedIn tout en économisant votre temps. 🚀
