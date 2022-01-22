# projets-professionnels
Projet d'optimisation du nombre de lits pour des thrombectomies pour le CHU d'Angers.

Situation générale: La thrombose correspond à l'interruption de la circulation sanguine dans un vaisseau due à la formation d'un caillot dans ce même vaisseau. 
Les thromboses au niveau du muscle cardiaque correspondent à l'infarctus du myocarde et celles au niveau du cerveau à l'AVC.

Une façon de traiter ces pathologies est de détruire ou d'extraire le caillot sanguin: c'est une thrombectomie. 
Cependant, seuls certains hôpitaux sont habilités à effectuer ce geste. Ils correspondent la plupart du temps aux CHU, dans les unités de chirurgie vasculaire.

Néanmoins, ouvrir de tels lits coûtent cher, notamment en matériel, à l'installation d'abord et à l'entretien aussi. 
C'est pourquoi il est important pour un hôpital d'avoir un nombre suffisant de lit, afin de pouvoir gérer la demande au mieux, mais également de conserver ce nombre suffisamment
bas, pour des raisons évidentes de budget.

Dans le GHT (Groupement de Territoires Hospitaliers) qui nous intéresse, seuls les hôpitaux suivants peuvent prendre en charge une thrombectomie:
-'CHU Angers'
-'CHU Laval'
-'CHD La-Roche-sur-Yon'
-'CHU Nantes', 'CHU Rennes'
-'CHU Tours'
-'CHU Amboise-Chateau-Renault'

C'est dans ce contexte que s'inscrit l'algorithme suivant.

Les distances des différents hôpitaux entre eux sont représentées par la matrice des distances et l'algorithme s'appuie sur un phénomène de file d'attente avec fonction de "punition"
