"""
Projet 3 — Gestionnaire de tâches (todo list)
Mini système de todo avec liste et dictionnaire.
Apprentissages : dictionnaires, boucles, fonctions, entrée utilisateur.
"""


# stockage des taches
tasks = {}
next_id = 1


def ajouter_tache(nom):
    # ajoute une tache dans le dico
    global next_id
    id = next_id
    tasks[id] = {"name": nom, "done": False}
    next_id = next_id + 1
    print(f"  / Tâche #{id} ajoutée : '{nom}'")
    return id


def marquer_faite(task_id):
    # marque une tache comme terminée
    trouve = False
    for id in tasks:
        if id == task_id:
            trouve = True
            break
    
    if trouve == False:
        print(f"  X Tâche #{task_id} introuvable.")
        return False
    
    tasks[task_id]["done"] = True
    print(f"  / Tâche #{task_id} marquée comme faite.")
    return True


def supprimer_tache(task_id):
    # supprime une tache du dico
    if task_id in tasks:
        nom = tasks[task_id]["name"]
        del tasks[task_id]
        print(f"Tâche #{task_id} supprimée : '{nom}'")
        return True
    else:
        print(f"  X Tâche #{task_id} introuvable.")
        return False


def afficher_taches():
    # affiche toutes les taches
    if len(tasks) == 0:
        print("\n  📭 Aucune tâche pour le moment.\n")
        return

    print("")
    print("=" * 45)
    print("       GESTIONNAIRE DE TÂCHES")
    print("=" * 45)
    
    liste_ids = list(tasks.keys())
    i = 0
    while i < len(liste_ids):
        tid = liste_ids[i]
        t = tasks[tid]
        if t["done"] == True:
            statut = "✔ Fait"
        else:
            statut = "◻ À faire"
        
        # formatage de l'affichage
        espace_id = str(tid)
        while len(espace_id) < 3:
            espace_id = " " + espace_id
        
        espace_statut = statut
        while len(espace_statut) < 10:
            espace_statut = " " + espace_statut
        
        print(f"  #{espace_id}  [{espace_statut}]  {t['name']}")
        i = i + 1
    
    print("=" * 45)

    # compter les taches faites
    faites = 0
    for cle in tasks:
        tache = tasks[cle]
        if tache["done"] == True:
            faites = faites + 1
    
    total = len(tasks)
    print(f"  Progression : {faites}/{total} tâches terminées")
    print("=" * 45)
    print("")


def afficher_menu():
    # menu principal
    print("\n--- MENU ---")
    print("  1. Afficher les tâches")
    print("  2. Ajouter une tâche")
    print("  3. Marquer une tâche comme faite")
    print("  4. Supprimer une tâche")
    print("  5. Quitter")
    print("------------")


def main():
    # quelques taches de demo au lancement
    ajouter_tache("Backup serveur")
    ajouter_tache("Update server")
    marquer_faite(2)
    ajouter_tache("Vérifier les logs")

    continuer = True
    while continuer:
        afficher_menu()
        choix = input("  Choix > ")
        choix = choix.strip()

        if choix == "1":
            afficher_taches()

        elif choix == "2":
            nom = input("Nom de la tâche > ")
            nom = nom.strip()
            if nom != "":
                ajouter_tache(nom)
            else:
                print("Nom vide, tâche non ajoutée.")

        elif choix == "3":
            afficher_taches()
            entree = input("ID de la tâche > ")
            try:
                tid = int(entree)
                marquer_faite(tid)
            except:
                print("ID invalide.")

        elif choix == "4":
            afficher_taches()
            entree = input("ID de la tâche > ")
            try:
                tid = int(entree)
                supprimer_tache(tid)
            except:
                print("ID invalide.")

        elif choix == "5":
            print("\nÀ bientôt !\n")
            continuer = False

        else:
            print("Choix invalide, réessaye.")


if __name__ == "__main__":
    main()
