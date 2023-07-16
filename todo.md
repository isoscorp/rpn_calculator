## Cleanup / code quality
* utiliser mypy pour le check des annotations
* utiliser un linter pour le formattage automatique, black par exemple
* déplacer la logique des opérations dans la classe Stack

## Gestion des erreurs
* gérer les opérations sur les nombres à virgule + précision des décimales
* gérer les erreurs (opérations interdites, opérandes insuffisants dans la stack)
* gérer les accès concurrents aux stacks : utiliser un lock à chaque opération sur une stack

## Testing
* tester unitairement les opérations, en particulier la non commutativité pour la soustraction / division
* rédiger un test d'intégration pour le cas nominal
  
## Maintenabilité
* remplacer flask-restplus par une librairie maintenue (flask-restx ?)
* gérer les migrations sql (manage_db.py reset la base) : utiliser alembic par exemple