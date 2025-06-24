import os
import shutil

# Dictionnaire des extensions et leurs dossiers cibles
EXTENSIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Autres': []
}

def organiser_dossier(dossier):
    for fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, fichier)
        if os.path.isfile(chemin_complet):
            deplacer_fichier(chemin_complet, dossier)

def deplacer_fichier(chemin_fichier, dossier_base):
    _, extension = os.path.splitext(chemin_fichier)
    deplace = False

    for dossier_cible, extensions in EXTENSIONS.items():
        if extension.lower() in extensions:
            nouveau_dossier = os.path.join(dossier_base, dossier_cible)
            os.makedirs(nouveau_dossier, exist_ok=True)
            shutil.move(chemin_fichier, nouveau_dossier)
            print(f"Déplacé : {chemin_fichier} -> {nouveau_dossier}")
            deplace = True
            break

    if not deplace:
        autre_dossier = os.path.join(dossier_base, 'Autres')
        os.makedirs(autre_dossier, exist_ok=True)
        shutil.move(chemin_fichier, autre_dossier)
        print(f"Déplacé : {chemin_fichier} -> {autre_dossier}")

if __name__ == "__main__":
    dossier_cible = input("Entrez le chemin du dossier à organiser : ")
    organiser_dossier(dossier_cible)
    print("Organisation terminée.")
