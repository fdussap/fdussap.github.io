---
pagetitle: "Installation Python -- F. Dussap"
title: "Installation de Python"
---


Cette page explique comment installer tout ce dont vous aurez besoin pour les TP d'analyse numérique : Python, NumPy, Matplotlib, SciPy et Jupyter, via **Miniforge**, l'installeur officiel de conda-forge.

**Pourquoi Miniforge ?** C'est un installeur léger de `conda` préconfiguré pour utiliser le canal conda-forge (communautaire, entièrement gratuit, **sans inscription ni compte à créer**).


Si vous avez déjà Python et les modules installés, passez directement aux sections [Vérifier que tout fonctionne](#vérifier-que-tout-fonctionne) et [Jupyter](#lancer-jupyter) (ce dernier n'est pas absolument nécessaire pour les TP). 


## Installer Miniforge

Se rendre sur la page [conda-forge.org/download/](https://conda-forge.org/download/) et suivre les instructions correspondant à votre système d'exploitation.

### Windows

1. Télécharger l'installeur `.exe` (Miniforge3, Windows x86_64) depuis la page ci-dessus.
2. Double-cliquer sur le fichier téléchargé, puis suivre les instructions.
3. Chercher **"Miniforge Prompt"** dans le menu Démarrer et l'ouvrir : c'est le terminal à utiliser pour toutes les commandes de ce document (ne pas utiliser l'invite de commandes Windows classique ni PowerShell directement).

### macOS

1. Télécharger le script d'installation correspondant à votre puce (`Miniforge3-MacOSX-arm64.sh` pour Apple Silicon M1/M2/M3/M4, `Miniforge3-MacOSX-x86_64.sh` pour un Mac Intel. En cas de doute, cliquer sur le logo Pomme > "À propos de ce Mac").
2. Ouvrir l'application **Terminal**, se placer dans le dossier de téléchargement (`cd ~/Downloads` en général), puis exécuter :

   ```bash
   zsh Miniforge3-MacOSX-*.sh
     
   ```
3. Répondre `yes` aux différentes questions (licence, initialisation de conda).
4. Fermer puis rouvrir le Terminal pour que les changements prennent effet.

### Linux

Deux approches possibles : Miniforge (comme pour Windows/macOS) ou le gestionnaire de paquets de votre distribution.

**Option A : Miniforge**

1. Télécharger le script `Miniforge3-Linux-x86_64.sh` (ou `-aarch64.sh` sur une architecture ARM) depuis la page ci-dessus.
2. Dans un terminal (bash ou zsh selon votre distribution):

   ```bash
   bash Miniforge3-Linux-x86_64.sh
   # ou
   zsh Miniforge3-Linux-x86_64.sh
    
   ```
4. Répondre `yes` aux différentes questions (licence, initialisation de conda dans votre shell — bash/zsh selon votre configuration).
5. Fermer puis rouvrir le terminal.

**Option B : gestionnaire de paquets de la distribution**

Tout dépend de votre distribution. Se référer aux sites suivants :

- https://numpy.org/install/
- https://matplotlib.org/stable/install/index.html
- https://scipy.org/install/


Dans les deux cas (A ou B), la suite de ce document (sections 2 à 5) fonctionne à l'identique, à une différence près : avec l'**Option B**, il n'y a pas d'environnement `conda` à activer, les commandes `conda create`/`conda activate` de la section 3 ne s'appliquent pas.



## Vérifier l'installation

Dans le terminal approprié (Miniforge Prompt sous Windows, Terminal sous macOS/Linux) :
```bash
conda --version
python --version
```
Vous devriez voir s'afficher un numéro de version pour chacune des deux commandes.



## Installer les bibliothèques
 
### Option A : environnement dédié

Créer un environement dédié à cette UE avec la commande :
```bash
conda create -n analyse_num numpy matplotlib scipy jupyter
```

Puis, activer cet environement **à chaque session de travail** avec :
```bash
conda activate analyse_num
```

L'intérêt : si vous installez autre chose plus tard pour un autre projet (ou une autre UE), vous pourrez créer un autre environement, avec ses propres bibliothèques sans qu'il n'y ait de conflit de version. 

 
### Option B : tout installer directement dans `base`
 
Plus simple pour un usage ponctuel : `base` est l'environnement actif par défaut à l'ouverture d'un terminal (vous devriez voir `(base)` au début de la ligne de commande), donc pas besoin de créer ni d'activer quoi que ce soit.
 
```bash
conda install -n base numpy matplotlib jupyter scipy
```
(le `-n base` est optionnel si `(base)` est déjà actif dans votre terminal, mais ne coûte rien de le préciser pour être sûr).
 
**Inconvénient** : si vous réutilisez ensuite cette même installation de conda pour un autre projet qui a besoin d'une version différente de NumPy (par exemple), il y aura conflit.
 




## Vérifier que tout fonctionne

Télécharger le fichier <a href="./Files/Analyse_numerique/test_install.py" download>test_install.py</a>, puis l'exécuter (avec l'environnement `analyse_num` activé) :
```bash
python test_install.py
```
Une fenêtre doit s'ouvrir avec le graphique d'une sinusoïde.


## Lancer Jupyter

Il n'est pas indispensable d'utiliser Jupyter pour les TP. Si vous préférez travailler avec des scripts Python, vous pouvez.

Deux interfaces possibles :

- **Jupyter Notebook** : l'interface classique, un fichier `.ipynb` par onglet de navigateur.
- **JupyterLab** : une interface plus complète (plusieurs fichiers ouverts, explorateur de fichiers intégré), recommandée si elle est disponible.

Dans le terminal, avec l'environnement activé (`conda activate analyse_num`), se placer dans le dossier contenant vos fichiers de TP puis taper :

```bash
jupyter notebook
# ou
jupyter lab
```

Une page s'ouvre automatiquement dans votre navigateur. Ouvrir le fichier <a href="./Files/Analyse_numerique/test_install.ipynb" download>test_install.ipynb</a> et suivre ses instructions.

**Pour arrêter le serveur Jupyter**, revenir dans le terminal et faire `Ctrl+C` (parfois deux fois), ou aller dans **File > Shut down** (jupyter lab) ou appuyer sur le bouton **Quit** (jupyter notebook).

