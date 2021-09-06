**Automatisation de renouvellement de certificat  SSL avec let's encrypt**
1. Inventaire des serveurs (distribution linux redhat,debian, centos, ubuntu)
2. Inventaire des serveurs web installé (apache, nginx et tomcat)
3. Vérification des fichiers de conf des serveurs web
4. Installation de Certbot sur serveur dédié pour permettre la demande du certificat wildcard au nom du domaine 
5. Création du  fichier de configuration contenant les identifiants de l'API OVH afin d'automatiser le processus de réalisation d'un challenge DNS01 en créant puis en supprimant des enregistrements TXT à l'aide de l'API OVH
6. Planification de la génération et du renouvellement des certificats let's encrypt avec crontab 
7. Création d'un partage avec les certificat et montage du nouveau partage sur les serveurs web pour éviter de redistribuer les certificats
8. Redémarrage du service sur chaque serveur web
9. Rédaction de la documentation qui explique les differentes étapes de la réalisation du projet


