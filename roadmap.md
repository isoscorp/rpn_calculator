## Key features / maintenance
* enrichissement des stacks pour faciliter le monitoring
  * auteur
  * titre de la stack
  * date de création
  * date de la dernière opération
  * durée de vie
* possibilité de chercher une stack par titre, date de création
* suppression des stacks non utilisées
  * proposition : job quotidien (exemple : dag Airflow) pour supprimer les stacks en fonction 
    de la date de dernière opération ou de la durée de vie
* permettre de poster plusieurs opérations en 1 seule requête en assurant l'atomicité

## Securité
* gestion de l'authentification (à définir avec le projet)
  
## Devops
* créer une pipeline d'intégration continue :
  * qualité du code
  * validation du swagger
  * tests unitaires & d'intégration
* déploiement via docker
* scalabilité horizontale via Kubernetes par exemple
* réplication de la base de données
