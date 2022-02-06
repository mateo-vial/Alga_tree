def ajouter_branche(arbre, noeud_ind, sous_arbre):
    """
    Input
    -----
        arbre : arbre de départ sous forme de liste
        noeud_ind : liste d'indices pour arriver au noeud choisi
        sous_arbre : arbre à ajouter au noeud sous forme de liste

    Output
    ------
        pas d'output mdr

    Description
    -----------
        ajoute un sous-arbre à un noeud d'un arbre
    """

    # Se déplacer jusqu'au noeud
    arbre_ = arbre
    for i in noeud_ind:
        arbre_ = arbre_[i]

    # Ajouter le sous-arbre
    arbre_.append(sous_arbre)

def supprimer_branche(arbre, noeud_ind):
    """
    Input
    -----
        arbre : arbre de départ sous forme de liste
        noeud_ind : liste d'indices pour arriver au noeud choisi

    Output
    ------
        pas d'output mdr

    Description
    -----------
        Supprime un noeud d'un arbre
    """

    # On sépare le dernier indice car c'est comme ça qu'on delete
    noeud_ind, dernier_ind = noeud_ind[:-1], noeud_ind[-1]

    # Se déplacer jusqu'au noeud
    arbre_ = arbre
    for i in noeud_ind:
        arbre_ = arbre_[i]

    # Supprimer le noeud
    del arbre_[dernier_ind]