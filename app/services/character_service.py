"""Character service for business logic and character generation"""

import random
from app.models import Character, Class, Race, Alignment, Stats


def roll_ability_score() -> int:
    """Roll 4d6, drop lowest die (standard D&D method)"""
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)


def generate_random_stats() -> Stats:
    """Generate random ability scores using 4d6 drop lowest"""
    return Stats(
        strength=roll_ability_score(),
        dexterity=roll_ability_score(),
        constitution=roll_ability_score(),
        intelligence=roll_ability_score(),
        wisdom=roll_ability_score(),
        charisma=roll_ability_score(),
    )


def generate_random_name(race: Race, class_: Class) -> str:
    """Generate a random character name based on race"""

    first_names = {
        Race.HUMAN: [
            "Alric",
            "Brianna",
            "Connor",
            "Diana",
            "Erik",
            "Fiona",
            "Garrett",
            "Helena",
        ],
        Race.ELF: [
            "Aelrindel",
            "Caelynn",
            "Erevan",
            "Faelyn",
            "Galadriel",
            "Silaqui",
            "Theren",
            "Valandil",
        ],
        Race.DWARF: [
            "Baern",
            "Dagnal",
            "Eberk",
            "Fargrim",
            "Gimli",
            "Thorin",
            "Ulfgar",
            "Vondal",
        ],
        Race.HALFLING: [
            "Alton",
            "Cora",
            "Eldon",
            "Lily",
            "Merric",
            "Portia",
            "Rosco",
            "Seraphina",
        ],
        Race.DRAGONBORN: [
            "Arjhan",
            "Balasar",
            "Donaar",
            "Ghesh",
            "Heskan",
            "Kriv",
            "Medrash",
            "Patrin",
        ],
        Race.GNOME: [
            "Alston",
            "Brocc",
            "Dimble",
            "Eldon",
            "Fonkin",
            "Gimble",
            "Orryn",
            "Roondar",
        ],
        Race.HALF_ELF: [
            "Arlan",
            "Celeste",
            "Damien",
            "Elara",
            "Gareth",
            "Lyra",
            "Rowan",
            "Selene",
        ],
        Race.HALF_ORC: [
            "Dench",
            "Feng",
            "Gell",
            "Holg",
            "Imsh",
            "Keth",
            "Mhurren",
            "Ront",
        ],
        Race.TIEFLING: [
            "Akmenios",
            "Damakos",
            "Ekemon",
            "Iados",
            "Kairon",
            "Leucis",
            "Melech",
            "Therai",
        ],
    }

    return random.choice(first_names.get(race, ["Adventurer"]))


def generate_random_description(
    name: str, race: Race, class_: Class, alignment: Alignment
) -> str:
    """Generate a character description using race, class, and alignment"""

    # Character traits by class
    class_traits = {
        Class.BARBARIAN: ["fierce", "wild", "untamed", "savage", "primal"],
        Class.BARD: ["charismatic", "eloquent", "artistic", "charming", "witty"],
        Class.CLERIC: ["devout", "faithful", "holy", "devoted", "righteous"],
        Class.DRUID: ["mystical", "nature-bound", "wise", "primal", "balanced"],
        Class.FIGHTER: [
            "disciplined",
            "skilled",
            "battle-hardened",
            "tactical",
            "brave",
        ],
        Class.MONK: ["disciplined", "serene", "focused", "spiritual", "meditative"],
        Class.PALADIN: ["noble", "honorable", "righteous", "sworn", "devoted"],
        Class.RANGER: [
            "skilled",
            "wilderness-wise",
            "tracking",
            "solitary",
            "keen-eyed",
        ],
        Class.ROGUE: ["cunning", "stealthy", "quick-witted", "shadowy", "resourceful"],
        Class.SORCERER: [
            "innately powerful",
            "mysterious",
            "chaotic",
            "gifted",
            "unpredictable",
        ],
        Class.WARLOCK: [
            "pact-bound",
            "mysterious",
            "dark",
            "enigmatic",
            "otherworldly",
        ],
        Class.WIZARD: ["scholarly", "studious", "arcane", "intellectual", "learned"],
    }

    # Background motivations by alignment
    alignment_motivations = {
        Alignment.LAWFUL_GOOD: [
            "protects the innocent",
            "upholds justice",
            "serves the greater good",
        ],
        Alignment.NEUTRAL_GOOD: [
            "helps those in need",
            "does what's right",
            "brings hope to others",
        ],
        Alignment.CHAOTIC_GOOD: [
            "fights for freedom",
            "rebels against tyranny",
            "champions the oppressed",
        ],
        Alignment.LAWFUL_NEUTRAL: [
            "follows a strict code",
            "maintains order",
            "upholds tradition",
        ],
        Alignment.TRUE_NEUTRAL: [
            "seeks balance",
            "avoids extremes",
            "remains independent",
        ],
        Alignment.CHAOTIC_NEUTRAL: [
            "follows their own path",
            "values freedom above all",
            "lives by their whims",
        ],
        Alignment.LAWFUL_EVIL: [
            "ruthlessly pursues power",
            "manipulates through law",
            "dominates through order",
        ],
        Alignment.NEUTRAL_EVIL: [
            "serves only themselves",
            "schemes for personal gain",
            "exploits the weak",
        ],
        Alignment.CHAOTIC_EVIL: [
            "spreads chaos and destruction",
            "revels in cruelty",
            "takes what they want",
        ],
        Alignment.UNALIGNED: [
            "acts on instinct",
            "follows no moral code",
            "exists beyond morality",
        ],
    }

    # Race-specific background elements
    race_backgrounds = {
        Race.HUMAN: [
            "from a diverse background",
            "adaptable to any situation",
            "driven by ambition",
        ],
        Race.ELF: [
            "with centuries of wisdom",
            "connected to ancient magic",
            "graceful and patient",
        ],
        Race.DWARF: [
            "with a proud clan heritage",
            "master of craftsmanship",
            "stubborn and loyal",
        ],
        Race.HALFLING: [
            "with a love for comfort and adventure",
            "lucky beyond measure",
            "curious about the world",
        ],
        Race.DRAGONBORN: [
            "bearing the blood of dragons",
            "seeking to honor their clan",
            "proud and honorable",
        ],
        Race.GNOME: [
            "with boundless curiosity",
            "inventive and clever",
            "forever optimistic",
        ],
        Race.HALF_ELF: [
            "caught between two worlds",
            "versatile and adaptable",
            "searching for belonging",
        ],
        Race.HALF_ORC: [
            "struggling against prejudice",
            "proving their worth",
            "fierce and determined",
        ],
        Race.TIEFLING: [
            "marked by infernal heritage",
            "overcoming dark assumptions",
            "resilient and resourceful",
        ],
    }

    # Build the description
    trait = random.choice(class_traits[class_])
    motivation = random.choice(alignment_motivations[alignment])
    background = random.choice(race_backgrounds[race])

    templates = [
        f"{name} is a {trait} {race.value} {class_.value} {background} who {motivation}.",
        f"A {trait} {class_.value} {background}, {name} {motivation} wherever they go.",
        f"{name}, a {race.value} {class_.value}, is known as a {trait} adventurer who {motivation}.",
        f"Born {background}, {name} became a {trait} {class_.value} who {motivation}.",
    ]

    return random.choice(templates)


def generate_random_character() -> Character:
    """Generate a completely random D&D character"""

    # Random selections
    race = random.choice(list(Race))
    class_ = random.choice(list(Class))
    alignment = random.choice(list(Alignment))
    stats = generate_random_stats()
    name = generate_random_name(race, class_)
    description = generate_random_description(name, race, class_, alignment)

    # Generate a random ID (in production, this would come from database)
    character_id = random.randint(1000, 9999)

    return Character(
        id=character_id,
        name=name,
        race=race,
        alignment=alignment,
        description=description,
        stats=stats,
        **{"class": class_},  # Use dict unpacking to handle the alias
    )
