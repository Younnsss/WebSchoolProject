# Documentation des Chemins URL

### Public = Funfacts

- **`/`**
  - **Description**: Affiche la liste des faits amusants. Les utilisateurs peuvent UP ou DOWN chaque fact.

- **`/create`**
  - **Description**: Formulaire pour ajouter un nouveau funfact.

- **`vote/<int:funfact_id>/<str:vote_value>/`**
  - **Description**: Route pour comptabiliser le vote d'un utilisateur pour un funfact.

### API

- **`api/facts/`**
  - **Description**: Endpoint pour récupérer la liste des funfacts

- **`api/votes/`**
  - **Description**: Endpoint pour récupérer la liste des votes


# Questions

### Fonctionnement de Django

1. **Affichage d'une page HTML `index.html` à l'URL global `/` via une application `public`**:
    - **Requête**: L'utilisateur accède à l'URL `/`.
    - **Global Route**: Après une comparaison au urlpatterns de djangoapp/urls.py, la requête est dirigée vers l'application public soit au fichier `public/urls.py`.
    - **Route**: Dans le `public/urls.py` de l'application public, une route est définie pour `/`, cette route définie la view associé.
    - **Vue**: La route appelle donc la vue définie qui va elle-même faire appel à un template htlm correspondant au contenu de la page.
    - **Template**: La vue rend le template `index.html` situé dans `public/templates/public/index.html`.

    **Arborescence des répertoires**:
    ```
    project_root/
    ├── public/
    │   ├── templates/
    │   │   └── public/
    │   │       └── index.html
    │   ├── urls.py
    │   └── views.py
    └── project/
        └── urls.py
    ```

2. **Configuration de la base de données**:
    - **Fichier**: `settings.py`
    - **Section**: `DATABASES`

 ex : 
 ...
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "mydb",
        'USER': "myuser",
        'PASSWORD': "mypassword",
        'HOST': "db",
        'PORT': '5432',
    }
}
...

3. **Configuration du fichier de paramètres**:
    - **Fichier principal**: `settings.py`
    - **Fichiers supplémentaires**: `settings_dev.py`, `settings_prod.py` (pour des configurations spécifiques à l'environnement)

4. **Commandes `makemigrations` et `migrate`**:
    - **`makemigrations`**: Crée seulement les fichiers de migration pour les modifications de modèle.
    - **`migrate`**: Applique les migrations à la base de données (créé les tables, ...)
    - **Fichiers mis en œuvre**: `models.py` représentant les tables, fichiers de migration dans `migrations/`.

### Fonctionnement de Docker

1. **Commandes Dockerfile**:
    - **`FROM`**: Spécifie l'image de base.
    - **`RUN`**: Exécute des commandes dans le conteneur.
    - **`WORKDIR`**: Définit le répertoire de travail dans lequel seront effectué es actions suivantes.
    - **`EXPOSE`**: Indique les ports exposés. C'est seulement à  titre indicatif
    - **`CMD`**: Spécifie la commande par défault à exécuter au démarrage du conteneur. Elle peut être facilement override.

2. **Définition d'un service dans [`docker-compose.yml`]**:
    - **`ports`**: Mappe les ports du conteneur aux ports de la machine hôte.
    - **`build`**: Spécifie le contexte et le Dockerfile pour construire l'image.
    - **`depends_on`**: Définit les dépendances entre services. Ainsi on peut choisir l'ordre dans lequel seront lancés les conteneurs selon les dépendances
    - **`environment`**: Définit les variables d'environnement dans le container.

3. **Définir des variables d'environnement**:
    - **Méthode**: Utiliser la commande Dockerfile **`ENV`**

4. **Adresser le serveur web dans un réseau Docker**:
    - **Solution**: Utiliser le nom du service Docker (par exemple, `web`) dans la configuration Nginx.