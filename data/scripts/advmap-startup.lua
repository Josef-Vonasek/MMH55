-- Global symbols (DO NOT EDIT)

doFile('/scripts/events.lua')

--
-- Logical constants
--
true = not nil
false = nil

--
-- Names filter
--
FILTER_HEROES = 0
FILTER_OBJECTS = 1
FILTER_REGIONS = 2
FILTER_OBJECTIVES = 3

--
-- Player IDs
--
PLAYER_NONE = 0
PLAYER_1 = 1
PLAYER_2 = 2
PLAYER_3 = 3
PLAYER_4 = 4
PLAYER_5 = 5
PLAYER_6 = 6
PLAYER_7 = 7
PLAYER_8 = 8

--
-- Player states
--
PLAYER_NOT_IN_GAME = 0
PLAYER_ACTIVE = 1
PLAYER_WON = 2
PLAYER_LOST = 3

--
-- Floors names
--
GROUND = 0
UNDERGROUND = 1

--
-- Kinds of resources
--
WOOD    = 0
ORE     = 1
MERCURY = 2
CRYSTAL = 3
SULFUR  = 4
GEM     = 5
GOLD    = 6

--
-- Kinds of treasures
--
TREASURE_CRYSTAL   = 0
TREASURE_GEMS      = 1
TREASURE_GOLD      = 2
TREASURE_MERCURY   = 3
TREASURE_ORE       = 4
TREASURE_SULFUR    = 5
TREASURE_WOOD      = 6
TREASURE_CAMPFIRE  = 8
TREASURE_CHEST     = 9
TREASURE_SEA_CHEST = 10
TREASURE_FLOATSAM  = 11
TREASURE_SHIPWRECK = 13

--
-- Date type IDs
--
DAY = 0
WEEK = 1
MONTH = 2
DAY_OF_WEEK = 3
ABSOLUTE_DAY = DAY

--
-- Advmap predefided names
--
OBJECT_GRAIL = 'grail'

--
-- Advmap object types
--
OBJECT_HERO = 0

--
-- Hero stat`s IDs
--
STAT_EXPERIENCE = 0
STAT_ATTACK = 1
STAT_DEFENCE = 2
STAT_SPELL_POWER = 3
STAT_KNOWLEDGE = 4
STAT_LUCK = 5
STAT_MORALE = 6
STAT_MOVE_POINTS = 7
STAT_MANA_POINTS = 8

--
-- Objective state`s IDs
--
OBJECTIVE_SCENARIO_INFO = 0
OBJECTIVE_UNKNOWN = 1
OBJECTIVE_ACTIVE = 2
OBJECTIVE_COMPLETED = 3
OBJECTIVE_FAILED = 4

--
-- Artifact sets IDs (for basic artifact sets)
-- (synchronized with RPGStats/ArtifactSets )
--
ARTIFACT_SET_DRAGONISH = 0
ARTIFACT_SET_DWARVEN = 1
ARTIFACT_SET_LIONS = 2
ARTIFACT_SET_MAGIS = 3
ARTIFACT_SET_NECROMANCERS = 4
ARTIFACT_SET_EDUCATIONAL = 5
ARTIFACT_SET_HUNTERS = 6
ARTIFACT_SET_OGRES = 7
ARTIFACT_SET_RUNIC = 8
ARTIFACT_SET_DEMONIC = 9

--
-- Artifact type IDs
--
ARTIFACT_SWORD_OF_RUINS = 1
ARTIFACT_GREAT_AXE_OF_GIANT_SLAYING = 2
ARTIFACT_WAND_OF_X = 3
ARTIFACT_UNICORN_HORN_BOW = 4
ARTIFACT_TITANS_TRIDENT = 5
ARTIFACT_STAFF_OF_VEXINGS = 6
ARTIFACT_SHACKLES_OF_WAR = 7
ARTIFACT_FOUR_LEAF_CLOVER = 8
ARTIFACT_ICEBERG_SHIELD = 9
ARTIFACT_GOLDEN_SEXTANT = 10
ARTIFACT_CROWN_OF_COURAGE = 11
ARTIFACT_CROWN_OF_MANY_EYES = 12
ARTIFACT_PLATE_MAIL_OF_STABILITY = 13
ARTIFACT_BREASTPLATE_OF_PETRIFIED_WOOD = 14
ARTIFACT_PEDANT_OF_MASTERY = 15
ARTIFACT_NECKLACE_OF_BRAVERY = 16
ARTIFACT_WEREWOLF_CLAW_NECKLACE = 17
ARTIFACT_EVERCOLD_ICICLE = 18
ARTIFACT_NECKLACE_OF_POWER = 19
ARTIFACT_RING_OF_LIGHTING_PROTECTION = 20
ARTIFACT_RING_OF_LIFE = 21
ARTIFACT_RING_OF_HASTE = 22
ARTIFACT_NIGHTMARISH_RING = 23
ARTIFACT_BOOTS_OF_SPEED = 24
ARTIFACT_GOLDEN_HORSESHOE = 25
ARTIFACT_WAYFARER_BOOTS = 26
ARTIFACT_BOOTS_OF_INTERFERENCE = 27
ARTIFACT_ENDLESS_SACK_OF_GOLD = 28
ARTIFACT_ENDLESS_BAG_OF_GOLD = 29
ARTIFACT_ANGEL_WINGS = 30
ARTIFACT_LION_HIDE_CAPE = 31
ARTIFACT_PHOENIX_FEATHER_CAPE = 32
ARTIFACT_CLOAK_OF_MOURNING = 33
ARTIFACT_HELM_OF_ENLIGHTMENT = 34
ARTIFACT_CHAIN_MAIL_OF_ENLIGHTMENT = 35
ARTIFACT_DRAGON_SCALE_ARMOR = 36
ARTIFACT_DRAGON_SCALE_SHIELD = 37
ARTIFACT_DRAGON_BONE_GRAVES = 38
ARTIFACT_DRAGON_WING_MANTLE = 39
ARTIFACT_DRAGON_TEETH_NECKLACE = 40
ARTIFACT_DRAGON_TALON_CROWN = 41
ARTIFACT_DRAGON_EYE_RING = 42
ARTIFACT_DRAGON_FLAME_TONGUE = 43
ARTIFACT_ROBE_OF_MAGI = 44
ARTIFACT_STAFF_OF_MAGI = 45
ARTIFACT_CROWN_OF_MAGI = 46
ARTIFACT_RING_OF_MAGI = 47
ARTIFACT_DWARVEN_MITHRAL_CUIRASS = 48
ARTIFACT_DWARVEN_MITHRAL_GREAVES = 49
ARTIFACT_DWARVEN_MITHRAL_HELMET = 50
ARTIFACT_DWARVEN_MITHRAL_SHIELD = 51
ARTIFACT_SCROLL_OF_SPELL_X = 52
ARTIFACT_GRAAL = 53
ARTIFACT_BOOTS_OF_LEVITATION = 54
ARTIFACT_SKULL_HELMET = 55
ARTIFACT_VALORIOUS_ARMOR = 56
ARTIFACT_BOOTS_OF_SWIFTNESS = 57
ARTIFACT_MOONBLADE = 58
ARTIFACT_RING_OF_CELERITY = 59
ARTIFACT_BAND_OF_CONJURER = 60
ARTIFACT_EARTHSLIDERS = 61
ARTIFACT_RIGID_MANTLE = 62
ARTIFACT_JINXING_BAND = 63
ARTIFACT_BONESTUDDED_LEATHER = 64
ARTIFACT_WISPERING_RING = 65
ARTIFACT_HELM_OF_CHAOS = 66
ARTIFACT_TWISTING_NEITHER = 67
ARTIFACT_SANDALS_OF_THE_SAINT = 68
ARTIFACT_SHAWL_OF_GREAT_LICH = 69
ARTIFACT_RING_OF_DEATH = 70
ARTIFACT_NECROMANCER_PENDANT = 71
ARTIFACT_FREIDA = 72
ARTIFACT_RING_OF_THE_SHADOWBRAND = 73
ARTIFACT_OGRE_CLUB = 74
ARTIFACT_OGRE_SHIELD = 75
ARTIFACT_TOME_OF_DESTRUCTION = 76
ARTIFACT_TOME_OF_LIGHT_MAGIC = 77
ARTIFACT_TOME_OF_DARK_MAGIC = 78
ARTIFACT_TOME_OF_SUMMONING_MAGIC = 79
ARTIFACT_BEGINNER_MAGIC_STICK = 80
ARTIFACT_RUNIC_WAR_AXE = 81
ARTIFACT_RUNIC_WAR_HARNESS = 82
ARTIFACT_SKULL_OF_MARKAL = 83
ARTIFACT_BEARHIDE_WRAPS = 84
ARTIFACT_DWARVEN_SMITHY_HUMMER = 85
ARTIFACT_RUNE_OF_FLAME = 86
ARTIFACT_TAROT_DECK = 87
ARTIFACT_CROWN_OF_LEADER = 88
ARTIFACT_MASK_OF_DOPPELGANGER = 89
ARTIFACT_EDGE_OF_BALANCE = 90
ARTIFACT_RING_OF_MACHINE_AFFINITY = 91
ARTIFACT_HORN_OF_PLENTY = 92
ARTIFACT_RING_OF_UNSUMMONING = 93
ARTIFACT_BOOK_OF_POWER = 94
ARTIFACT_TREEBORN_QUIVER = 95
ARTIFACT_PRINCESS = 96
ARTIFACT_RES_WOOD = 97
ARTIFACT_RES_ORE = 98
ARTIFACT_RES_SULPHUR = 99
ARTIFACT_RES_CRYSTAL = 100
ARTIFACT_RES_GEM = 101
ARTIFACT_RES_MERCURY = 102	
ARTIFACT_LEGION_T1 = 103
ARTIFACT_LEGION_T2 = 104
ARTIFACT_LEGION_T3 = 105
ARTIFACT_LEGION_T4 = 106
ARTIFACT_LEGION_T5 = 107
ARTIFACT_LEGION_T6 = 108
ARTIFACT_LEGION_T7 = 109
ARTIFACT_STEADFAST = 110
ARTIFACT_BUCKLER = 111
ARTIFACT_LIFE_01 = 112
ARTIFACT_LIFE_02 = 113
ARTIFACT_LIFE_03 = 114
ARTIFACT_LIFE_04 = 115
ARTIFACT_MONK_01 = 116
ARTIFACT_MONK_02 = 117
ARTIFACT_MONK_03 = 118
ARTIFACT_MONK_04 = 119
ARTIFACT_GUARDIAN_01 = 120
ARTIFACT_GUARDIAN_02 = 121
ARTIFACT_GUARDIAN_03 = 122
ARTIFACT_DRACONIC = 123
ARTIFACT_SENTINEL = 124
ARTIFACT_EIGHTFOLD = 125
ARTIFACT_CODEX = 126


-- Skill type IDs
--
-- Basic Skills
SKILL_LOGISTICS = 1
SKILL_WAR_MACHINES = 2
SKILL_LEARNING = 3
SKILL_LEADERSHIP = 4
SKILL_LUCK = 5
SKILL_OFFENCE = 6
SKILL_DEFENCE = 7
SKILL_SORCERY = 8
SKILL_DESTRUCTIVE_MAGIC = 9
SKILL_DARK_MAGIC = 10
SKILL_LIGHT_MAGIC = 11
SKILL_SUMMONING_MAGIC = 12
-- Class skills
SKILL_TRAINING   = 13
SKILL_GATING     = 14
SKILL_NECROMANCY = 15
SKILL_AVENGER = 16
SKILL_ARTIFICIER = 17
SKILL_INVOCATION = 18
-- Perks
PERK_PATHFINDING = 19
PERK_SCOUTING = 20
PERK_NAVIGATION = 21
PERK_FIRST_AID = 22
PERK_BALLISTA = 23
PERK_CATAPULT = 24
PERK_INTELLIGENCE = 25
PERK_SCHOLAR = 26
PERK_EAGLE_EYE = 27
PERK_RECRUITMENT = 28
PERK_ESTATES = 29
PERK_DIPLOMACY = 30
PERK_RESISTANCE = 31
PERK_LUCKY_STRIKE = 32
PERK_FORTUNATE_ADVENTURER = 33
PERK_TACTICS = 34
PERK_ARCHERY = 35
PERK_FRENZY = 36
PERK_PROTECTION = 37
PERK_EVASION = 38
PERK_TOUGHNESS = 39
PERK_MYSTICISM = 40
PERK_WISDOM = 41
PERK_ARCANE_TRAINING = 42
PERK_MASTER_OF_ICE = 43
PERK_MASTER_OF_FIRE = 44
PERK_MASTER_OF_LIGHTNINGS = 45
PERK_MASTER_OF_CURSES = 46
PERK_MASTER_OF_MIND = 47
PERK_MASTER_OF_SICKNESS = 48
PERK_MASTER_OF_BLESSING = 49
PERK_MASTER_OF_ABJURATION = 50
PERK_MASTER_OF_WRATH = 51
PERK_MASTER_OF_QUAKES = 52
PERK_MASTER_OF_CREATURES = 53
PERK_MASTER_OF_ANIMATION = 54
-- Knight perks
PERK_HOLY_CHARGE = 55
PERK_PRAYER = 56
PERK_EXPERT_TRAINER = 57
-- Demonlord perks
PERK_CONSUME_CORPSE = 58
PERK_DEMONIC_FIRE = 59
PERK_DEMONIC_STRIKE = 60
-- Necromancer perks
PERK_RAISE_ARCHERS          = 61
PERK_NO_REST_FOR_THE_WICKED = 62
PERK_DEATH_SCREAM           = 63
-- Ranger perks
PERK_MULTISHOT = 64
PERK_SNIPE_DEAD = 65
PERK_IMBUE_ARROW = 66
-- Wizard perks 
PERK_MAGIC_BOND = 67
PERK_MELT_ARTIFACT = 68
PERK_MAGIC_MIRROR = 69
-- Warlock perks
PERK_EMPOWERED_SPELLS = 70
PERK_DARK_RITUAL = 71
PERK_ELEMENTAL_VISION = 72
-- Feats
-- Knight
KNIGHT_FEAT_ROAD_HOME = 73
KNIGHT_FEAT_TRIPLE_BALLISTA = 74
KNIGHT_FEAT_ENCOURAGE = 75
KNIGHT_FEAT_RETRIBUTION = 76
KNIGHT_FEAT_HOLD_GROUND = 77
KNIGHT_FEAT_GUARDIAN_ANGEL = 78
KNIGHT_FEAT_STUDENT_AWARD = 79
KNIGHT_FEAT_GRAIL_VISION = 80
KNIGHT_FEAT_CASTER_CERTIFICATE = 81
KNIGHT_FEAT_ANCIENT_SMITHY = 82
KNIGHT_FEAT_PARIAH = 83
KNIGHT_FEAT_ELEMENTAL_BALANCE = 84
KNIGHT_FEAT_ABSOLUTE_CHARGE = 85
-- Demon Lord
DEMON_FEAT_QUICK_GATING = 86
DEMON_FEAT_MASTER_OF_SECRETS = 87
DEMON_FEAT_TRIPLE_CATAPULT = 88
DEMON_FEAT_GATING_MASTERY = 89
DEMON_FEAT_CRITICAL_GATING = 90
DEMON_FEAT_CRITICAL_STRIKE = 91
DEMON_FEAT_DEMONIC_RETALIATION = 92
DEMON_FEAT_EXPLODING_CORPSES = 93
DEMON_FEAT_DEMONIC_FLAME = 94
DEMON_FEAT_WEAKENING_STRIKE = 95
DEMON_FEAT_FIRE_PROTECTION = 96
DEMON_FEAT_FIRE_AFFINITY = 97
DEMON_FEAT_ABSOLUTE_GATING = 98
-- Necromancer
NECROMANCER_FEAT_DEATH_TREAD = 99
NECROMANCER_FEAT_LAST_AID = 100
NECROMANCER_FEAT_LORD_OF_UNDEAD = 101
NECROMANCER_FEAT_HERALD_OF_DEATH = 102
NECROMANCER_FEAT_DEAD_LUCK = 103
NECROMANCER_FEAT_CHILLING_STEEL = 104
NECROMANCER_FEAT_CHILLING_BONES = 105
NECROMANCER_FEAT_SPELLPROOF_BONES = 106
NECROMANCER_FEAT_DEADLY_COLD = 107
NECROMANCER_FEAT_SPIRIT_LINK = 108
NECROMANCER_FEAT_TWILIGHT = 109
NECROMANCER_FEAT_HAUNT_MINE = 110
NECROMANCER_FEAT_ABSOLUTE_FEAR = 111
-- Ranger
RANGER_FEAT_DISGUISE_AND_RECKON = 112
RANGER_FEAT_IMBUE_BALLISTA = 113
RANGER_FEAT_CUNNING_OF_THE_WOODS = 114
RANGER_FEAT_FOREST_GUARD_EMBLEM = 115
RANGER_FEAT_ELVEN_LUCK = 116
RANGER_FEAT_FOREST_RAGE = 117
RANGER_FEAT_LAST_STAND = 118
RANGER_FEAT_INSIGHTS = 119
RANGER_FEAT_SUN_FIRE = 120
RANGER_FEAT_SOIL_BURN = 121
RANGER_FEAT_STORM_WIND = 122
RANGER_FEAT_FOG_VEIL = 123
RANGER_FEAT_ABSOLUTE_LUCK = 124
-- Wizard
WIZARD_FEAT_MARCH_OF_THE_MACHINES = 125
WIZARD_FEAT_REMOTE_CONTROL = 126
WIZARD_FEAT_ACADEMY_AWARD = 127
WIZARD_FEAT_ARTIFICIAL_GLORY = 128
WIZARD_FEAT_SPOILS_OF_WAR = 129
WIZARD_FEAT_WILDFIRE = 130
WIZARD_FEAT_SEAL_OF_PROTECTION = 131
WIZARD_FEAT_COUNTERSPELL = 132
WIZARD_FEAT_MAGIC_CUSHION = 133
WIZARD_FEAT_SUPRESS_DARK  = 134
WIZARD_FEAT_SUPRESS_LIGHT  = 135
WIZARD_FEAT_UNSUMMON  = 136
WIZARD_FEAT_ABSOLUTE_WIZARDY = 137
-- warlock
WARLOCK_FEAT_TELEPORT_ASSAULT = 138
WARLOCK_FEAT_SHAKE_GROUND = 139
WARLOCK_FEAT_DARK_REVELATION = 140
WARLOCK_FEAT_FAST_AND_FURIOUS = 141
WARLOCK_FEAT_LUCKY_SPELLS = 142
WARLOCK_FEAT_POWER_OF_HASTE = 143
WARLOCK_FEAT_POWER_OF_STONE = 144
WARLOCK_FEAT_CHAOTIC_SPELLS = 145
WARLOCK_FEAT_SECRETS_OF_DESTRUCTION = 146
WARLOCK_FEAT_PAYBACK = 147
WARLOCK_FEAT_ELITE_CASTERS = 148
WARLOCK_FEAT_ELEMENTAL_OVERKILL	= 149
WARLOCK_FEAT_ABSOLUTE_CHAINS = 150
-- runemage
HERO_SKILL_RUNELORE = 151
HERO_SKILL_REFRESH_RUNE = 152
HERO_SKILL_STRONG_RUNE = 153
HERO_SKILL_FINE_RUNE = 154
HERO_SKILL_QUICKNESS_OF_MIND = 155
HERO_SKILL_RUNIC_MACHINES = 156
HERO_SKILL_TAP_RUNES = 157
HERO_SKILL_RUNIC_ATTUNEMENT = 158
HERO_SKILL_DWARVEN_LUCK = 159
HERO_SKILL_OFFENSIVE_FORMATION = 160
HERO_SKILL_DEFENSIVE_FORMATION = 161
HERO_SKILL_DISTRACT = 162
HERO_SKILL_SET_AFIRE = 163
HERO_SKILL_SHRUG_DARKNESS = 164
HERO_SKILL_ETERNAL_LIGHT = 165
HERO_SKILL_RUNIC_ARMOR = 166
HERO_SKILL_ABSOLUTE_PROTECTION = 167
-- runmage & barbarian   cross-class
HERO_SKILL_SNATCH = 168
HERO_SKILL_MENTORING = 169
HERO_SKILL_EMPATHY = 170
HERO_SKILL_PREPARATION = 171
-- barbarian
HERO_SKILL_DEMONIC_RAGE = 172
HERO_SKILL_MIGHT_OVER_MAGIC = 173
HERO_SKILL_MEMORY_OF_OUR_BLOOD = 174
HERO_SKILL_POWERFULL_BLOW = 175
HERO_SKILL_ABSOLUTE_RAGE = 176
HERO_SKILL_PATH_OF_WAR = 177
HERO_SKILL_BATTLE_ELATION = 178
HERO_SKILL_LUCK_OF_THE_BARBARIAN = 179
HERO_SKILL_STUNNING_BLOW = 180
HERO_SKILL_DEFEND_US_ALL = 181
HERO_SKILL_GOBLIN_SUPPORT = 182
HERO_SKILL_BARBARIAN_LEARNING = 183
HERO_SKILL_POWER_OF_BLOOD = 184
HERO_SKILL_WARCRY_LEARNING = 185
HERO_SKILL_BODYBUILDING = 186
HERO_SKILL_VOICE = 187
HERO_SKILL_VOICE_TRAINING = 188
HERO_SKILL_MIGHTY_VOICE = 189
HERO_SKILL_VOICE_OF_RAGE = 190
HERO_SKILL_SHATTER_DESTRUCTIVE_MAGIC = 191
HERO_SKILL_CORRUPT_DESTRUCTIVE = 192
HERO_SKILL_WEAKEN_DESTRUCTIVE = 193
HERO_SKILL_DETAIN_DESTRUCTIVE = 194
HERO_SKILL_SHATTER_DARK_MAGIC = 195
HERO_SKILL_CORRUPT_DARK = 196
HERO_SKILL_WEAKEN_DARK = 197
HERO_SKILL_DETAIN_DARK = 198
HERO_SKILL_SHATTER_LIGHT_MAGIC = 199
HERO_SKILL_CORRUPT_LIGHT = 200
HERO_SKILL_WEAKEN_LIGHT = 201
HERO_SKILL_DETAIN_LIGHT = 202
HERO_SKILL_SHATTER_SUMMONING_MAGIC = 203
HERO_SKILL_CORRUPT_SUMMONING = 204
HERO_SKILL_WEAKEN_SUMMONING = 205
HERO_SKILL_DETAIN_SUMMONING = 206
HERO_SKILL_DEATH_TO_NONEXISTENT = 207
HERO_SKILL_BARBARIAN_ANCIENT_SMITHY = 208
HERO_SKILL_BARBARIAN_WEAKENING_STRIKE = 209
HERO_SKILL_BARBARIAN_SOIL_BURN = 210
HERO_SKILL_BARBARIAN_FOG_VEIL = 211
HERO_SKILL_BARBARIAN_INTELLIGENCE = 212
HERO_SKILL_BARBARIAN_MYSTICISM = 213
HERO_SKILL_BARBARIAN_ELITE_CASTERS = 214
HERO_SKILL_BARBARIAN_STORM_WIND = 215
HERO_SKILL_BARBARIAN_FIRE_PROTECTION = 216	
HERO_SKILL_BARBARIAN_SUN_FIRE = 217
HERO_SKILL_BARBARIAN_DISTRACT = 218
HERO_SKILL_BARBARIAN_DARK_REVELATION = 219
HERO_SKILL_BARBARIAN_MENTORING = 220

-- Skill type cannonical IDs
--
-- Basic Skills
SKILL_LOGISTICS = 1
SKILL_WAR_MACHINES = 2
SKILL_LEARNING = 3
SKILL_LEADERSHIP = 4
SKILL_LUCK = 5
SKILL_OFFENCE = 6
SKILL_DEFENCE = 7
SKILL_SORCERY = 8
SKILL_DESTRUCTIVE_MAGIC = 9
SKILL_DARK_MAGIC = 10
SKILL_LIGHT_MAGIC = 11
SKILL_SUMMONING_MAGIC = 12
-- Class skills
SKILL_TRAINING   = 13
SKILL_GATING     = 14
SKILL_NECROMANCY = 15
SKILL_AVENGER = 16
SKILL_ARTIFICIER = 17
SKILL_INVOCATION = 18
-- Perks
SKILL_PATHFINDING = 19
SKILL_SCOUTING = 20
SKILL_NAVIGATION = 21
SKILL_FIRST_AID = 22
SKILL_BALLISTA = 23
SKILL_CATAPULT = 24
SKILL_INTELLIGENCE = 25
SKILL_SCHOLAR = 26
SKILL_EAGLE_EYE = 27
SKILL_RECRUITMENT = 28
SKILL_ESTATES = 29
SKILL_DIPLOMACY = 30
SKILL_RESISTANCE = 31
SKILL_LUCKY_STRIKE = 32
SKILL_FORTUNATE_ADVENTURER = 33
SKILL_TACTICS = 34
SKILL_ARCHERY = 35
SKILL_FRENZY = 36
SKILL_PROTECTION = 37
SKILL_EVASION = 38
SKILL_TOUGHNESS = 39
SKILL_MYSTICISM = 40
SKILL_WISDOM = 41
SKILL_ARCANE_TRAINING = 42
SKILL_MASTER_OF_ICE = 43
SKILL_MASTER_OF_FIRE = 44
SKILL_MASTER_OF_LIGHTNINGS = 45
SKILL_MASTER_OF_CURSES = 46
SKILL_MASTER_OF_MIND = 47
SKILL_MASTER_OF_SICKNESS = 48
SKILL_MASTER_OF_BLESSING = 49
SKILL_MASTER_OF_ABJURATION = 50
SKILL_MASTER_OF_WRATH = 51
SKILL_MASTER_OF_QUAKES = 52
SKILL_MASTER_OF_CREATURES = 53
SKILL_MASTER_OF_ANIMATION = 54
-- Knight perks
SKILL_HOLY_CHARGE = 55
SKILL_PRAYER = 56
SKILL_EXPERT_TRAINER = 57
-- Demonlord perks
SKILL_CONSUME_CORPSE = 58
SKILL_DEMONIC_FIRE = 59
SKILL_DEMONIC_STRIKE = 60
-- Necromancer perks
SKILL_RAISE_ARCHERS          = 61
SKILL_NO_REST_FOR_THE_WICKED = 62
SKILL_DEATH_SCREAM           = 63
-- Ranger perks
SKILL_MULTISHOT = 64
SKILL_SNIPE_DEAD = 65
SKILL_IMBUE_ARROW = 66
-- Wizard perks 
SKILL_MAGIC_BOND = 67
SKILL_MELT_ARTIFACT = 68
SKILL_MAGIC_MIRROR = 69
-- Warlock perks
SKILL_EMPOWERED_SPELLS = 70
SKILL_DARK_RITUAL = 71
SKILL_ELEMENTAL_VISION = 72
-- Feats
-- Knight
SKILL_ROAD_HOME = 73
SKILL_TRIPLE_BALLISTA = 74
SKILL_ENCOURAGE = 75
SKILL_RETRIBUTION = 76
SKILL_HOLD_GROUND = 77
SKILL_GUARDIAN_ANGEL = 78
SKILL_STUDENT_AWARD = 79
SKILL_GRAIL_VISION = 80
SKILL_CASTER_CERTIFICATE = 81
SKILL_ANCIENT_SMITHY = 82
SKILL_PARIAH = 83
SKILL_ELEMENTAL_BALANCE = 84
SKILL_ABSOLUTE_CHARGE = 85
-- Demon Lord
SKILL_QUICK_GATING = 86
SKILL_MASTER_OF_SECRETS = 87
SKILL_TRIPLE_CATAPULT = 88
SKILL_GATING_MASTERY = 89
SKILL_CRITICAL_GATING = 90
SKILL_CRITICAL_STRIKE = 91
SKILL_DEMONIC_RETALIATION = 92
SKILL_EXPLODING_CORPSES = 93
SKILL_DEMONIC_FLAME = 94
SKILL_WEAKENING_STRIKE = 95
SKILL_FIRE_PROTECTION = 96
SKILL_FIRE_AFFINITY = 97
SKILL_ABSOLUTE_GATING = 98
-- Necromancer
SKILL_DEATH_TREAD = 99
SKILL_LAST_AID = 100
SKILL_LORD_OF_UNDEAD = 101
SKILL_HERALD_OF_DEATH = 102
SKILL_DEAD_LUCK = 103
SKILL_CHILLING_STEEL = 104
SKILL_CHILLING_BONES = 105
SKILL_SPELLPROOF_BONES = 106
SKILL_DEADLY_COLD = 107
SKILL_SPIRIT_LINK = 108
SKILL_TWILIGHT = 109
SKILL_HAUNT_MINE = 110
SKILL_ABSOLUTE_FEAR = 111
-- Ranger
SKILL_DISGUISE_AND_RECKON = 112
SKILL_IMBUE_BALLISTA = 113
SKILL_CUNNING_OF_THE_WOODS = 114
SKILL_FOREST_GUARD_EMBLEM = 115
SKILL_ELVEN_LUCK = 116
SKILL_FOREST_RAGE = 117
SKILL_LAST_STAND = 118
SKILL_INSIGHTS = 119
SKILL_SUN_FIRE = 120
SKILL_SOIL_BURN = 121
SKILL_STORM_WIND = 122
SKILL_FOG_VEIL = 123
SKILL_ABSOLUTE_LUCK = 124
-- Wizard
SKILL_MARCH_OF_THE_MACHINES = 125
SKILL_REMOTE_CONTROL = 126
SKILL_ACADEMY_AWARD = 127
SKILL_ARTIFICIAL_GLORY = 128
SKILL_SPOILS_OF_WAR = 129
SKILL_WILDFIRE = 130
SKILL_SEAL_OF_PROTECTION = 131
SKILL_COUNTERSPELL = 132
SKILL_MAGIC_CUSHION = 133
SKILL_SUPRESS_DARK  = 134
SKILL_SUPRESS_LIGHT  = 135
SKILL_UNSUMMON  = 136
SKILL_ABSOLUTE_WIZARDY = 137
-- warlock
SKILL_TELEPORT_ASSAULT = 138
SKILL_SHAKE_GROUND = 139
SKILL_DARK_REVELATION = 140
SKILL_FAST_AND_FURIOUS = 141
SKILL_LUCKY_SPELLS = 142
SKILL_POWER_OF_HASTE = 143
SKILL_POWER_OF_STONE = 144
SKILL_CHAOTIC_SPELLS = 145
SKILL_SECRETS_OF_DESTRUCTION = 146
SKILL_PAYBACK = 147
SKILL_ELITE_CASTERS = 148
SKILL_ELEMENTAL_OVERKILL	= 149
SKILL_ABSOLUTE_CHAINS = 150
-- runemage
SKILL_RUNELORE = 151
SKILL_REFRESH_RUNE = 152
SKILL_STRONG_RUNE = 153
SKILL_FINE_RUNE = 154
SKILL_QUICKNESS_OF_MIND = 155
SKILL_RUNIC_MACHINES = 156
SKILL_TAP_RUNES = 157
SKILL_RUNIC_ATTUNEMENT = 158
SKILL_DWARVEN_LUCK = 159
SKILL_OFFENSIVE_FORMATION = 160
SKILL_DEFENSIVE_FORMATION = 161
SKILL_DISTRACT = 162
SKILL_SET_AFIRE = 163
SKILL_SHRUG_DARKNESS = 164
SKILL_ETERNAL_LIGHT = 165
SKILL_RUNIC_ARMOR = 166
SKILL_ABSOLUTE_PROTECTION = 167
-- runmage & barbarian   cross-class
SKILL_SNATCH = 168
SKILL_MENTORING = 169
SKILL_EMPATHY = 170
SKILL_PREPARATION = 171
-- barbarian
SKILL_DEMONIC_RAGE = 172
SKILL_MIGHT_OVER_MAGIC = 173
SKILL_MEMORY_OF_OUR_BLOOD = 174
SKILL_POWERFULL_BLOW = 175
SKILL_ABSOLUTE_RAGE = 176
SKILL_PATH_OF_WAR = 177
SKILL_BATTLE_ELATION = 178
SKILL_LUCK_OF_THE_BARBARIAN = 179
SKILL_STUNNING_BLOW = 180
SKILL_DEFEND_US_ALL = 181
SKILL_GOBLIN_SUPPORT = 182
SKILL_BARBARIAN_LEARNING = 183
SKILL_POWER_OF_BLOOD = 184
SKILL_WARCRY_LEARNING = 185
SKILL_BODYBUILDING = 186
SKILL_VOICE = 187
SKILL_VOICE_TRAINING = 188
SKILL_MIGHTY_VOICE = 189
SKILL_VOICE_OF_RAGE = 190
SKILL_SHATTER_DESTRUCTIVE_MAGIC = 191
SKILL_CORRUPT_DESTRUCTIVE = 192
SKILL_WEAKEN_DESTRUCTIVE = 193
SKILL_DETAIN_DESTRUCTIVE = 194
SKILL_SHATTER_DARK_MAGIC = 195
SKILL_CORRUPT_DARK = 196
SKILL_WEAKEN_DARK = 197
SKILL_DETAIN_DARK = 198
SKILL_SHATTER_LIGHT_MAGIC = 199
SKILL_CORRUPT_LIGHT = 200
SKILL_WEAKEN_LIGHT = 201
SKILL_DETAIN_LIGHT = 202
SKILL_SHATTER_SUMMONING_MAGIC = 203
SKILL_CORRUPT_SUMMONING = 204
SKILL_WEAKEN_SUMMONING = 205
SKILL_DETAIN_SUMMONING = 206
SKILL_DEATH_TO_NONEXISTENT = 207
SKILL_BARBARIAN_ANCIENT_SMITHY = 208
SKILL_BARBARIAN_WEAKENING_STRIKE = 209
SKILL_BARBARIAN_SOIL_BURN = 210
SKILL_BARBARIAN_FOG_VEIL = 211
SKILL_BARBARIAN_INTELLIGENCE = 212
SKILL_BARBARIAN_MYSTICISM = 213
SKILL_BARBARIAN_ELITE_CASTERS = 214
SKILL_BARBARIAN_STORM_WIND = 215
SKILL_BARBARIAN_FIRE_PROTECTION = 216	
SKILL_BARBARIAN_SUN_FIRE = 217
SKILL_BARBARIAN_DISTRACT = 218
SKILL_BARBARIAN_DARK_REVELATION = 219
SKILL_BARBARIAN_MENTORING = 220

--
-- Town type IDs
--
TOWN_HEAVEN = 0
TOWN_PRESERVE = 1
TOWN_ACADEMY = 2
TOWN_DUNGEON = 3
TOWN_NECROMANCY = 4
TOWN_INFERNO = 5
TOWN_FORTRESS = 6
TOWN_STRONGHOLD = 7

--
-- Town buildings IDs
--
TOWN_BUILDING_TOWN_HALL = 0
TOWN_BUILDING_FORT = 1
TOWN_BUILDING_MARKETPLACE = 2	
TOWN_BUILDING_SHIPYARD = 3
TOWN_BUILDING_TAVERN = 4
TOWN_BUILDING_BLACKSMITH = 5
TOWN_BUILDING_MAGIC_GUILD = 6
TOWN_BUILDING_DWELLING_1 = 7
TOWN_BUILDING_DWELLING_2 = 8
TOWN_BUILDING_DWELLING_3 = 9
TOWN_BUILDING_DWELLING_4 = 10
TOWN_BUILDING_DWELLING_5 = 11
TOWN_BUILDING_DWELLING_6 = 12
TOWN_BUILDING_DWELLING_7 = 13
TOWN_BUILDING_GRAIL = 14
TOWN_BUILDING_WONDER = 15
TOWN_BUILDING_SPECIAL_0 = 16
TOWN_BUILDING_SPECIAL_1 = 17
TOWN_BUILDING_SPECIAL_2 = 18
TOWN_BUILDING_SPECIAL_3 = 19
TOWN_BUILDING_SPECIAL_4 = 20
TOWN_BUILDING_SPECIAL_5 = 21
TOWN_BUILDING_SPECIAL_6 = 22
TOWN_BUILDING_SPECIAL_7 = 23
TOWN_BUILDING_SPECIAL_8 = 24
TOWN_BUILDING_SPECIAL_9 = 25

TOWN_BUILDING_HAVEN_TRAINING_GROUNDS 			= TOWN_BUILDING_SPECIAL_1
TOWN_BUILDING_HAVEN_MONUMENT_TO_FALLEN_HEROES 	= TOWN_BUILDING_SPECIAL_2
TOWN_BUILDING_HAVEN_HOSPITAL 					= TOWN_BUILDING_SPECIAL_3
TOWN_BUILDING_HAVEN_STABLE 						= TOWN_BUILDING_SPECIAL_4
TOWN_BUILDING_HAVEN_FARMS 						= TOWN_BUILDING_SPECIAL_5
TOWN_BUILDING_INFERNO_INFERNAL_LOOM 			= TOWN_BUILDING_SPECIAL_1
TOWN_BUILDING_INFERNO_ORDER_OF_FIRE 			= TOWN_BUILDING_SPECIAL_3
TOWN_BUILDING_INFERNO_HALLS_OF_HORROR 			= TOWN_BUILDING_SPECIAL_4
TOWN_BUILDING_INFERNO_SACRIFICIAL_PIT 			= TOWN_BUILDING_SPECIAL_5
TOWN_BUILDING_DUNGEON_ALTAR_OF_ELEMENTS 		= TOWN_BUILDING_SPECIAL_1
TOWN_BUILDING_DUNGEON_RITUAL_PIT 				= TOWN_BUILDING_SPECIAL_3
TOWN_BUILDING_DUNGEON_TRADE_GUILD				= TOWN_BUILDING_SPECIAL_4
TOWN_BUILDING_DUNGEON_TREASURE_DIG_SITE 		= TOWN_BUILDING_SPECIAL_5
TOWN_BUILDING_DUNGEON_HALL_OF_INTRIGUE 			= TOWN_BUILDING_SPECIAL_6
TOWN_BUILDING_ACADEMY_LIBRARY 					= TOWN_BUILDING_SPECIAL_1
TOWN_BUILDING_ACADEMY_ARCANE_FORGE 				= TOWN_BUILDING_SPECIAL_2
TOWN_BUILDING_ACADEMY_ARTIFACT_MERCHANT			= TOWN_BUILDING_SPECIAL_3
TOWN_BUILDING_ACADEMY_TREASURE_CAVE 			= TOWN_BUILDING_SPECIAL_4
TOWN_BUILDING_ACADEMY_ELEMENTAL_ENCLAVE 		= TOWN_BUILDING_SPECIAL_5
TOWN_BUILDING_PRESERVE_AVENGERS_BROTHERHOOD		= TOWN_BUILDING_SPECIAL_0
TOWN_BUILDING_PRESERVE_MYSTIC_POND 				= TOWN_BUILDING_SPECIAL_2
TOWN_BUILDING_PRESERVE_SPARKLING_FONTAINS 		= TOWN_BUILDING_SPECIAL_3
TOWN_BUILDING_PRESERVE_BLOOMING_GROVE 			= TOWN_BUILDING_SPECIAL_4
TOWN_BUILDING_PRESERVE_TREANT_SAMPLING 			= TOWN_BUILDING_SPECIAL_5
TOWN_BUILDING_NECROMANCY_AMPLIFIER 				= TOWN_BUILDING_SPECIAL_1
TOWN_BUILDING_NECROMANCY_UNHOLY_TEMPLE 			= TOWN_BUILDING_SPECIAL_2
TOWN_BUILDING_NECROMANCY_UNEARHED_GRAVES 		= TOWN_BUILDING_SPECIAL_3
TOWN_BUILDING_NECROMANCY_DRAGON_TOMBSTONE 		= TOWN_BUILDING_SPECIAL_4
TOWN_BUILDING_NECROMANCY_SHROUD_OF_DARKNESS 	= TOWN_BUILDING_SPECIAL_5
TOWN_BUILDING_FORTRESS_RUNIC_SHRINE 		= TOWN_BUILDING_SPECIAL_1;
TOWN_BUILDING_FORTRESS_ARENA 			= TOWN_BUILDING_SPECIAL_2;
TOWN_BUILDING_FORTRESS_GUARDPOST 		= TOWN_BUILDING_SPECIAL_3;
TOWN_BUILDING_FORTRESS_RUNIC_STONEWORKS 	= TOWN_BUILDING_SPECIAL_4;
TOWN_BUILDING_FORTRESS_RUNIC_ACADEMY 		= TOWN_BUILDING_SPECIAL_5;
TOWN_BUILDING_STRONGHOLD_HALL_OF_TRIAL			= TOWN_BUILDING_SPECIAL_1
TOWN_BUILDING_STRONGHOLD_GARBAGE_PILE			= TOWN_BUILDING_SPECIAL_2
TOWN_BUILDING_STRONGHOLD_TRAVELLERS_SHELTER	= TOWN_BUILDING_SPECIAL_3
TOWN_BUILDING_STRONGHOLD_PILE_OF_OUR_FOES		= TOWN_BUILDING_SPECIAL_4
TOWN_BUILDING_STRONGHOLD_SLAVE_MARKET			= TOWN_BUILDING_SPECIAL_5

--
-- Monster mood IDs
--
MONSTER_MOOD_FRIENDLY = 0
MONSTER_MOOD_AGGRESSIVE = 1
MONSTER_MOOD_HOSTILE = 2
MONSTER_MOOD_WILD = 3

--
-- Monster courage IDs
--
MONSTER_COURAGE_ALWAYS_JOIN = 0
MONSTER_COURAGE_ALWAYS_FIGHT = 1
MONSTER_COURAGE_CAN_FLEE_JOIN = 2

--
-- Borderguard key colors
--
RED_KEY = 1
BLUE_KEY = 2
GREEN_KEY = 3
YELLOW_KEY = 4
ORANGE_KEY = 5
TEAL_KEY = 6
PURPLE_KEY = 7
TAN_KEY = 8

--
-- Trigger type IDs
--
NEW_DAY_TRIGGER = 0
PLAYER_ADD_HERO_TRIGGER = 1
PLAYER_REMOVE_HERO_TRIGGER = 2
OBJECTIVE_STATE_CHANGE_TRIGGER = 3
OBJECT_TOUCH_TRIGGER = 4
OBJECT_CAPTURE_TRIGGER = 5
REGION_ENTER_AND_STOP_TRIGGER = 6
REGION_ENTER_WITHOUT_STOP_TRIGGER = 7
HERO_LEVELUP_TRIGGER = 8
WAR_FOG_ENTER_TRIGGER = 9
COMBAT_RESULTS_TRIGGER = 11
CUSTOM_ABILITY_TRIGGER = 12
REGION_EXIT_TRIGGER = 13
HERO_ADD_SKILL_TRIGGER = 14
HERO_REMOVE_SKILL_TRIGGER = 15
HERO_TOUCH_TRIGGER = 16  -- works only for heroes disabled by SetObjectEnabled function

--
-- Saved combat results types
--
COMBAT_RESULT_NONE = 0
COMBAT_RESULT_WIN = 1
COMBAT_RESULT_RETREAT = 2
COMBAT_RESULT_SURRENDER = 3

--
-- Custom abilities IDs
--
CUSTOM_ABILITY_1 = 1
CUSTOM_ABILITY_2 = 2
CUSTOM_ABILITY_3 = 3
CUSTOM_ABILITY_4 = 4

--
-- Custom abilities modes
--
CUSTOM_ABILITY_NOT_PRESENT = -1
CUSTOM_ABILITY_DISABLED = 0
CUSTOM_ABILITY_ENABLED = 1

--
-- Moon weeks (for GetCurrentMoonWeek adventure script function)
--
WEEK_OF_NOTHING = 0
WEEK_OF_TOAD = 1
WEEK_OF_SALAMANDER = 2
WEEK_OF_BEETLE = 3
WEEK_OF_WYVERN = 4
WEEK_OF_DRAGONFLY = 5
WEEK_OF_FOX = 6
WEEK_OF_SHAMAN = 7
WEEK_OF_RABBIT = 8
WEEK_OF_SQUIRREL = 9
WEEK_OF_CATERPILLAR = 10
WEEK_OF_HAMSTER = 11
WEEK_OF_PIGEON = 12
WEEK_OF_RAGE = 13
WEEK_OF_EAGLE = 14
WEEK_OF_BEE = 15
WEEK_OF_WASP = 16
WEEK_OF_SWAN = 17
WEEK_OF_BUTTERFLY = 18
WEEK_OF_THANE = 19
WEEK_OF_ANTILOPE = 20
WEEK_OF_ORC = 21
WEEK_OF_RAVEN = 22
WEEK_OF_BADGER = 23
WEEK_OF_FLAMINGO = 24
WEEK_OF_TORTOISE = 25
WEEK_OF_LYNX = 26
WEEK_OF_PENGUIN = 27
WEEK_OF_FALCON = 28
WEEK_OF_HEDGEHOG = 29
WEEK_OF_SPARROW = 30
WEEK_OF_SWALLOW = 31
WEEK_OF_LION = 32
WEEK_OF_SPEARS = 33
WEEK_OF_BEAR = 34
WEEK_OF_CHIEFTAIN = 35
WEEK_OF_CENTAUR = 36
WEEK_OF_GOBLIN = 37
WEEK_OF_DEER = 38
WEEK_OF_OWL = 39
WEEK_OF_DEFENDER = 40
WEEK_OF_WYRM = 41
WEEK_OF_TIGER = 42
WEEK_OF_PLAGUE = 43
WEEK_OF_DISEASE = 44
WEEK_OF_FEVER = 45
WEEK_OF_FLAME = 46
WEEK_OF_WINDS = 47
WEEK_OF_FOLLY = 48
WEEK_OF_HONOR = 49
WEEK_OF_DIPLOMACY = 50
WEEK_OF_FORGERY = 51
WEEK_OF_TRADE = 52
WEEK_OF_MEDITATION = 53
WEEK_OF_LIFE = 54
WEEK_OF_CONJUNCTION = 55
WEEK_OF_JEWELS = 56
WEEK_OF_ALCHEMY = 57
WEEK_OF_GOLD = 58
WEEK_OF_FESTIVALS = 59
WEEK_OF_HARVEST = 60
WEEK_OF_IDLENESS = 61
WEEK_OF_MAGIC = 62
WEEK_OF_FEEBLENESS = 63
WEEK_OF_SORROW = 64
WEEK_OF_CHAOS = 65
WEEK_OF_CALM = 66
WEEK_OF_HOPE = 67
WEEK_OF_WATER = 68
WEEK_OF_FIRE = 69
WEEK_OF_EARTH = 70
WEEK_OF_AIR = 71
WEEK_OF_FIRENICE = 72
WEEK_OF_MIGHT = 73
WEEK_OF_BALANCE = 74
WEEK_OF_MIGHTNMAGIC = 75
WEEK_OF_INFIRMITY = 76
WEEK_OF_LIGHT = 77
WEEK_OF_EVOCATION = 78
WEEK_OF_ABJURATION = 79
WEEK_OF_ALTERATION = 80
WEEK_OF_CONJURATION = 81
WEEK_OF_ETHER = 82
WEEK_OF_TOUGHNESS = 83
WEEK_OF_PEASANT = 84
WEEK_OF_ARCHER = 85
WEEK_OF_FOOTMAN = 86
WEEK_OF_GRIFFIN = 87
WEEK_OF_PRIEST = 88
WEEK_OF_CAVALIER = 89
WEEK_OF_ANGEL = 90
WEEK_OF_GREMLIN = 91
WEEK_OF_GARGOYLE = 92
WEEK_OF_GOLEM = 93
WEEK_OF_MAGI = 94
WEEK_OF_GENIE = 95
WEEK_OF_RAKSHASA = 96
WEEK_OF_GIANT = 97
WEEK_OF_PIXIE = 98
WEEK_OF_WARDANCER = 99
WEEK_OF_WOODELF = 100
WEEK_OF_DRUID = 101
WEEK_OF_UNICORN = 102
WEEK_OF_TREANT = 103
WEEK_OF_GREENDRAGON = 104
WEEK_OF_IMP = 105
WEEK_OF_DEMON = 106
WEEK_OF_HELLHOUND = 107
WEEK_OF_SUCCUBUS = 108
WEEK_OF_NIGHTMARE = 109
WEEK_OF_BALOR = 110
WEEK_OF_DEVIL = 111
WEEK_OF_ASSASSIN = 112
WEEK_OF_WITCH = 113
WEEK_OF_MINOTAUR = 114
WEEK_OF_RIDER = 115
WEEK_OF_HYDRA = 116
WEEK_OF_MATRON = 117
WEEK_OF_DRAGON = 118
WEEK_OF_SKELETON = 119
WEEK_OF_WALKINGDEAD = 120
WEEK_OF_WIGHT = 121
WEEK_OF_VAMPIRE = 122
WEEK_OF_LICH = 123
WEEK_OF_GHOST = 124
WEEK_OF_BONEDRAGON = 125

-- Animation Action Types
--
--INVISIBLE = 0
IDLE = 1
ONESHOT_STILL = 2
ONESHOT = 3
--MOVE = 4
NON_ESSENTIAL = 5

-- Monsters names filter
MONSTER_NAME_SINGLE = 0
MONSTER_NAME_MULTIPLE = 1
MONSTER_NAMES_ALL = 2

-- Disabled interactive objects modes
DISABLED_DEFAULT = 0
DISABLED_ATTACK = 1
DISABLED_INTERACT = 2
DISABLED_BLOCKED = 3

-- Region Auto Action modes
REGION_AUTOACTION_ON_ENTER = 1
REGION_AUTOACTION_ON_EXIT = 2

-- Region Auto Action enable variants
REGION_AUTOACTION_OBJECT_NO_ACTION = -1
REGION_AUTOACTION_OBJECT_DISABLE = 0
REGION_AUTOACTION_OBJECT_ENABLE = 1

-- Heroes Roles Modes
--
-- NOTE: for SetHeroRoleMode(heroName,roleMode) script commmand
--
HERO_ROLE_MODE_REGULAR = 0
HERO_ROLE_MODE_FREEMAN = 1	-- always Freelancer
HERO_ROLE_MODE_HERMIT  = 2	-- always Freelancer, never interact with other heroes

--
-- Players filtering constants (you can sum PLAYERFLT_1..8, but not PLAYERFLT_TEAM_1..8)
--
PLAYERFLT_1 = 1
PLAYERFLT_2 = 2
PLAYERFLT_3 = 4
PLAYERFLT_4 = 8
PLAYERFLT_5 = 16
PLAYERFLT_6 = 32
PLAYERFLT_7 = 64
PLAYERFLT_8 = 128
PLAYERFLT_ALL = 255
PLAYERFLT_TEAM_1 = -1
PLAYERFLT_TEAM_2 = -2
PLAYERFLT_TEAM_3 = -3
PLAYERFLT_TEAM_4 = -4
PLAYERFLT_TEAM_5 = -5
PLAYERFLT_TEAM_6 = -6
PLAYERFLT_TEAM_7 = -7
PLAYERFLT_TEAM_8 = -8

--
-- Players Teams constants
--
PLAYERS_TEAM_1 = 1
PLAYERS_TEAM_2 = 2
PLAYERS_TEAM_3 = 3
PLAYERS_TEAM_4 = 4
PLAYERS_TEAM_5 = 5
PLAYERS_TEAM_6 = 6
PLAYERS_TEAM_7 = 7
PLAYERS_TEAM_8 = 8

--
-- Hero battle bonuses IDs
--
HERO_BATTLE_BONUS_LUCK = 0
HERO_BATTLE_BONUS_MORALE = 1
HERO_BATTLE_BONUS_ATTACK = 2
HERO_BATTLE_BONUS_DEFENCE = 3
HERO_BATTLE_BONUS_HITPOINTS = 4
HERO_BATTLE_BONUS_INITIATIVE = 5
HERO_BATTLE_BONUS_SPEED = 6

function createAdvmapAliases()
--
-- dumb command aliasing
--
names = GetAllNames
GiveExpToLevel = LevelUpHero
Exists = IsObjectExists
GetObjectPos = GetObjectPosition
SetObjectPos = SetObjectPosition
CreateMob = CreateMonster
GenerateMobs = GenerateMonsters
KillMobs = RemoveAllMonsters
CalcAverageTier = CalcAverageMonstersTier
SetLight = SetAmbientLight
SetCombatLight = SetCombatAmbientLight
ShowFlyMessage = ShowFlyingSign
Trigger = SetTrigger
ExecConsoleCommand = consoleCmd
SetCombatLight = SetCombatAmbientLight
GiveArtifact = GiveArtefact
end

MakeSyncCommandCallback = function(event_id)
    return function() mark_event(%event_id)	end
end

SyncCommand = function(command, arg, callback, saveName)
    if saveName == nil then
        saveName = ''
    end
    local event = make_event()
    command(arg, 'MakeSyncCommandCallback(' .. event .. ')', saveName)
    wait_event(event)
    if callback and callback ~= '' then
        parse(callback .. '()')()
    end
end

if MessageBoxInt then
    MessageBox = function(name, callback) SyncCommand(MessageBoxInt, name, callback) end
end
if QuestionBoxInt then
    QuestionBox = QuestionBoxInt
--	QuestionBox = function(name, callback) SyncCommand(QuestionBoxInt, name, callback) end
end
if StartCutSceneInt then
    StartCutScene = function(name, callback, saveName) SyncCommand(StartCutSceneInt, name, callback, saveName) end
end
if StartDialogSceneInt then
    StartDialogScene = function(name, callback, saveName) SyncCommand(StartDialogSceneInt, name, callback, saveName) end
end
doFile("/scripts/advmap-common.lua")
