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
bdd.create_theme(conn, ("CULT", "Culture"))
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
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.leslibraires.ca%2Fbooks%2F9782266201728%2Ffront%2F9782266201728_large.jpg%3Fv%3D58879&f=1&nofb=1&ipt=0db71546b30c7804a45c066f3016fe2a75d70916f6356bb3aedbf89322cd25b1&ipo=images")

document_id = bdd.create_document(conn, ("Harry Potter à l'école des sorciers", True, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "Un jeune sorcier découvre qu'il est le célèbre Harry Potter et qu'il a été accepté à Poudlard, une école de magie.")
bdd.update_info_document(conn, document_id, "auteur", "J.K. Rowling")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fec56229aec51f1baff1d-185c3068e22352c56024573e929788ff.ssl.cf1.rackcdn.com%2Fattachments%2Flarge%2F2%2F2%2F4%2F005453224.jpg&f=1&nofb=1&ipt=a0b9886015b1b768d9d3130221f7d851911daeebaee3531ba3f951df069e8f12&ipo=images")

document_id = bdd.create_document(conn, ("Le Petit Prince", False, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "Un jeune prince voyageur partage ses expériences sur différentes planètes avec un pilote échoué dans le désert.")
bdd.update_info_document(conn, document_id, "auteur", "Antoine de Saint-Exupéry")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F2.bp.blogspot.com%2F-6F9tw-WV26o%2FVhIifSTNyEI%2FAAAAAAAABEI%2FOIBHzZ_dH6Y%2Fs1600%2Fle_petit_prince_1.jpg&f=1&nofb=1&ipt=8a06fab6cab2ab5fae8e651310083ee79772933594bfd08670eb73f47493d6ef&ipo=images")

document_id = bdd.create_document(conn, ("Les Misérables", False, "DRAMA"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'un ancien forçat cherchant la rédemption dans une France tourmentée par les révolutions.")
bdd.update_info_document(conn, document_id, "auteur", "Victor Hugo")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fec56229aec51f1baff1d-185c3068e22352c56024573e929788ff.ssl.cf1.rackcdn.com%2Fattachments%2Flarge%2F0%2F4%2F9%2F003116049.jpg&f=1&nofb=1&ipt=c04beb17dfdbecf89d0d8f416439513158f34455f2a4d8d9651e6cd049c4721c&ipo=images")

document_id = bdd.create_document(conn, ("Orgueil et Préjugés", True, "ROM"))
bdd.update_info_document(conn, document_id, "description", "Dans l'Angleterre du XIXe siècle, l'histoire d'amour compliquée entre Elizabeth Bennet et Mr. Darcy.")
bdd.update_info_document(conn, document_id, "auteur", "Jane Austen")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.livredepoche.com%2Fsites%2Fdefault%2Ffiles%2Fimages%2Flivres%2Fcouv%2F9782253088905-001-T.jpeg&f=1&nofb=1&ipt=dec946d4aacab0d8c6f7c98700a543a4e31ccd1d03979034ed9f531aead2fb18&ipo=images")

document_id = bdd.create_document(conn, ("Crime et Châtiment", True, "DRAMA"))
bdd.update_info_document(conn, document_id, "description", "Un étudiant en droit commet un meurtre et est tourmenté par sa conscience dans la Russie impériale.")
bdd.update_info_document(conn, document_id, "auteur", "Fyodor Dostoevsky")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.senscritique.com%2Fmedia%2F000020002515%2Fsource_big%2Fcrime_et_chatiment.jpg&f=1&nofb=1&ipt=d17d76e569683a2743eff2f1f85a968dde87b98af200b897fabc984dd1932d80&ipo=images")

document_id = bdd.create_document(conn, ("Le Comte de Monte-Cristo", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'Edmond Dantès, un homme injustement emprisonné qui cherche à se venger de ceux qui l'ont trahi.")
bdd.update_info_document(conn, document_id, "auteur", "Alexandre Dumas")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.livredepochejeunesse.com%2Flocal%2Fcache-vignettes%2FL550xH783%2Farton2663-ab623.jpg%3F1632033902&f=1&nofb=1&ipt=db5341e99eba540915263f16bacfa88e2a088d57399299e8d67c4b51e47401fb&ipo=images")

document_id = bdd.create_document(conn, ("Les Quatre Filles du docteur March", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire des sœurs March, Meg, Jo, Beth et Amy, pendant la guerre de Sécession aux États-Unis.")
bdd.update_info_document(conn, document_id, "auteur", "Louisa May Alcott")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.123loisirs.com%2Fimages%2Fquatre_filles_march.jpg&f=1&nofb=1&ipt=ba23d15e2c9021829d8430945486165c7f7641ae0f5c8419a9172e41c76e22f3&ipo=images")

document_id = bdd.create_document(conn, ("Le Nom de la Rose", True, "POL"))
bdd.update_info_document(conn, document_id, "description", "Dans un monastère médiéval, un moine franciscain enquête sur une série de meurtres mystérieux.")
bdd.update_info_document(conn, document_id, "auteur", "Umberto Eco")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.livredepoche.com%2Fsites%2Fdefault%2Ffiles%2Fimages%2Flivres%2Fcouv%2F9782253033134-001-T.jpeg&f=1&nofb=1&ipt=ffcf9353124defe91baf8b2af2d78534b42d026f217dc684474c442107054444&ipo=images")

document_id = bdd.create_document(conn, ("Le Parfum", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'un homme doté d'un sens olfactif extraordinaire qui cherche à créer le parfum ultime en utilisant des méthodes sinistres.")
bdd.update_info_document(conn, document_id, "auteur", "Patrick Süskind")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Flesmotsalabouche.com%2Fwp-content%2Fuploads%2F2021%2F04%2Fparfum6-1280x2054.jpg&f=1&nofb=1&ipt=2001208c62c2891ba637c2b1cb9c55633125f2cecca46d318f380ccdfbdb2663&ipo=images")

document_id = bdd.create_document(conn, ("Les Trois Mousquetaires", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les aventures d'un jeune homme nommé d'Artagnan qui aspire à devenir mousquetaire du roi.")
bdd.update_info_document(conn, document_id, "auteur", "Alexandre Dumas")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.w2VcImTjLQiqh5OyhWu_9QHaKF%26pid%3DApi&f=1&ipt=cd56450917ecd8c9ab00114894cef2831be6cf327b51724123f87e93ca15feed&ipo=images")

document_id = bdd.create_document(conn, ("L'Étranger", False, "DRAMA"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'un homme indifférent à tout ce qui l'entoure, jusqu'à ce qu'un événement tragique bouleverse sa vie.")
bdd.update_info_document(conn, document_id, "auteur", "Albert Camus")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.senscritique.com%2Fmedia%2F000004679110%2Fsource_big%2FL_Etranger.jpg&f=1&nofb=1&ipt=1ea9357aefa9852080377ac26076b1fe8a750ea3436687c1d9d6055f881f2273&ipo=images")

document_id = bdd.create_document(conn, ("Moby Dick", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'obsession d'un capitaine pour la chasse à la baleine blanche légendaire, Moby Dick.")
bdd.update_info_document(conn, document_id, "auteur", "Herman Melville")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.senscritique.com%2Fmedia%2F000019481669%2Fsource_big%2FMoby_Dick.jpg&f=1&nofb=1&ipt=6b2ffdfb8b30ab49c3542c96cc63fec808317464405b51853b8420e7d7d8bed8&ipo=images")

document_id = bdd.create_document(conn, ("L'Odyssée", True, "CLAS"))
bdd.update_info_document(conn, document_id, "description", "Le récit des aventures d'Ulysse lors de son voyage de retour vers Ithaque après la guerre de Troie.")
bdd.update_info_document(conn, document_id, "auteur", "Homère")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.mten3giRAWryyOUz2hmw-QHaKp%26pid%3DApi&f=1&ipt=b5b9dd1c7da33fe9df79c85779978dac7f92fba9f5368904a34434f7aeb851dc&ipo=images")

document_id = bdd.create_document(conn, ("Le Rouge et le Noir", False, "CLAS"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'un jeune homme ambitieux nommé Julien Sorel qui gravit les échelons de la société.")
bdd.update_info_document(conn, document_id, "auteur", "Stendhal")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.livraddict.com%2Fcovers%2F343%2F343811%2Fcouv3306187.jpg&f=1&nofb=1&ipt=6ae5903278c91f5cfdcd9afda66897c8fc65f13afb9b4eddfae4d834919447c0&ipo=images")

document_id = bdd.create_document(conn, ("Don Quichotte", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les aventures comiques d'un chevalier obsédé par les romans de chevalerie et de son fidèle écuyer, Sancho Panza.")
bdd.update_info_document(conn, document_id, "auteur", "Miguel de Cervantes")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.images-chapitre.com%2Fima1%2Foriginal%2F467%2F66532467_13884384.jpg&f=1&nofb=1&ipt=3a79cb0256d1d906e57ecf5c3592c98bce75a50f15d3b03451c2827edc62085b&ipo=images")

document_id = bdd.create_document(conn, ("Anna Karenina", True, "ROM"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'Anna Karenina, une femme mariée qui succombe à une passion amoureuse qui bouleverse sa vie.")
bdd.update_info_document(conn, document_id, "auteur", "Leo Tolstoy")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Falessandria.bookrepublic.it%2Fapi%2Fbooks%2F9788811137689%2Fcover&f=1&nofb=1&ipt=b1cd1b2cf6e0d42fba6c41c71f0d224e016dcc9c247467be9b81145f207c8eac&ipo=images")

document_id = bdd.create_document(conn, ("Les Fleurs du Mal", True, "POES"))
bdd.update_info_document(conn, document_id, "description", "Recueil de poèmes qui explore les thèmes de la beauté, de la sensualité et de la mort.")
bdd.update_info_document(conn, document_id, "auteur", "Charles Baudelaire")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fec56229aec51f1baff1d-185c3068e22352c56024573e929788ff.ssl.cf1.rackcdn.com%2Fattachments%2Flarge%2F0%2F9%2F9%2F001069099.jpg&f=1&nofb=1&ipt=4c22a2e0ec6b9179fbc165ba83410ef9a1a64183143e8071e705cbbd100b2f39&ipo=images")

document_id = bdd.create_document(conn, ("Guerre et Paix", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Un vaste roman épique qui suit les destins de plusieurs personnages pendant les guerres napoléoniennes.")
bdd.update_info_document(conn, document_id, "auteur", "Leo Tolstoy")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimgv2-2-f.scribdassets.com%2Fimg%2Fword_document%2F408283566%2Foriginal%2Feaaf62d97b%2F1602733215%3Fv%3D1&f=1&nofb=1&ipt=0f4040b369e8ae1b665873a70b2fdd4b6cfddb2b01caae9c9e4973837999f961&ipo=images")

document_id = bdd.create_document(conn, ("Les Hauts de Hurlevent", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Une histoire de passion intense et de vengeance dans les landes sauvages du Yorkshire.")
bdd.update_info_document(conn, document_id, "auteur", "Emily Brontë")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.uaGCIwnEYgUJmz4W7EXmxAHaL_%26pid%3DApi&f=1&ipt=87cbb500b97eaf1a446c88f9bcf59f1d49bbebc9d16cfc09ac9505440e140577&ipo=images")

document_id = bdd.create_document(conn, ("Le Journal d'Anne Frank", True, "BIO"))
bdd.update_info_document(conn, document_id, "description", "Les écrits intimes d'Anne Frank, une jeune fille juive cachée pendant l'occupation nazie des Pays-Bas.")
bdd.update_info_document(conn, document_id, "auteur", "Anne Frank")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.decitre.fr%2Fmedia%2Fcatalog%2Fproduct%2F9%2F7%2F8%2F2%2F2%2F5%2F3%2F0%2F9782253001270FS.gif&f=1&nofb=1&ipt=fa14dff7ccc146577492a1996c2f95638a1f4db709b01b1f51732254ba7026cd&ipo=images")

document_id = bdd.create_document(conn, ("Les Aventures de Tom Sawyer", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les aventures d'un jeune garçon espiègle et débrouillard dans le Mississippi du XIXe siècle.")
bdd.update_info_document(conn, document_id, "auteur", "Mark Twain")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fec56229aec51f1baff1d-185c3068e22352c56024573e929788ff.ssl.cf1.rackcdn.com%2Fattachments%2Flarge%2F7%2F4%2F7%2F004790747.jpg&f=1&nofb=1&ipt=3cbd4cc133ab4b68cab05ea68974e29a2aec166879cae22ce5c81ea7d953976c&ipo=images")

document_id = bdd.create_document(conn, ("Vingt mille lieues sous les mers", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Le capitaine Nemo et son sous-marin Nautilus embarquent pour des aventures sous-marines incroyables.")
bdd.update_info_document(conn, document_id, "auteur", "Jules Verne")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.livredepochejeunesse.com%2Flocal%2Fcache-vignettes%2FL550xH783%2Farton2922-3fc84.jpg&f=1&nofb=1&ipt=d670940b930123dc9c28d404881166ca7d8bb3ea291b7127f6474bbba50d6c14&ipo=images")

document_id = bdd.create_document(conn, ("Le Petit Nicolas", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les histoires amusantes et espiègles d'un jeune garçon nommé Nicolas et de ses camarades de classe.")
bdd.update_info_document(conn, document_id, "auteur", "René Goscinny")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F71Qf8yHrNsL.jpg&f=1&nofb=1&ipt=38b4344414bf1c7334a16d9a3c4bdaed7c514bc786692cfb07b0ecf833bfd252&ipo=images")

document_id = bdd.create_document(conn, ("Les Piliers de la Terre", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire de la construction d'une cathédrale au XIIe siècle, avec des complots, des amours interdites et des luttes de pouvoir.")
bdd.update_info_document(conn, document_id, "auteur", "Ken Follett")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.livredepoche.com%2Fsites%2Fdefault%2Ffiles%2Fimages%2Flivres%2Fcouv%2F9782253059530-001-T.jpeg&f=1&nofb=1&ipt=5a9837acc50836ba6520a4f90d71fedbfa46bfb4d61c6ab753b8bd8414f434b1&ipo=images")

document_id = bdd.create_document(conn, ("Le Portrait de Dorian Gray", True, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "Un jeune homme vend son âme pour conserver sa jeunesse éternelle, tandis que son portrait vieillit et reflète ses actes immoraux.")
bdd.update_info_document(conn, document_id, "auteur", "Oscar Wilde")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.livredepoche.com%2Fsites%2Fdefault%2Ffiles%2Fimages%2Flivres%2Fcouv%2F9782253002888-001-T.jpeg&f=1&nofb=1&ipt=a504d17c0cba92c72209f015f4fa4294e879e2ed28e24bf313ef7e7612b5ccc7&ipo=images")

document_id = bdd.create_document(conn, ("Le Silence des Agneaux", False, "THRILL"))
bdd.update_info_document(conn, document_id, "description", "Un jeune agent du FBI fait équipe avec un psychopathe cannibale emprisonné pour attraper un tueur en série.")
bdd.update_info_document(conn, document_id, "auteur", "Thomas Harris")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fmedia.senscritique.com%2Fmedia%2F000000101689%2Fsource_big%2FLe_Silence_des_agneaux.jpg&f=1&nofb=1&ipt=eaf0f427b322728719a8dac18a4734e8262cea6e5f94702cc5a2444562ae0683&ipo=images")

document_id = bdd.create_document(conn, ("Les Raisins de la colère", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'une famille de fermiers touchée par la Grande Dépression et leur voyage vers la Californie en quête d'une vie meilleure.")
bdd.update_info_document(conn, document_id, "auteur", "John Steinbeck")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.onlalu.com%2Fwp-content%2Fuploads%2Fcouvs%2F33%2F9782070360833.jpg&f=1&nofb=1&ipt=4782257efd5757a4d223bfec0ab6eb9d296591e68150353ab4c0590b311d83a4&ipo=images")

document_id = bdd.create_document(conn, ("Les Aventures d'Alice au pays des merveilles", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Une petite fille nommée Alice tombe dans un terrier de lapin et se retrouve dans un monde fantastique rempli de créatures étranges.")
bdd.update_info_document(conn, document_id, "auteur", "Lewis Carroll")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.explicit.bing.net%2Fth%3Fid%3DOIP.Z3qgeDbT40KL2vEEIsMyfAC1Es%26pid%3DApi&f=1&ipt=45b83187701089058f0496ba4ae3600d9b247bb9b8a4756ba0e8d8858bf53ba4&ipo=images")

document_id = bdd.create_document(conn, ("Le Guépard", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire d'une famille noble en Sicile au moment du Risorgimento italien et de ses luttes pour maintenir son statut et son influence.")
bdd.update_info_document(conn, document_id, "auteur", "Giuseppe Tomasi di Lampedusa")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.F2_7lWeaNPsHiUV1Y9igXAHaKX%26pid%3DApi&f=1&ipt=2340820378f477147a98959fff6c1220c441f5d4b711f41ff3157e79b2c15b7c&ipo=images")

document_id = bdd.create_document(conn, ("Le Journal de Bridget Jones", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Les tribulations hilarantes d'une jeune femme à la recherche de l'amour et de l'épanouissement personnel.")
bdd.update_info_document(conn, document_id, "auteur", "Helen Fielding")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F3.bp.blogspot.com%2F-C2hdWY54lKw%2FTy0mtMBbZvI%2FAAAAAAAACjU%2F_rOS6Gyfh20%2Fs1600%2FLe%2Bjournal%2Bde%2BBridget%2BJones.jpg&f=1&nofb=1&ipt=5c93da55ca70e431b81da4d7e65341fad9db66b852595dd39ac97b08e3161511&ipo=images")

document_id = bdd.create_document(conn, ("L'Alchimiste", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Un jeune berger entreprend un voyage à la recherche de son trésor personnel et découvre des leçons spirituelles sur son chemin.")
bdd.update_info_document(conn, document_id, "auteur", "Paulo Coelho")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fservimg.eyrolles.com%2Fstatic%2Fmedia%2F4704%2F9782081394704_internet_h1400.jpg&f=1&nofb=1&ipt=a23e390201c67b5a66ae9724bdaa0765880b39c7b6fe7a7f033b7db0cf1b72d4&ipo=images")

document_id = bdd.create_document(conn, ("Cent ans de solitude", True, "SF/FANT"))
bdd.update_info_document(conn, document_id, "description", "L'histoire de la famille Buendía sur plusieurs générations, dans un village isolé où se mêlent réalité et magie.")
bdd.update_info_document(conn, document_id, "auteur", "Gabriel García Márquez")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fimages.leslibraires.ca%2Fbooks%2F9782020238113%2Ffront%2F9782020238113_large.jpg&f=1&nofb=1&ipt=6342e26469e83a05d9a398ae119f52e9012ca929a71b23ea4c8ebba79d521c88&ipo=images")

document_id = bdd.create_document(conn, ("1984", True, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Un monde dystopique où la surveillance constante et le contrôle totalitaire régissent la vie des individus.")
bdd.update_info_document(conn, document_id, "auteur", "George Orwell")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F0d%2F2c%2F09%2F0d2c0915b3c86c8ac0680f3f6c88731d.jpg&f=1&nofb=1&ipt=62414ae33a9e6541a49f75dd23039ec8cbca7c12f2ec3bb06f580c43375f2611&ipo=images")

document_id = bdd.create_document(conn, ("Barbe Bleue", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Une jeune fille se retrouve en colocation avec un mysterieux propriétaire.")
bdd.update_info_document(conn, document_id, "auteur", "Amélie Nothomb")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.images-chapitre.com%2Fima1%2Foriginal%2F498%2F59955498_11515594.jpg&f=1&nofb=1&ipt=8facc0a036cb709032da2368a6b5caef31ad534bb64e44c7ff1a384d53c67643&ipo=images")

document_id = bdd.create_document(conn, ("Bonne Nuit Punpun t.1", False, "DRAMA"))
bdd.update_info_document(conn, document_id, "description", "L'histoire de Punpun, un garçon livrant sa situation familiale bancale, puis abordant son premier amour, décrivant son entourage, tout en traversant le début de son adolescence pensée par son esprit plus ou moins hyperactif, sur plusieurs années de sa vie.")
bdd.update_info_document(conn, document_id, "auteur", "Inio Asano")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.senscritique.com%2Fmedia%2F000017700707%2Fsource_big%2FBonne_nuit_Punpun_tome_1.jpg&f=1&nofb=1&ipt=dc25233a1314554eafcb3c92877f4e359107d6b9d92faa677fa3cc64a932bf17&ipo=images")

document_id = bdd.create_document(conn, ("Où est Charlie", False, "FICT"))
bdd.update_info_document(conn, document_id, "description", "Amusez vous pendant des heures avec ce classique du livre de divertissement !")
bdd.update_info_document(conn, document_id, "liencouverture", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fsecure.sogides.com%2Fpublic%2Fproduits%2F9782%2F324%2F006%2Fgr_9782324006555.jpg&f=1&nofb=1&ipt=83dcc8a3def685349bcf8f33abbf8d5935ebfae73735242f933e3b6919615c82&ipo=images")

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
bdd.link_document_theme(conn, 1, "FANT")
bdd.link_document_theme(conn, 1, "AVE")

bdd.link_document_theme(conn, 2, "FANT")
bdd.link_document_theme(conn, 2, "AMIT")

bdd.link_document_theme(conn, 3, "DEP")
bdd.link_document_theme(conn, 3, "PHIL")

bdd.link_document_theme(conn, 4, "SOC")
bdd.link_document_theme(conn, 4, "SURV")

bdd.link_document_theme(conn, 5, "AMO")
bdd.link_document_theme(conn, 5, "SOC")

bdd.link_document_theme(conn, 6, "PHIL")
bdd.link_document_theme(conn, 6, "SOC")

bdd.link_document_theme(conn, 7,  "AVE")
bdd.link_document_theme(conn, 7, "HIST")

bdd.link_document_theme(conn, 8, "FAM")
bdd.link_document_theme(conn, 8, "HIST")

bdd.link_document_theme(conn, 9, "MYST")
bdd.link_document_theme(conn, 9, "RELIG")

bdd.link_document_theme(conn, 10, "CULT")
bdd.link_document_theme(conn, 10, "VOY")

bdd.link_document_theme(conn, 11, "HIST")
bdd.link_document_theme(conn, 11, "CULT")

bdd.link_document_theme(conn, 12, "PHIL")
bdd.link_document_theme(conn, 12, "CULT")

bdd.link_document_theme(conn, 13, "DEP")
bdd.link_document_theme(conn, 13, "MYST")

bdd.link_document_theme(conn, 14, "FANT")
bdd.link_document_theme(conn, 14, "HIST")

bdd.link_document_theme(conn, 15, "SOC")
bdd.link_document_theme(conn, 15, "PHILO")

bdd.link_document_theme(conn, 16, "AVE")
bdd.link_document_theme(conn, 16, "HUM")

bdd.link_document_theme(conn, 17, "AMO")
bdd.link_document_theme(conn, 17, "DEP")

bdd.link_document_theme(conn, 18, "PHILO")
bdd.link_document_theme(conn, 18, "CULT")

bdd.link_document_theme(conn, 19, "HIST")
bdd.link_document_theme(conn, 19, "AVE")

bdd.link_document_theme(conn, 20, "FAMI")
bdd.link_document_theme(conn, 20, "CULT")

bdd.link_document_theme(conn, 21, "HIST")
bdd.link_document_theme(conn, 21, "CULT")

bdd.link_document_theme(conn, 22, "AVE")
bdd.link_document_theme(conn, 22, "CULT")

bdd.link_document_theme(conn, 23, "VOY")
bdd.link_document_theme(conn, 23, "FANT")

bdd.link_document_theme(conn, 24, "AVE")
bdd.link_document_theme(conn, 24, "HUM")

bdd.link_document_theme(conn, 25, "HIST")
bdd.link_document_theme(conn, 25, "MYST")

bdd.link_document_theme(conn, 26, "DEP")
bdd.link_document_theme(conn, 26, "PHILO")

bdd.link_document_theme(conn, 27, "MYST")
bdd.link_document_theme(conn, 27, "AVE")

bdd.link_document_theme(conn, 28, "VOY")
bdd.link_document_theme(conn, 28, "HIST")

bdd.link_document_theme(conn, 29, "FANT")
bdd.link_document_theme(conn, 29, "MYST")

bdd.link_document_theme(conn, 30, "HIST")
bdd.link_document_theme(conn, 30, "FAM")

bdd.link_document_theme(conn, 31, "HUM")
bdd.link_document_theme(conn, 31, "AMO")

bdd.link_document_theme(conn, 32, "DEP")
bdd.link_document_theme(conn, 32, "PHILO")

bdd.link_document_theme(conn, 33, "FANT")
bdd.link_document_theme(conn, 33, "FAMI")

bdd.link_document_theme(conn, 34, "POLI")
bdd.link_document_theme(conn, 34, "SOC")

bdd.link_document_theme(conn, 35, "ART")
bdd.link_document_theme(conn, 35, "MYST")

bdd.link_document_theme(conn, 36, "IDENT")
bdd.link_document_theme(conn, 36, "AMI")
bdd.link_document_theme(conn, 36, "FAMI")