le .env en local pour la securite
on va mettre a la place de .env le secret de github action pour mettre les valeurs dans le .env
dockerignore ne prend pas tous ce que vous mentionner dedans pour optimiser la charge de l'image
gitignore dit a git de pas suivre le fichier qui est mentionne dedans comme le node_modules en js et le py_cache en python
le docker compose file est destine pour le serveur de production mais pas avec le repo github.
la creation de workflows (steps : etapes a faire apres le push declencheur) test + build image + transfert d image vers le dockerhub et apres automatisation de deploiement vers le serveur de production via ssh ou vers le cloud(AWS , Azure ou googlecloud )
le docker construit l image a partir de l instruction dans le dockerfile, il va construire l image de mon code (mon propre code:app django)
dans le docker compose : on mentionne juste le mysql pour un nouvelle container car mysql a deja une image public,pas necessaire de le creer manuellement et l image de ton code personnel depuis le dockerhub
le container est comme une instance de votre image et le docker compose va lancer le container mysql et le django (chaque container est un processus isole mais ils utilisent le meme noyau que le hote)
Donc dans le processus,Image(app + system de fichier + OS leger(alpine) et toutes les dependandes qui sert a faire touner l app)