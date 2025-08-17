[app]
# Nom de l'application
title = MonApp

# Nom du package (sans espace, minuscule)
package.name = monapp

# Domaine inversé (unique)
package.domain = org.monapp

# Dossier contenant ton code
source.dir = .

# Extensions de fichiers incluses
source.include_exts = py,png,jpg,kv,db,atlas,ttf,txt,mp3,wav,json

# Version de ton application
version = 0.1

# Librairies Python nécessaires
# On force PyJNIus depuis GitHub pour corriger l'erreur "long"
requirements = python3,kivy==2.2.1,kivymd==1.1.1,https://github.com/kivy/pyjnius/archive/master.zip,sqlite3

# Orientation de l'application
orientation = portrait

# Permissions Android (ajoute ici celles dont tu as besoin)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Icône et splash screen (facultatif, à personnaliser)
icon.filename = %(source.dir)s/R.png
presplash.filename = %(source.dir)s/R.png

# Inclure des fichiers supplémentaires dans l’APK
# exemple : android.add_assets = ./data
# android.add_assets = 

[buildozer]
# Niveau de logs (2 = normal, 1 = silencieux, 3 = détaillé)
log_level = 2

# Évite l’avertissement root dans WSL
warn_on_root = 0

# Version de l’API Android
android.api = 31

# API minimale supportée
android.minapi = 21

# Version SDK utilisée pour compiler
android.sdk = 28

# Version du NDK (25b est la plus stable pour Kivy)
android.ndk = 25b

# API du NDK
android.ndk_api = 21

# Type de compilation (armeabi-v7a = 32 bits, arm64-v8a = 64 bits, ou les deux)
# android.archs = armeabi-v7a, arm64-v8a

# Forcer la réinstallation des dépendances locales si besoin
p4a.local_recipes = ./recipes

# Si tu veux déboguer avec adb :
# adb = /chemin/vers/adb

android.sdk_path = ./android-sdk
android.ndk_path = ./android-ndk
