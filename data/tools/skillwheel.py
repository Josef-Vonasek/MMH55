from collections import defaultdict
from fileinput import filename
from os import utime, walk
from xdb import XDB
from math import sin, cos, radians

OFFENCE = 'OFFENCE'
DEFENCE = 'DEFENCE'
LUCK = 'LUCK'
LEADERSHIP = 'LEADERSHIP'
MACHINES = 'WAR_MACHINES'
COMBAT = 'TRAINING'
LOGISTICS = 'LOGISTICS'
LEARNING = 'LEARNING'
SORCERY = 'SORCERY'
INVOCATION = 'INVOCATION'
STAMINA = 'EXPERT_TRAINER'
RUSH = 'WARCRY_LEARNING'
FAITH = 'SHATTER_DARK_MAGIC'
SUMMON = 'SUMMONING_MAGIC'
CHAOS = 'DESTRUCTIVE_MAGIC'
DARK = 'DARK_MAGIC'
LIGHT = 'LIGHT_MAGIC'
GATING = 'GATING'
NECROMANCY = 'NECROMANCY'
AVENGER = 'AVENGER'
ARTIFICIER = 'ARTIFICIER'
RUNELORE = 'RUNELORE'
RAGE = 'DEMONIC_RAGE'
VOICE = 'VOICE'

SKILLS = {
    OFFENCE: ( 'FAST_AND_FURIOUS',  'FRENZY', 'TACTICS', 'CHILLING_STEEL', 'OFFENSIVE_FORMATION', 'ARCHERY' ), 
    DEFENCE: ( 'DEFENSIVE_FORMATION', 'HOLD_GROUND', 'LAST_STAND', 'EVASION', 'PROTECTION', 'SPELLPROOF_BONES' ), 
    LUCK: ( 'ELVEN_LUCK', 'LUCKY_STRIKE', 'DEAD_LUCK', 'DARK_REVELATION', 'CHAOTIC_SPELLS', 'LUCKY_SPELLS' ),
    STAMINA: ( 'TOUGHNESS', 'PREPARATION', 'RESISTANCE', 'DWARVEN_LUCK', 'POWER_OF_STONE', 'BODYBUILDING' ), 
    RUSH: ( 'POWER_OF_HASTE', 'TELEPORT_ASSAULT', 'SNATCH', 'DEATH_TREAD', 'WILDFIRE', 'RUNIC_MACHINES' ), 
    LOGISTICS: ( 'DISGUISE_AND_RECKON', 'REMOTE_CONTROL', 'PATHFINDING', 'NAVIGATION', 'GRAIL_VISION', 'ESTATES' ),

    FAITH: ( 'DETAIN_SUMMONING', 'BARBARIAN_FOG_VEIL', 'DETAIN_DESTRUCTIVE', 'BARBARIAN_ANCIENT_SMITHY', 'DETAIN_LIGHT', 'BARBARIAN_STORM_WIND', 'DETAIN_DARK', 'BARBARIAN_SOIL_BURN' ),
    MACHINES: ( 'BALLISTA', 'TRIPLE_BALLISTA', 'FIRST_AID', 'LAST_AID', 'CATAPULT', 'TRIPLE_CATAPULT' ), 
    LEARNING: ( 'SCOUTING', 'QUICKNESS_OF_MIND', 'SCHOLAR', 'MENTORING', 'INTELLIGENCE', 'COUNTERSPELL' ),

    COMBAT: ( 'HOLY_CHARGE', 'CRITICAL_STRIKE', 'STUNNING_BLOW', 'POWERFULL_BLOW','DEMONIC_STRIKE', 'BARBARIAN_WEAKENING_STRIKE' ),
    LEADERSHIP: ( 'RECRUITMENT', 'DIPLOMACY', 'ENCOURAGE', 'PRAYER', 'RAISE_ARCHERS', 'ROAD_HOME' ),

    SORCERY: ( 'MAGIC_BOND', 'ELITE_CASTERS', 'WISDOM', 'EAGLE_EYE', 'ARCANE_TRAINING', 'PAYBACK' ), 
    INVOCATION: ( 'EMPOWERED_SPELLS', 'DISTRACT', 'CONSUME_CORPSE', 'EXPLODING_CORPSES', 'DARK_RITUAL', 'PARIAH' ), 
 
    #'SHATTER_LIGHT_MAGIC': ( 'DEFENSIVE_FORMATION', 'EVASION', 'PROTECTION', 'SPELLPROOF_BONES', 'TOUGHNESS', 'HOLDGROUND' ), 
    SUMMON: ( 'ELEMENTAL_BALANCE', 'FOG_VEIL' , 'SUN_FIRE', 'FIRE_AFFINITY', 'MASTER_OF_QUAKES', 'SHAKE_GROUND'),
    CHAOS: ( 'DEADLY_COLD', 'MASTER_OF_ICE', 'MASTER_OF_FIRE',  'SET_AFIRE', 'ANCIENT_SMITHY', 'MASTER_OF_LIGHTNINGS' ),
    DARK: ( 'MASTER_OF_SICKNESS', 'SPIRIT_LINK', 'WEAKENING_STRIKE', 'MASTER_OF_MIND', 'MASTER_OF_CURSES',  'SOIL_BURN' ), 
    LIGHT: ( 'MASTER_OF_ABJURATION', 'ETERNAL_LIGHT', 'TWILIGHT',  'MASTER_OF_WRATH', 'MASTER_OF_BLESSING', 'GUARDIAN_ANGEL'), 

    GATING: ( 'SPOILS_OF_WAR', 'PATH_OF_WAR', 'GATING_MASTERY', 'CRITICAL_GATING', 'DEMONIC_FIRE', 'QUICK_GATING' ),
    NECROMANCY: ( 'DEATH_SCREAM', 'SHRUG_DARKNESS', 'NO_REST_FOR_THE_WICKED', 'LORD_OF_UNDEAD', 'CHILLING_BONES', 'HERALD_OF_DEATH' ), # 'HAUNT_MINE'
    AVENGER: ( 'FOREST_RAGE', 'FOREST_GUARD_EMBLEM', 'IMBUE_ARROW', 'IMBUE_BALLISTA', 'SNIPE_DEAD', 'MULTISHOT' ), 
    ARTIFICIER: ( 'ACADEMY_AWARD', 'SUPRESS_LIGHT', 'MELT_ARTIFACT', 'MAGIC_MIRROR', 'ARTIFICIAL_GLORY', 'MARCH_OF_THE_MACHINES' ),
    RUNELORE: ( 'DEMONIC_FLAME', 'RUNIC_ATTUNEMENT', 'FINE_RUNE', 'TAP_RUNES', 'FORTUNATE_ADVENTURER', 'STRONG_RUNE'),
    RAGE: ( 'POWER_OF_BLOOD',  'MIGHT_OVER_MAGIC', 'BATTLE_ELATION', 'MEMORY_OF_OUR_BLOOD', 'GOBLIN_SUPPORT', 'DEFEND_US_ALL' ),

    VOICE: ( 'MIGHTY_VOICE', 'VOICE_OF_RAGE', 'BARBARIAN_MYSTICISM', 'BARBARIAN_DISTRACT', 'VOICE_TRAINING', 'BARBARIAN_ELITE_CASTERS' ),
}

ULTIMATES = {
    # STORM_WIND, MAGIC_CUSHION, UNSUMMON, 
    OFFENCE: 'WEAKEN_DESTRUCTIVE',  # DragonForm - 2 Dragons # 
    DEFENCE: 'SHATTER_SUMMONING_MAGIC',  # Benedicted - Visit Monastery
    LUCK: 'ABSOLUTE_LUCK',  # Absolute Protection - 2 Armors
    STAMINA: 'CORRUPT_DARK', # High Ground - 2 Boots
    RUSH: 'EMPATHY',  # Dodge - 2 INI items
    LOGISTICS: 'CORRUPT_DESTRUCTIVE',  # Charge & Governor - 2 Boots

    FAITH: 'ABSOLUTE_PROTECTION', # Join - 2 Saint # 
    MACHINES: 'WEAKEN_SUMMONING',#'RUNELORE',  # Steroids - 2 Dragons
    LEARNING: 'ABSOLUTE_WIZARDY',  # Spells - 2 Books

    COMBAT: 'ABSOLUTE_CHARGE',  # Anti Magic - 2 resists
    LEADERSHIP: 'RETRIBUTION',  # Empathy - 2 Lions

    SORCERY: 'MYSTICISM',  # Hexing - 2 staffs
    INVOCATION: 'WEAKEN_DARK',  # Vampirism - 2 Necro

    SUMMON: 'MASTER_OF_CREATURES',
    CHAOS: 'SHATTER_DESTRUCTIVE_MAGIC',
    DARK: 'SHATTER_LIGHT_MAGIC',
    LIGHT: 'RUNIC_ARMOR',
    
    GATING: 'WEAKEN_LIGHT', # Instant
    NECROMANCY: 'WEAKEN_LIGHT', # Horror
    AVENGER: 'WEAKEN_LIGHT', # CUNNING_OF_THE_WOODS
    ARTIFICIER: 'WEAKEN_LIGHT',
    RUNELORE: 'WEAKEN_LIGHT',

    VOICE: 'WEAKEN_DARK',

    RAGE: 'ABSOLUTE_RAGE', 

    'ABSOLUTE_GATING': 'ABSOLUTE_GATING',
    'ABSOLUTE_FEAR': 'ABSOLUTE_FEAR',
}

SKIP = defaultdict(list, {
    'POWER_OF_HASTE': [ 'BARBARIAN' ],
    'TELEPORT_ASSAULT': [ 'BARBARIAN' ],
})


MIGHT = [COMBAT, LEADERSHIP, MACHINES]
MAGE1 = [SORCERY, INVOCATION, MACHINES]
MAGE2 = [SORCERY, INVOCATION, CHAOS]
def BASIC(replace):
    BASIC = [OFFENCE, DEFENCE, LUCK, STAMINA, RUSH, LOGISTICS] + [FAITH, LEARNING]
    return [replace[s] if s in replace else s for s in BASIC]

HEROES = {
    'KNIGHT':       ('H', 1, (40,25,25), OFFENCE    , BASIC({})                + [COMBAT, INVOCATION, MACHINES, DARK]), # RENEGADE
    'RANGER':       ('H', 2, (30,40,15), LIGHT      , BASIC({})                + MIGHT + [LIGHT]), # KNIGHT
    'HERETIC':      ('H', 3, (25,10,40), LEARNING   , BASIC({})                + MAGE2 + [DARK, SUMMON]), # HERETIC
    'WIZARD':       ('I', 1, (50,25,10), COMBAT     , BASIC({DEFENCE: DARK})   + MIGHT + [GATING]), # DEMON LORD
    'DEMON_LORD':   ('I', 2, (35,15,30), GATING     , BASIC({OFFENCE: DARK})   + MAGE1 + [GATING, CHAOS]), # GATEKEEPER
    'SORCERER':     ('I', 3, (15,10,45), SORCERY    , BASIC({STAMINA: DARK})   + MAGE2 + [GATING, SUMMON]), # SORCERER
    'RUNEMAGE':     ('N', 1, (35,35,20), RUSH       , BASIC({})                + [COMBAT, INVOCATION, DARK, NECROMANCY]), # DEATH KNIGHT
    'NECROMANCERA': ('N', 2, (15,25,35), NECROMANCY , BASIC({})                + MAGE2 + [NECROMANCY, DARK]), # NECROMANCER
    'REAVER':       ('N', 3, (10,15,50), LOGISTICS  , BASIC({RUSH: DARK})      + MAGE2 + [NECROMANCY, SUMMON]), # NETHERMAGE
    'BEASTMASTER':  ('D', 1, (40,30,15), LEADERSHIP , BASIC({})                + MIGHT + [DARK]), # OVERLORD
    'SEER':         ('D', 2, (30,10,40), LUCK       , BASIC({STAMINA: DARK})   + MAGE1 + [NECROMANCY, CHAOS]), # TRICKSTER
    'WARLOCK':      ('D', 3, (15,10,50), INVOCATION , BASIC({OFFENCE: DARK})   + MAGE2 + [NECROMANCY, SUMMON]), # WARLOCK
    'RANGERA':      ('S', 1, (45,30,10), DEFENCE    , BASIC({STAMINA: LIGHT})  + MIGHT + [AVENGER]), # RANGER
    'WARDEN':       ('S', 2, (35,25,15), AVENGER    , BASIC({RUSH: DARK})      + MIGHT + [AVENGER, CHAOS]), # AVENGER
    'ENCHANTER':    ('S', 3, (10,20,40), LEARNING   , BASIC({})                + MAGE2 + [LIGHT, SUMMON]), # DRUID
    'GUILDMASTER':  ('A', 1, (35,25,10), LOGISTICS  , BASIC({LUCK: LIGHT})     + [DARK, LEADERSHIP, MACHINES, ARTIFICIER]), # ENCHANTER
    'ELEMENTALIST': ('A', 2, ( 5,35,30), ARTIFICIER , BASIC({OFFENCE: CHAOS})  + MAGE1 + [ARTIFICIER, SUMMON]), # CONJURER
    'WIZARDA':      ('A', 3, ( 5,15,40), SORCERY    , BASIC({FAITH: DARK})     + MAGE2 + [ARTIFICIER, SUMMON]), # WIZARD
    'NECROMANCER':  ('F', 1, (35,45,10), MACHINES   , BASIC({LEARNING: LIGHT}) + MIGHT + [RUNELORE]), # ENGINEER
    'FLAMEKEEPERA': ('F', 2, (30,20,30), RUNELORE   , BASIC({LEARNING: DARK})  + MAGE1 + [RUNELORE, CHAOS]), # FLAMEKEEPER
    'RUNEMAGEA':    ('F', 3, (10,15,45), STAMINA    , BASIC({LUCK: LIGHT})     + MAGE2 + [RUNELORE, SUMMON]), # RUNEMAGE
    'BARBARIAN':    ('B', 1, (50,35, 0), RAGE       , BASIC({RUSH: VOICE})     + MIGHT + [RAGE]), # CHIEFTAN
    'SHAMAN':       ('B', 2, (20,20,30), DARK       , BASIC({RUSH: DARK})      + MIGHT + [RAGE, INVOCATION]), # SHAMAN
    'WARLOCKB':     ('B', 3, (20,10,40), FAITH      , BASIC({LUCK: LIGHT})     + MAGE2 + [NECROMANCY, SUMMON]), # WITCH
}

DUELS = {
    'AcademyPreset1': ('A', LIGHT, {LIGHT:(0,2), LEARNING:(0,2), ARTIFICIER:(1,2), LEADERSHIP:(1,0), DEFENCE:(1,2), RUSH:(0,1)}),
    'AcademyPreset2': ('A', GATING, {RUSH:(0,1), LEARNING:(0,2), SORCERY:(0,2), DEFENCE:(1,2), ARTIFICIER:(1,2), STAMINA:(0,2)}),
    'AcademyPreset3': ('A', LUCK, {CHAOS:(0,2), LEARNING:(0,2), SORCERY:(0,2), DEFENCE:(1,2), INVOCATION:(0,1), STAMINA:(0,1)}),
    'AdvMapHero1': ('H', RUSH, {DARK:(0,2), LEADERSHIP:(1,0), COMBAT:(1,0), RUSH:(0,1), DEFENCE:(1,2), OFFENCE:(2,0)}),
    'AdvMapHero2': ('H', GATING, {LIGHT:(0,2), LEARNING:(0,2), COMBAT:(1,0), LEADERSHIP:(1,0), DEFENCE:(1,2), RUSH:(0,1)}),
    'AdvMapHero3': ('H', OFFENCE, {DARK:(0,2), LEARNING:(0,2), SORCERY:(0,2), STAMINA:(0,1), OFFENCE:(2,0), RUSH:(0,1)}),
    'DungeonPreset1': ('D', COMBAT, {DARK:(0,2), COMBAT:(1,0), LEADERSHIP:(1,0), DEFENCE:(1,2), OFFENCE:(2,0), RUSH:(0,1)}),
    'DungeonPreset2': ('D', GATING, {CHAOS:(0,2), LEARNING:(0,2), SORCERY:(0,2), LUCK:(0,1), DEFENCE:(1,2), STAMINA:(0,1)}),
    'DungeonPreset3': ('D', CHAOS, {CHAOS:(0,2),  SORCERY:(0,2), INVOCATION:(0,1), DEFENCE:(1,2), OFFENCE:(2,0), STAMINA:(0,1)}),
    'InfernoPreset1': ('I', GATING, {DARK:(0,2), LEARNING:(0,2), GATING:(2,1), LEADERSHIP:(1,0), COMBAT:(2,0), STAMINA:(0,1)}),
    'InfernoPreset2': ('I', 'ABSOLUTE_GATING', {SUMMON:(1,0), GATING:(2,1), SORCERY:(0,2),DEFENCE:(1,2), RUSH:(0,1), OFFENCE:(1,0)}),
    'InfernoPreset3': ('I', DARK, {CHAOS:(0,2), LEARNING:(0,2), SORCERY:(0,2), STAMINA:(0,1), GATING:(2,1), RUSH:(0,1)}),
    'NecropolisPreset1': ('N', GATING, {DARK:(0,2), LEARNING:(1,0), DEFENCE:(1,2), FAITH:(3,2), RUSH:(0,1), OFFENCE:(1,0)}),
    'NecropolisPreset2': ('N', 'ABSOLUTE_FEAR', {DARK:(0,2), NECROMANCY:(0,2), SORCERY:(0,2), OFFENCE:(1,0), RUSH:(0,1), STAMINA:(0,1)}),
    'NecropolisPreset3': ('N', INVOCATION, {DARK:(0,2), SORCERY:(0,2), RUSH:(0,1), INVOCATION:(2,1), OFFENCE:(2,0), STAMINA:(0,1)}),
    'RuneMagePreset1': ('F', MACHINES, {LIGHT:(0,2),  RUNELORE:(0,1), LEADERSHIP:(1,0), DEFENCE:(1,2), FAITH:(2,3), RUSH:(0,1)}),
    'RuneMagePreset2': ('F', GATING, {LIGHT:(0,2), SORCERY:(0,2), DARK:(1,0), DEFENCE:(1,2), RUNELORE:(0,1), STAMINA:(0,1)}),
    'RuneMagePreset3': ('F', FAITH, {CHAOS:(0,2), LEARNING:(0,2), SORCERY:(0,2), RUNELORE:(0,1), DEFENCE:(1,2),  STAMINA:(0,1)}),
    'StrongHoldPreset1': ('B', LEADERSHIP, {VOICE: (0,2), LEARNING:(0,2), RAGE:(1,0), LEADERSHIP:(1,0), DEFENCE:(1,2), FAITH:(2,3)}),
    'StrongHoldPreset2': ('B', RAGE, {DARK:(0,2), COMBAT:(1,0), LEADERSHIP:(1,0), OFFENCE:(1,2), RAGE:(0,1), STAMINA:(0,1)}),
    'StrongHoldPreset3': ('B', SUMMON, {SUMMON:(1,0), SORCERY:(0,2), RUSH:(0,1), OFFENCE:(1,2), FAITH:(1,2), STAMINA:(0,1)}),
    'SylvanPreset1': ('S', LEARNING, {OFFENCE:(0,2), LEARNING:(0,2), AVENGER:(2,1), LEADERSHIP:(1,0), DEFENCE:(1,2), RUSH:(0,1)}),
    'SylvanPreset2': ('S', GATING, {DARK:(0,2), LEARNING:(0,2), AVENGER:(2,1), LEADERSHIP:(1,0), COMBAT:(1,2), STAMINA:(0,1)}),
    'SylvanPreset3': ('S', SORCERY, {SUMMON:(1,0), LEARNING:(0,2), SORCERY:(0,2), FAITH:(0,1), DEFENCE:(1,2), OFFENCE:(1,0)}),
    # DEFENCE
}

SPELLS = {
    LIGHT:['MAGIC_ARROW','BLESS','STONESKIN','BLOODLUST','HASTE','DEFLECT_ARROWS','DISPEL','REGENERATION','HOLY_WORD','DIVINE_VENGEANCE','RESURRECT','CELESTIAL_SHIELD','BLIND'],
    DARK: ['PLAGUE','CURSE','WEAKNESS','SLOW','DISRUPTING_RAY','ANIMATE_DEAD','SORRO','TELEPORT','PHANTOM','UNHOLY_WORD','BERSERK','VAMPIRISM'],
    SUMMON : ['WASP_SWARM','LAND_MINE','ARCANE_CRYSTAL','EARTHQUAKE','MAGIC_FIST','ANTI_MAGIC','BLADE_BARRIER','SUMMON_HIVE','FIREWALL','HYPNOTIZE','CONJURE_PHOENIX'],
    CHAOS: ['STONE_SPIKES','ICE_BOLT','METEOR_SHOWER','LIGHTNING_BOLT','FIREBALL','FROST_RING','ARMAGEDDON','IMPLOSION','DEEP_FREEZE','CHAIN_LIGHTNING'],
    RUNELORE: ['RUNE_OF_REVIVE', 'RUNE_OF_MAGIC_CONTROL', 'RUNE_OF_EXORCISM', 'RUNE_OF_STUNNING', 'RUNE_OF_DRAGONFORM'],
    VOICE: ['WARCRY_RALLING_CRY','WARCRY_CALL_OF_BLOOD','WARCRY_WORD_OF_THE_CHIEF','WARCRY_FEAR_MY_ROAR','WARCRY_BATTLECRY','WARCRY_SHOUT_OF_MANY'],
}

def camel_case(name):
    return ''.join(word.capitalize() for word in name.split('_'))

def name(skill):
    return 'HERO_SKILL_'+skill

def dependency(skill, hero):
    deps  = XDB.new('dependenciesIDs',[XDB.new('Item', 'HERO_SKILL_'+skill)])
    return XDB.new('Item', [XDB.new('Class', 'HERO_CLASS_'+hero), deps])

def is128x128(href):
    any_of, none_of = ['H5A2/', 'H5A1/', 'Added/'], [
        'Bodybuilding', 'AgonizingStrike', 'Basic_Voice',
        'Advanced_Voice', 'Expert_Voice', 'Our_Blood', 
        'MightOverMagic', 'GatingMastery', 'Shatter', 'Detain',
        'Runic_Machines', 'CursedGround', 'Path_of_War',
        'Rage_of_the_Forest',
    ]
    return any(x in href for x in any_of) and not any(x in href for x in none_of)


def skills():
    root = XDB.load('GameMechanics/RefTables/Skills.2.xdb')
    data = {s['ID'].txt: s for s in root['objects']}


    for skillname, skill in data.items():
        skill['obj']['SkillPrerequisites'] = []
        skill['obj']['SkillType'].txt = 'SKILLTYPE_DISABLED' 
        if skillname == 'HERO_SKILL_SEAL_OF_PROTECTION':
             skill['obj']['SkillType'].txt = 'SKILLTYPE_STANDART_PERK'

    for skill, perks in SKILLS.items():
        data[name(skill)]['obj']['SkillType'].txt = 'SKILLTYPE_SKILL'
        for perk1, perk2 in zip(perks[::2], perks[1::2]):
            deps2 = [dependency(perk1, hero) for hero in HEROES]
            perk1, perk2 = data[name(perk1)], data[name(perk2)]
            perk1['obj']['SkillType'].txt = 'SKILLTYPE_STANDART_PERK'
            perk2['obj']['SkillType'].txt = 'SKILLTYPE_SPECIAL_PERK'
            perk1['obj']['BasicSkillID'].txt = name(skill)
            perk2['obj']['BasicSkillID'].txt = name(skill)
            perk1['obj']['SkillPrerequisites'] = []
            perk2['obj']['SkillPrerequisites'] = deps2
    
    
    root.save('GameMechanics/RefTables/Skills.xdb')

def duels():
    for hero, (tag, ult, skills) in DUELS.items():
        path = f'Maps/DuelMode/Heroes/{hero}.xdb'
        root = XDB.load(path)

        skillnames = [ULTIMATES[ult]] + list(skills)
        perknames = [(SKILLS[s][2*p[0]], SKILLS[s][2*p[0]+1], SKILLS[s][2*p[1]]) for s, p in skills.items()]
        root['Editable']['skills'] = [XDB.new('Item', {'Mastery':'MASTERY_EXPERT', 'SkillID': name(s)}) for s in skillnames]
        root['Editable']['perkIDs'] = [XDB.new('Item', name(p)) for ps in perknames for p in ps]
        root['Editable']['spellIDs'] = [XDB.new('Item', 'SPELL_'+s) for sk in skills if sk in SPELLS for s in SPELLS[sk]]
        if ult == LEARNING:
            root['Editable']['spellIDs'] = [XDB.new('Item', 'SPELL_'+s) for ss in SPELLS.values() for s in ss]

        stats = next(h[2] for h in HEROES.values() if tag+hero[-1:] == h[0]+str(h[1]))
        root['Editable']['Offence'].int    = int(0.5 * stats[0])
        root['Editable']['Defence'].int    = int(0.5 * stats[1])
        root['Editable']['Spellpower'].int = int(0.5 * stats[2])
        root['Editable']['Knowledge'].int  = int(0.5 * (100 - stats[0] - stats[1] - stats[2]))


        root['PrimarySkillMastery'].txt = 'MASTERY_EXPERT'

        root.save(path)



def lua():
    file = open('scripts/H55-Skills.lua', 'w')

    file.write(f'SKILL_STAMINA = SKILL_{STAMINA}\n')
    file.write(f'SKILL_RUSH = SKILL_{RUSH}\n')
    file.write(f'SKILL_FAITH = SKILL_{FAITH}\n\n')

    file.write('H55_Skills = {\n')
    for s in SKILLS:
        file.write(f'  SKILL_{s},\n')
    file.write('}\n\n')
    
    file.write('H55_Skillnames = {\n')
    for s in SKILLS:
        n = s.split('_')[0].capitalize()
        file.write(f'  [SKILL_{s}] = "{n}",\n')
    file.write('}\n\n')
    
    file.write('H55_Perks = {\n')
    for s, ps in SKILLS.items():
        file.write(f'  [SKILL_{s}] = {{ {", ".join("SKILL_"+p for p in ps)} }},\n')
    file.write('}\n\n')

    file.write('H55_Ultimates = {\n')
    for s, u in ULTIMATES.items():
        file.write(f'  [SKILL_{s}] = {{ ["skill"] = SKILL_{u}, ["player"] = {{}}, ["hero"] = {{}} }},\n')
    file.write('}\n\n')
    



def classes():
    root = XDB.load('GameMechanics/RefTables/HeroClass.2.xdb')
    
    for data in root['objects']:
        hero = data['ID'].txt[11:]
        if hero == 'NONE': continue
        hero = HEROES[hero]
        data['obj']['SkillsProbs'] = [XDB.new('Item', {'SkillID': name(s), 'Prob': '5'}) for s in hero[4]]
        data['obj']['AttributeProbs'] = {
            'OffenceProb': hero[2][0],
            'DefenceProb': hero[2][1],
            'SpellpowerProb': hero[2][2],
            'KnowledgeProb': 100 - hero[2][0] - hero[2][1] - hero[2][2],
        }

    root.save('GameMechanics/RefTables/HeroClass.xdb')


    for dirname, _, names in walk('MapObjects/'):
        for filename in names:
            path = dirname + '/' + filename
            try:
                data = XDB.load(path)
                clss = data['Class'].txt[11:]
                data['PrimarySkill']['Mastery'].txt = 'MASTERY_BASIC'
                data['PrimarySkill']['SkillID'].txt = name(HEROES[clss][3])

                data.save(path)
            except Exception as e:
                print('ERROR:', filename, e)


def swname(name):
    name = camel_case(name).replace('Magic', '').replace('ExpertTrainer', 'ShatterSummoning').replace('WarcryLearning','ShatterDestructive')
    alias =  {
        'Offence': 'Offense',
        'Defence': 'Defense',
        'Training': 'Combat',
        'Learning': 'Enlightenment',
        'DemonicRage': 'Bloodrage',
        'Voice': 'Shout',
        'Invocation': 'Occultism',
        'Artificier': 'Artificer',
        'Voice': 'Shouting',
    }
    return name if name not in alias else alias[name]

SW = 'UI/Doc/SkillWheel'
def skillwheel():
    root = XDB.load('./GameMechanics/RefTables/Skills.2.xdb')
    root = {s['ID'].txt: s for s in root['objects']}

    # BUTTON TEMPLATES
    pb = XDB.load(f'{SW}/Skills/_Template/PerkButtonX.(WindowMSButtonShared).xdb')
    pd = XDB.load(f'{SW}/Skills/_Template/PerkDescX.(WindowTextViewShared).xdb')
    pp = XDB.load(f'{SW}/Skills/_Template/PerkPageX.(WindowSimple).xdb')
    pg = XDB.load(f'{SW}/Skills/_Template/PerkPageX.(WindowSimpleShared).xdb')
    so = XDB.load(f'{SW}/Skills/_Template/SwitchOnX.(UISSendUIMessage).xdb')
    for skill in (swname(s) for s in SKILLS):
        for i in range(10):
            for tag in ('Normal', 'MouseOver', 'Pushed', 'Disabled', 'RightButtonDown'):
                pb['VisualStates'][0][tag]['Background'].atr['href'] = f'{i}.(BackgroundSimpleScallingTexture).xdb#xpointer(/BackgroundSimpleScallingTexture)'
            pb['VisualStates'][0]['MouseOver']['OnEnterSubState']['Commands'][0].atr['href'] = f'SwitchOn{i}.(UISSendUIMessage).xdb#xpointer(/UISSendUIMessage)'
            pd['Children'][0].atr['href'] = f'PerkName{i}.(WindowTextView).xdb#xpointer(/WindowTextView)'
            pp['Shared'].atr['href'] = f'PerkPage{i}.(WindowSimpleShared).xdb#xpointer(/WindowSimpleShared)'
            pp['Name'].txt = f'{swname(skill)}_Perk{i}'
            pg['Children'][0].atr['href'] = f'PerkDesc{i}.(WindowTextView).xdb#xpointer(/WindowTextView)'
            so['szParam'][0].txt = f'{swname(skill)}_Perk{i}'
            pb.save(f'{SW}/Skills/{skill}/PerkButton{i}.(WindowMSButtonShared).xdb')
            pd.save(f'{SW}/Skills/{skill}/PerkDesc{i}.(WindowTextViewShared).xdb')
            pp.save(f'{SW}/Skills/{skill}/PerkPage{i}.(WindowSimple).xdb')
            pg.save(f'{SW}/Skills/{skill}/PerkPage{i}.(WindowSimpleShared).xdb')
            so.save(f'{SW}/Skills/{skill}/SwitchOn{i}.(UISSendUIMessage).xdb')

        

    # BUTTONS POSITIONS
    pb = XDB.load(f'{SW}/Skills/_Template/PerkButtonX.(WindowMSButton).xdb')
    for i in range(12):
        for j, (angle, dist) in enumerate(((20,190), (10,350), (20,350), (30,350), (10,300), (20,300), (30,300), (10,250), (20,250), (30,250))):
            dist, angle = dist - 10, radians(angle - 5 + 360/12 * i)
            for skill in (swname(s) for s in SKILLS):
                pb['Shared'].atr['href'] = f'/{SW}/Skills/{skill}/PerkButton{j}.(WindowMSButtonShared).xdb#xpointer(/WindowMSButtonShared)'
                pb['Placement']['Position']['First']['x'].int = int(612 + sin(angle) * dist)
                pb['Placement']['Position']['First']['y'].int = int(366 + cos(angle) * dist)
                pb.save(f'{SW}/Skills/{skill}/P{i+1}/PerkButton{j}.(WindowMSButton).xdb')
    
    # CLASSES
    for id, ix, probs, skill, _ in HEROES.values():
        path = f'{SW}/Classes/{id}{ix}/Icon.(BackgroundSimpleScallingTexture).xdb'
        data = XDB.load(path)

        data['Texture'].atr['href'] = root[name(skill)]['obj']['Texture'][3].atr['href']
        
        data.save(path)

        for i, namE in enumerate(('Attack', 'Defense', 'Spellpower', 'Knowledge')):
            prob = probs[i] if i < 3 else 100 - probs[0] - probs[1] - probs[2]
            open(f'{SW}/Classes/{id}{ix}/PrimarySkills/Prob_{namE}.txt', 'w', encoding='utf-16').write(f'{prob}<br><font size=15>%')

    
    # CLASSES SKILL AVAILABILITY
    for id, ix, _, _, skills in HEROES.values():
        path = f'{SW}/Wheels/{id}{ix}.(WindowSimpleShared).xdb'

        tree = [f'{swname(s)}/P{i+1}/PerkButton{j}' for i, s in enumerate(skills) for j in range(ULTIMATES[s] == 'NONE', 10)]
        tree = [f'/{SW}/Skills/{t}.(WindowMSButton).xdb#xpointer(/WindowMSButton)' for t in tree]
        tree = [XDB.new('Item', [], {'href' : t}) for t in tree]

        data = XDB.load(path)
        data['Children'] = list(data['Children'])[:4] + tree
        data.save(path)

    # SKILL ORDER
    pict = XDB.load(f'{SW}/Skills/_Template/X.(BackgroundSimpleScallingTexture).xdb')
    namE = XDB.load(f'{SW}/Skills/_Template/PerkNameX.(WindowTextView).xdb')
    desc = XDB.load(f'{SW}/Skills/_Template/PerkDescX.(WindowTextView).xdb')
    for skill, perks in SKILLS.items():
        print(skill)
        perks = [root[name(p)]['obj'] for p in perks]
        perks = [(p['Texture'][1], p['NameFileRef'][0], p['DescriptionFileRef'][0]) for p in perks]
        level = root[name(skill)]['obj']
        level = [(level['Texture'][1+i], level['NameFileRef'][i], level['DescriptionFileRef'][i]) for i in range(3)]
        ultim = root[name(ULTIMATES[skill])]['obj']
        ultim = [(ultim['Texture'][1], ultim['NameFileRef'][0], ultim['DescriptionFileRef'][0])] if ULTIMATES[skill] != 'NONE' else []
        
        # SKILLS
        for ix, href in zip((1,2,3,4,7,5,8,6,9,0), (level + perks[:6] + ultim)):
            href = [h.atr['href'] for h in href]
            path = SW + '/Skills/' + swname(skill)

            size = '128' if is128x128(href[0]) else '64'
            for xy in pict['Size']: 
                xy.txt = size
            pict['Texture'].atr['href'] = href[0]
            pict.save(f'{path}/{ix}.(BackgroundSimpleScallingTexture).xdb')

            namE['TextFileRef'].atr['href'] = href[1]
            namE.save(f'{path}/PerkName{ix}.(WindowTextView).xdb')

            desc['Shared'].atr['href'] = f'PerkDesc{ix}.(WindowTextViewShared).xdb#xpointer(/WindowTextViewShared)'
            desc['TextFileRef'].atr['href'] = href[2][:-3] + 'u.txt' if ix == 0 else href[2]
            desc.save(f'{path}/PerkDesc{ix}.(WindowTextView).xdb')



if __name__ == '__main__':
    skills()
    skillwheel()
    classes()
    lua()
    duels()