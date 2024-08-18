import sys


def text_scrolling(text_to_scroll):
    for line in text_to_scroll:       
        sys.stdout.write(line) 
        input()


beginning = [
    "- Ho mon Dieu !!!",
    "Les cris du boss dans le couloir n'avaient pas la même tonalité qu'à l'habituelle.",
    "- Une bombe !!!",
    "P***... il ne reste que 10 minutes et ce connard ne me paiera jamais pour des heures supplémentaires",
    "Et là, il rentre dans le open-space et, en sueur, vient planter ses mains poisseuses sur mon bureau",
    "- Toi ! me gueule t'il dessus.",
    "- Moi ? en regardant autour de moi.",
    "- Toi !",
    "- Moi ?",
    "- Oui toi petit c***! Tu viens avec moi !",
    "Il me traine dans son bureau, sur sa table il y a un colis ouvert.",
    "Tremblant, il reste sur le port de la porte et me montre ce fameux colis de son tout petit doigt tout boudiné",
    "Bon, il y a effectivement une bombe..",
    "- Il y a un petit écran dessus avec une énigme à résoudre",
    "et, en sanglots, il rajoute : - Il a de toute évidence été codé par un génie !!",
    "Sur ce, il m'enferme dans son bureau et me crie : ",
    "- Je te vire pas si tu la désamorce !!"

]

win_end = ["La bombe est désamorcée.",
          "La porte s'ouvre violemment, laissant place à des cris de joie et de soulagement.",
          "En quelques instants, je deviens le héros du bureau, puis de la ville.",
          "Les médias se passionnent pour mon histoire, des hommages affluent de partout.",
          "Ma bravoure, ma rapidité d'esprit, tout le monde en parle.",
          "Les honneurs pleuvent et, à ma grande surprise, je me retrouve au-devant de la scène politique.",
          "Les gens m'adulent, les responsabilités s'accumulent.",
          "Devenu une figure emblématique, les portes du pouvoir s'ouvrent.",
          "Élu par acclamation, je deviens le roi de Belgique.",
          "Une ascension fulgurante, portée par cet acte héroïque.",
          "Le temps passant...",
          "Le roi, désireux de créer un parc d'attractions privé,",
          "lance un projet de démolition de quartiers résidentiels à faible revenu pour construire cet espace récréatif.",
          "Cette décision provoque un tollé parmi les citoyens et les groupes sociaux qui défendent les droits des plus démunis.",
          "Des rumeurs commencent à circuler sur le roi effectuant des vols en avion de chasse alors qu'il est sous l'influence de l'alcool et autres.",
          "Des preuves photographiques circulent sur Tick-Tock et documentent ces comportements irresponsables mettant en danger la sécurité nationale",
          "Le 26/03/2033, lors d'une de ses sorties, le roi, par inatvertance, tire un missile sur la tour RTBF.",
          "Il y a de nombreux morts, dont le journaliste qui a sorti les enquêtes sur le parc-d'attractions-gate",
          "Lors de la même balade, un deuxième missile touche par hasard le lanceur d'alerte ayant rendu public des photos du roi sniffant un rail avant de conduire",
          "Le 01/04/2034, le roi meurt de sa belle mort et à cet occasion, un deuil national est décrèté par le gouvernement",
          "De nombreux citoyens, le visage grave et triste, se rendent à son enterrement...",
          "Nan j'rigole, c'était un poisson d'avril!",
          "En fait, il est mort d'une syrose du foie, seul et haï par tous",
          "Fin",

]


loose_end = [
    "L'éclair blanc déchire la réalité, engloutissant tout dans son sillage destructeur.",
    "La lumière intense dévore les murs, les corps, les espoirs. Un fracas assourdissant m'engloutit dans un chaos terrifiant.",
    "L'explosion emporte une partie significative de l'humanité dans une danse macabre d'éclats, de flammes et de débris.",
    "Ce qui reste du monde n'est que désolation.",
    "Un hiver atomique s'abat, plongeant les rares survivants dans un froid glacial.",
    "La radioactivité se répand tel un poison, déformant les corps, semant la maladie et la mort.",
    "Les enfants naissent avec des malformations, des maladies incurables se répandent, anéantissant tout espoir de normalité.",
    "Les villes se transforment en cimetières, les champs en terres stériles.",
    "Chaque jour devient un combat pour la survie, une lutte contre les éléments déchaînés et la décrépitude des corps rongés par la radiation.",
    "La vie tente de renaître dans ce monde apocalyptique, mais chaque battement de cœur est une symphonie de souffrance et de désespoir.",
    "Le monde se relève péniblement de cette catastrophe, mais mon nom est devenu synonyme de désespoir, de négligence, de défaillance.",
    "Chaque récit, chaque trace de mon existence est teinté de mépris et de colère.",
    "Les survivants me blâment, me haïssent pour n'avoir pu sauver ce qui pouvait l'être. ",
    "Les générations futures, celles dont les vies sont déformées par la radioactivité, maudiront mon nom comme celui d'un symbole de l'échec humain.",
    "Dans leurs récits, je serai l'incarnation du regret, de la trahison, celui qui a abandonné l'humanité à son destin funeste.",
    "Les livres d'histoire porteront mon fardeau, chaque mention de mon nom réveillant le spectre d'une tragédie que l'on aurait pu éviter.",
    "Mon héritage, c'est une souffrance éternelle gravée dans l'inconscient collectif, une marque indélébile de la faillite humaine.",
    "Et ainsi, dans le tourment perpétuel de cet au-delà, ma conscience porte le poids de cette haine universelle,",
    "Eternellement condamné à être celui qui a précipité l'humanité vers sa propre chute.",
    "Fin",

]








