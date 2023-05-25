import bdd

# Connexion à la base de données
database = r"bdd.db"
conn = bdd.create_connection(database)

# Création de genres
bdd.create_genre(conn, ("FICT", "Fiction générale"))
bdd.create_genre(conn, ("MYST/SUS", "Mystère et Suspense"))
bdd.create_genre(conn, ("ROM", "Romance"))
bdd.create_genre(conn, ("SF", "Science-fiction"))
bdd.create_genre(conn, ("BIO", "Biographie"))
bdd.create_genre(conn, ("HIST", "Histoire"))
bdd.create_genre(conn, ("POL", "Policier"))
bdd.create_genre(conn, ("DRAMA", "Drame"))
bdd.create_genre(conn, ("POE", "Poésie"))
bdd.create_genre(conn, ("CLAS", "Classique"))
bdd.create_genre(conn, ("JEUN", "Jeunesse"))
bdd.create_genre(conn, ("FANT", "Fantaisie"))
bdd.create_genre(conn, ("HIST", "Historique"))
bdd.create_genre(conn, ("PHILO", "Philosophie"))

# Création de thèmes
bdd.create_theme(conn, ("AMO", "Amour"))
bdd.create_theme(conn, ("AVE", "Aventure"))
bdd.create_theme(conn, ("FAM", "Famille"))
bdd.create_theme(conn, ("AMIT", "Amitié"))
bdd.create_theme(conn, ("SURV", "Survie"))
bdd.create_theme(conn, ("DEP", "Développement personnel"))
bdd.create_theme(conn, ("ENV", "Environnement"))
bdd.create_theme(conn, ("POLI", "Politique"))
bdd.create_theme(conn, ("HIST", "Histoire"))
bdd.create_theme(conn, ("SCI", "Science"))
bdd.create_theme(conn, ("FANT", "Fantaisie"))
bdd.create_theme(conn, ("HUM", "Humour"))
bdd.create_theme(conn, ("MYST", "Mystère"))
bdd.create_theme(conn, ("SOC", "Société"))
bdd.create_theme(conn, ("CUL", "Culture"))
bdd.create_theme(conn, ("VOY", "Voyage"))
bdd.create_theme(conn, ("IDENT", "Identité"))
bdd.create_theme(conn, ("RELIG", "Religion"))
bdd.create_theme(conn, ("PHIL", "Philosophie"))
bdd.create_theme(conn, ("ART", "Art"))

#Création de rayons
bdd.create_rayon(conn, ("FICT", "Fiction générale", 2))
bdd.create_rayon(conn, ("POE", "Poésie", 0))
bdd.create_rayon(conn, ("ROM", "Romance", 1))
bdd.create_rayon(conn, ("SF/FANT", "Science-fiction et Fantaisie", 3))
bdd.create_rayon(conn, ("BIO", "Biographie", 2))
bdd.create_rayon(conn, ("DRAMA", "Drame", 0))
bdd.create_rayon(conn, ("POL", "Policier", 1))
bdd.create_rayon(conn, ("CLAS", "Classique", 3))

#Création de document
document_id = bdd.create_document(conn, ("Le Seigneur des Anneaux", True, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "Dans un monde imaginaire, un jeune hobbit doit détruire un anneau maléfique pour sauver la Terre du Milieu.")
bdd.update_info_document(conn, document_id, "auteur", "J.R.R. Tolkien")

document_id = bdd.create_document(conn, ("Harry Potter à l'école des sorciers", True, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "Un jeune sorcier découvre qu'il est le célèbre Harry Potter et qu'il a été accepté à Poudlard, une école de magie.")
bdd.update_info_document(conn, document_id, "auteur", "J.K. Rowling")

document_id = bdd.create_document(conn, ("Le Petit Prince", False, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "Un jeune prince voyageur partage ses expériences sur différentes planètes avec un pilote échoué dans le désert.")
bdd.update_info_document(conn, document_id, "auteur", "Antoine de Saint-Exupéry")

document_id = bdd.create_document(conn, ("Les Misérables", False, "DRAMA"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'un ancien forçat cherchant la rédemption dans une France tourmentée par les révolutions.")
bdd.update_info_document(conn, document_id, "auteur", "Victor Hugo")

document_id = bdd.create_document(conn, ("Orgueil et Préjugés", True, "ROM"))
bdd.update_info_document(conn, document_id, "description", "Dans l'Angleterre du XIXe siècle, l'histoire d'amour compliquée entre Elizabeth Bennet et Mr. Darcy.")
bdd.update_info_document(conn, document_id, "auteur", "Jane Austen")

document_id = bdd.create_document(conn, ("Crime et Châtiment", True, "DRAMA"))
bdd.update_info_document(conn, document_id, "description", "Un étudiant en droit commet un meurtre et est tourmenté par sa conscience dans la Russie impériale.")
bdd.update_info_document(conn, document_id, "auteur", "Fyodor Dostoevsky")

document_id = bdd.create_document(conn, ("Le Comte de Monte-Cristo", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'Edmond Dantès, un homme injustement emprisonné qui cherche à se venger de ceux qui l'ont trahi.")
bdd.update_info_document(conn, document_id, "auteur", "Alexandre Dumas")

document_id = bdd.create_document(conn, ("Les Quatre Filles du docteur March", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire des sœurs March, Meg, Jo, Beth et Amy, pendant la guerre de Sécession aux États-Unis.")
bdd.update_info_document(conn, document_id, "auteur", "Louisa May Alcott")

document_id = bdd.create_document(conn, ("Le Nom de la Rose", True, "POL"))
bdd.update_info_document(conn, document_id, "description", "Dans un monastère médiéval, un moine franciscain enquête sur une série de meurtres mystérieux.")
bdd.update_info_document(conn, document_id, "auteur", "Umberto Eco")

document_id = bdd.create_document(conn, ("Le Parfum", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'un homme doté d'un sens olfactif extraordinaire qui cherche à créer le parfum ultime en utilisant des méthodes sinistres.")
bdd.update_info_document(conn, document_id, "auteur", "Patrick Süskind")

document_id = bdd.create_document(conn, ("Les Trois Mousquetaires", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les aventures d'un jeune homme nommé d'Artagnan qui aspire à devenir mousquetaire du roi.")
bdd.update_info_document(conn, document_id, "auteur", "Alexandre Dumas")

document_id = bdd.create_document(conn, ("L'Étranger", False, "DRAMA"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'un homme indifférent à tout ce qui l'entoure, jusqu'à ce qu'un événement tragique bouleverse sa vie.")
bdd.update_info_document(conn, document_id, "auteur", "Albert Camus")

document_id = bdd.create_document(conn, ("Moby Dick", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'obsession d'un capitaine pour la chasse à la baleine blanche légendaire, Moby Dick.")
bdd.update_info_document(conn, document_id, "auteur", "Herman Melville")

document_id = bdd.create_document(conn, ("L'Odyssée", True, "CLAS"))
bdd.update_info_document(conn, document_id, "description", "Le récit des aventures d'Ulysse lors de son voyage de retour vers Ithaque après la guerre de Troie.")
bdd.update_info_document(conn, document_id, "auteur", "Homer")

document_id = bdd.create_document(conn, ("Le Rouge et le Noir", False, "CLAS"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'un jeune homme ambitieux nommé Julien Sorel qui gravit les échelons de la société.")
bdd.update_info_document(conn, document_id, "auteur", "Stendhal")

document_id = bdd.create_document(conn, ("Don Quichotte", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les aventures comiques d'un chevalier obsédé par les romans de chevalerie et de son fidèle écuyer, Sancho Panza.")
bdd.update_info_document(conn, document_id, "auteur", "Miguel de Cervantes")

document_id = bdd.create_document(conn, ("Anna Karenina", True, "ROM"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'Anna Karenina, une femme mariée qui succombe à une passion amoureuse qui bouleverse sa vie.")
bdd.update_info_document(conn, document_id, "auteur", "Leo Tolstoy")

document_id = bdd.create_document(conn, ("Les Fleurs du Mal", True, "POES"))
bdd.update_info_document(conn, document_id, "description", "Recueil de poèmes qui explore les thèmes de la beauté, de la sensualité et de la mort.")
bdd.update_info_document(conn, document_id, "auteur", "Charles Baudelaire")

document_id = bdd.create_document(conn, ("Guerre et Paix", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Un vaste roman épique qui suit les destins de plusieurs personnages pendant les guerres napoléoniennes.")
bdd.update_info_document(conn, document_id, "auteur", "Leo Tolstoy")

document_id = bdd.create_document(conn, ("Les Hauts de Hurlevent", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Une histoire de passion intense et de vengeance dans les landes sauvages du Yorkshire.")
bdd.update_info_document(conn, document_id, "auteur", "Emily Brontë")

document_id = bdd.create_document(conn, ("Le Journal d'Anne Frank", True, "BIO"))
bdd.update_info_document(conn, document_id, "description", "Les écrits intimes d'Anne Frank, une jeune fille juive cachée pendant l'occupation nazie des Pays-Bas.")
bdd.update_info_document(conn, document_id, "auteur", "Anne Frank")

document_id = bdd.create_document(conn, ("Les Aventures de Tom Sawyer", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les aventures d'un jeune garçon espiègle et débrouillard dans le Mississippi du XIXe siècle.")
bdd.update_info_document(conn, document_id, "auteur", "Mark Twain")

document_id = bdd.create_document(conn, ("Vingt mille lieues sous les mers", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Le capitaine Nemo et son sous-marin Nautilus embarquent pour des aventures sous-marines incroyables.")
bdd.update_info_document(conn, document_id, "auteur", "Jules Verne")

document_id = bdd.create_document(conn, ("Le Petit Nicolas", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les histoires amusantes et espiègles d'un jeune garçon nommé Nicolas et de ses camarades de classe.")
bdd.update_info_document(conn, document_id, "auteur", "René Goscinny")

document_id = bdd.create_document(conn, ("Les Piliers de la Terre", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire de la construction d'une cathédrale au XIIe siècle, avec des complots, des amours interdites et des luttes de pouvoir.")
bdd.update_info_document(conn, document_id, "auteur", "Ken Follett")

document_id = bdd.create_document(conn, ("Le Portrait de Dorian Gray", True, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "Un jeune homme vend son âme pour conserver sa jeunesse éternelle, tandis que son portrait vieillit et reflète ses actes immoraux.")
bdd.update_info_document(conn, document_id, "auteur", "Oscar Wilde")

document_id = bdd.create_document(conn, ("Le Silence des Agneaux", False, "THRILL"))
bdd.update_info_document(conn, document_id, "description", "Un jeune agent du FBI fait équipe avec un psychopathe cannibale emprisonné pour attraper un tueur en série.")
bdd.update_info_document(conn, document_id, "auteur", "Thomas Harris")

document_id = bdd.create_document(conn, ("Les Raisins de la colère", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'une famille de fermiers touchée par la Grande Dépression et leur voyage vers la Californie en quête d'une vie meilleure.")
bdd.update_info_document(conn, document_id, "auteur", "John Steinbeck")

document_id = bdd.create_document(conn, ("Les Aventures d'Alice au pays des merveilles", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Une petite fille nommée Alice tombe dans un terrier de lapin et se retrouve dans un monde fantastique rempli de créatures étranges.")
bdd.update_info_document(conn, document_id, "auteur", "Lewis Carroll")

document_id = bdd.create_document(conn, ("Le Guépard", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'une famille noble en Sicile au moment du Risorgimento italien et de ses luttes pour maintenir son statut et son influence.")
bdd.update_info_document(conn, document_id, "auteur", "Giuseppe Tomasi di Lampedusa")

document_id = bdd.create_document(conn, ("Le Journal de Bridget Jones", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les tribulations hilarantes d'une jeune femme à la recherche de l'amour et de l'épanouissement personnel.")
bdd.update_info_document(conn, document_id, "auteur", "Helen Fielding")

document_id = bdd.create_document(conn, ("L'Alchimiste", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Un jeune berger entreprend un voyage à la recherche de son trésor personnel et découvre des leçons spirituelles sur son chemin.")
bdd.update_info_document(conn, document_id, "auteur", "Paulo Coelho")

document_id = bdd.create_document(conn, ("Cent ans de solitude", True, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire de la famille Buendía sur plusieurs générations, dans un village isolé où se mêlent réalité et magie.")
bdd.update_info_document(conn, document_id, "auteur", "Gabriel García Márquez")

document_id = bdd.create_document(conn, ("1984", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Un monde dystopique où la surveillance constante et le contrôle totalitaire régissent la vie des individus.")
bdd.update_info_document(conn, document_id, "auteur", "George Orwell")

document_id = bdd.create_document(conn, ("Barbe Bleue", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Une jeune fille se retrouve en colocation avec un mysterieux propriétaire.")
bdd.update_info_document(conn, document_id, "auteur", "Amélie Nothomb")

document_id = bdd.create_document(conn, ("Bonne Nuit Punpun 1", False, "DRAMA"))
bdd.update_info_document(conn, document_id, "description", "L'histoire de Punpun, un garçon livrant sa situation familiale bancale, puis abordant son premier amour, décrivant son entourage, tout en traversant le début de son adolescence pensée par son esprit plus ou moins hyperactif, sur plusieurs années de sa vie.")
bdd.update_info_document(conn, document_id, "auteur", "Inio Asano")

document_id = bdd.create_document(conn, ("Où est Charlie", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Amusez vous pendant des heures avec ce classique du livre de divertissement !")

# Atttribution de genres aux documents
bdd.link_document_genre(conn, 1, "FANT")
bdd.link_document_genre(conn, 2, "FANT")
bdd.link_document_genre(conn, 3, "CLAS")
bdd.link_document_genre(conn, 4, "CLAS")
bdd.link_document_genre(conn, 5, "ROM")
bdd.link_document_genre(conn, 6, "DRAMA")
bdd.link_document_genre(conn, 7, "CLAS")
bdd.link_document_genre(conn, 8, "FICT")
bdd.link_document_genre(conn, 9, "POL")
bdd.link_document_genre(conn, 10, "FICT")
bdd.link_document_genre(conn, 11, "CLAS")
bdd.link_document_genre(conn, 12, "FICT")
bdd.link_document_genre(conn, 13, "CLAS")
bdd.link_document_genre(conn, 14, "FANT")
bdd.link_document_genre(conn, 15, "CLAS")
bdd.link_document_genre(conn, 16, "CLAS")
bdd.link_document_genre(conn, 17, "ROM")
bdd.link_document_genre(conn, 18, "POES")
bdd.link_document_genre(conn, 19, "HIST")
bdd.link_document_genre(conn, 20, "MYST/SUS")
bdd.link_document_genre(conn, 21, "HIST")
bdd.link_document_genre(conn, 22, "JEUN")
bdd.link_document_genre(conn, 23, "CLAS")
bdd.link_document_genre(conn, 24, "JEUN")
bdd.link_document_genre(conn, 25, "MYST/SUS")
bdd.link_document_genre(conn, 26, "POL")
bdd.link_document_genre(conn, 27, "HIST")
bdd.link_document_genre(conn, 28, "FANT")
bdd.link_document_genre(conn, 29, "HIST")
bdd.link_document_genre(conn, 30, "ROM")
bdd.link_document_genre(conn, 31, "FICT")
bdd.link_document_genre(conn, 32, "FANT")
bdd.link_document_genre(conn, 33, "CLAS")
bdd.link_document_genre(conn, 34, "FICT")
bdd.link_document_genre(conn, 35, "DRAMA")
bdd.link_document_genre(conn, 36, "JEUN")

# Attribution de thèmes aux documents