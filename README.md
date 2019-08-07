# ARA v1

Le docker compose pour ara v1 consiste pour le moment en 3 images :
- une image postgres pour la base de donnée qui expose le port **5432**
- l'api qui est une image alpine avec django et ara[server] qui expose le port **9006**
- un front JS basé sur un image nginx:alpine qui expose le port **9007**

- Par défaut en suivant la procédure l'api est accèssible sur l'url <http://localhost:9006>.
- Il est possible d'accéder à l'administration par l'url <http://localhost:9006/admin/>.
Par défaut le user admin est : eul/eul.
- Le user pour renseigner les élements depuis l'execution des playbooks a été créé par le script createsuperuser. Par défaut le user est : ansible/ansible.
- Le front a besoin de connaître l'url de l'api. Pour cela il faut resneigner le fichier **config.json** avec ces informations à l'execution du conteneur.

## TODO

- Pour le moment le volume de la base de donnée n'est pas monté.
- Il faudra pouvoir paramétrer les ports d'écoute.
- Il faudrait reflechir à un meilleur moyen d'amorcer la base django (cf ci-dessous)
- Ajouter un middleware à djang pour gérer le trailing slash dans les urls. Actuellement le / est obligatoire à la fin des urls.
- Améliorer et compléter le front.
- Mieux gérer la clé de chiffrement de django (cf fichier settings.yaml)

## Construction

```sh
$ docker-compose build
$ docker-compose up
```

## Initialisation de la base de donnée

```sh
# Accès conteneur de l'api
$ docker exec -it $(docker ps | grep ara_v1_ara-api | awk '{print $1}') /bin/sh
# Mise à jour de la base de donnée
~ ara-manage migrate
# Création du super user et du user ansible (il faudra reset les mots de passe)
~ cat createsuperuser.py | ara-manage shell
```

## Activation des callbacks ara sur le master ansible

```sh
source <(python3 -m ara.setup.env)
```
