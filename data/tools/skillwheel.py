from collections import defaultdict
from os import utime
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
STAMINA = 'SHATTER_SUMMONING_MAGIC'
RUSH = 'SHATTER_DESTRUCTIVE_MAGIC'
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
    OFFENCE: ( 'FAST_AND_FURIOUS',  'FRENZY', 'TACTICS', 'EXPERT_TRAINER', 'OFFENSIVE_FORMATION', 'ARCHERY' ), # 
    DEFENCE: ( 'DEFENSIVE_FORMATION', 'HOLD_GROUND', 'TOUGHNESS', 'EVASION', 'PROTECTION', 'SPELLPROOF_BONES' ), # Prayer - 
    LUCK: ( 'DEAD_LUCK', 'LUCKY_STRIKE', 'ELVEN_LUCK', 'ABSOLUTE_LUCK', 'CHAOTIC_SPELLS', 'LUCKY_SPELLS' ), # Absolute Protection - 2 Armors
    STAMINA: ( 'LAST_STAND', 'REMOTE_CONTROL', 'RESISTANCE', 'DWARVEN_LUCK', 'POWER_OF_STONE', 'BARBARIAN_SOIL_BURN' ), # Dragonform - 2 Dragons
    RUSH: ( 'POWER_OF_HASTE', 'TELEPORT_ASSAULT', 'SNATCH', 'PREPARATION', 'WILDFIRE', 'RUNIC_MACHINES' ), # Evasion - 2 Shields
    LOGISTICS: ( 'SCOUTING', 'DEATH_TREAD', 'PATHFINDING', 'NAVIGATION', 'ESTATES', 'GRAIL_VISION' ), # Charge - 2 Boots

    FAITH: ( 'DETAIN_SUMMONING', 'BARBARIAN_FOG_VEIL', 'DETAIN_DESTRUCTIVE', 'BARBARIAN_ANCIENT_SMITHY', 'DETAIN_LIGHT', 'BARBARIAN_STORM_WIND', 'DETAIN_DARK', 'CHILLING_STEEL' ), # Vampirism - 2 Necro
    MACHINES: ( 'BALLISTA', 'TRIPLE_BALLISTA', 'FIRST_AID', 'LAST_AID', 'CATAPULT', 'TRIPLE_CATAPULT' ), # Steroids - 2 Dragons
    LEARNING: ( 'DISGUISE_AND_RECKON', 'QUICKNESS_OF_MIND', 'SCHOLAR', 'MENTORING', 'INTELLIGENCE', 'COUNTERSPELL' ), # Spells - 2 Books

    COMBAT: ( 'HOLY_CHARGE', 'STUNNING_BLOW', 'POWERFULL_BLOW', 'CRITICAL_STRIKE', 'DEMONIC_STRIKE', 'BARBARIAN_WEAKENING_STRIKE' ), # Anti Magic - 2 resists
    LEADERSHIP: ( 'DIPLOMACY', 'RETRIBUTION', 'RECRUITMENT', 'PRAYER', 'ENCOURAGE', 'ROAD_HOME' ), # Joining - 2 Lions

    SORCERY: ( 'MAGIC_BOND', 'ELITE_CASTERS', 'ARCANE_TRAINING', 'PAYBACK', 'WISDOM', 'EAGLE_EYE' ), # Distract? - 2 staffs
    INVOCATION: ( 'EMPOWERED_SPELLS', 'DISTRACT', 'CONSUME_CORPSE', 'EXPLODING_CORPSES', 'DARK_RITUAL', 'PARIAH' ), # Rage - Magma, Roots, Fierce, Charge, Wound, Bash, Searing
 
    #'SHATTER_LIGHT_MAGIC': ( 'DEFENSIVE_FORMATION', 'EVASION', 'PROTECTION', 'SPELLPROOF_BONES', 'TOUGHNESS', 'HOLDGROUND' ), # EMPATHY - X Morale
    SUMMON: ( 'FIRE_AFFINITY', 'SUN_FIRE', 'ELEMENTAL_BALANCE', 'SHAKE_GROUND', 'MASTER_OF_QUAKES', 'FOG_VEIL' ), # 2x Crystals - X Crystals
    CHAOS: ( 'DEADLY_COLD', 'MASTER_OF_ICE', 'SET_AFIRE',  'MASTER_OF_FIRE', 'ANCIENT_SMITHY', 'MASTER_OF_LIGHTNINGS' ), # -HP - X Spellpower
    DARK: ( 'MASTER_OF_SICKNESS', 'SPIRIT_LINK', 'WEAKENING_STRIKE', 'MASTER_OF_MIND', 'MASTER_OF_CURSES',  'SOIL_BURN' ), # -INI 
    LIGHT: ( 'MASTER_OF_ABJURATION', 'ETERNAL_LIGHT', 'TWILIGHT',  'MASTER_OF_WRATH', 'MASTER_OF_BLESSING', 'GUARDIAN_ANGEL'), 

    GATING: ( 'SPOILS_OF_WAR', 'PATH_OF_WAR', 'GATING_MASTERY', 'CRITICAL_GATING', 'DEMONIC_FIRE', 'QUICK_GATING' ), # Instant
    NECROMANCY: ( 'DEATH_SCREAM', 'SHRUG_DARKNESS', 'NO_REST_FOR_THE_WICKED', 'LORD_OF_UNDEAD', 'CHILLING_BONES', 'HAUNT_MINE' ), # Horror
    AVENGER: ( 'FOREST_RAGE', 'FOREST_GUARD_EMBLEM', 'IMBUE_ARROW', 'IMBUE_BALLISTA', 'SNIPE_DEAD', 'MULTISHOT' ), # CUNNING_OF_THE_WOODS
    ARTIFICIER: ( 'ACADEMY_AWARD', 'SUPRESS_LIGHT', 'MELT_ARTIFACT', 'MAGIC_MIRROR', 'ARTIFICIAL_GLORY', 'MARCH_OF_THE_MACHINES' ),
    RUNELORE: ( 'FORTUNATE_ADVENTURER', 'RUNIC_ATTUNEMENT', 'FINE_RUNE', 'TAP_RUNES', 'DEMONIC_FLAME', 'STRONG_RUNE'),
    RAGE: ( 'BATTLE_ELATION', 'MIGHT_OVER_MAGIC', 'MEMORY_OF_OUR_BLOOD', 'ABSOLUTE_RAGE', 'GOBLIN_SUPPORT', 'DEFEND_US_ALL' ),

    VOICE: ( 'MIGHTY_VOICE', 'VOICE_OF_RAGE', 'BARBARIAN_MYSTICISM', 'BARBARIAN_DISTRACT', 'VOICE_TRAINING', 'BARBARIAN_ELITE_CASTERS' ),
}

ULTIMATES = {
    # STORM_WIND, MAGIC_CUSHION, UNSUMMON, 
    OFFENCE: 'CORRUPT_DARK',  # DragonForm - 2 Dragons
    DEFENCE: 'ABSOLUTE_PROTECTION',  # Benedicted - Visit Monastery
    LUCK: 'MAGIC_CUSHION',  # Absolute Protection - 2 Armors
    STAMINA: 'STORM_WIND', # High Ground - 2 Boots
    RUSH: 'CORRUPT_LIGHT',  # Dodge - 2 INI items
    LOGISTICS: 'CORRUPT_DESTRUCTIVE',  # Charge & Governor - 2 Boots

    FAITH: 'CORRUPT_SUMMONING', # Join - 2 Saint 
    MACHINES: 'WEAKEN_DESTRUCTIVE',  # Steroids - 2 Dragons
    LEARNING: 'ABSOLUTE_WIZARDY',  # Spells - 2 Books

    COMBAT: 'ABSOLUTE_CHARGE',  # Anti Magic - 2 resists
    LEADERSHIP: 'EMPATHY',  # Empathy - 2 Lions

    SORCERY: 'MYSTICISM',  # Hexing - 2 staffs
    INVOCATION: 'WEAKEN_DARK',  # Vampirism - 2 Necro

    SUMMON: 'NONE',
    CHAOS: 'NONE',
    DARK: 'NONE',
    LIGHT: 'NONE',
    
    GATING: 'WEAKEN_LIGHT', # Instant
    NECROMANCY: 'WEAKEN_LIGHT', # Horror
    AVENGER: 'WEAKEN_LIGHT', # CUNNING_OF_THE_WOODS
    ARTIFICIER: 'WEAKEN_LIGHT',
    RUNELORE: 'WEAKEN_LIGHT',
    RAGE: 'WEAKEN_LIGHT',

    VOICE: 'NONE',
}

SKIP = defaultdict(list, {
    'SCHOLAR': ['BARBARIAN'],
    'POWER_OF_STONE': [ 'BARBARIAN' ],
    'POWER_OF_HASTE': [ 'BARBARIAN' ],
    'TELEPORT_ASSAULT': [ 'BARBARIAN' ],
})


MIGHT = [COMBAT, LEADERSHIP, MACHINES]
MAGE1 = [SORCERY, INVOCATION, MACHINES]
MAGE2 = [SORCERY, INVOCATION]
def BASIC(replace):
    BASIC = [OFFENCE, DEFENCE, LUCK, STAMINA, RUSH, LOGISTICS] + [FAITH, LEARNING]
    return [replace[s] if s in replace else s for s in BASIC]

HEROES = {
    'KNIGHT':       ('H', 1, BASIC({})                 + MIGHT + [DARK]), # RENEGADE
    'RANGER':       ('H', 2, BASIC({})                 + MIGHT + [LIGHT]), # KNIGHT
    'HERETIC':      ('H', 3, BASIC({})                 + MAGE2 + [CHAOS, DARK, SUMMON]), # HERETIC
    'WIZARD':       ('I', 1, BASIC({DEFENCE: DARK})    + MIGHT + [GATING]), # DEMON LORD
    'DEMON_LORD':   ('I', 2, BASIC({OFFENCE: DARK})    + MAGE1 + [GATING, CHAOS]), # GATEKEEPER
    'SORCERER':     ('I', 3, BASIC({STAMINA: DARK})    + MAGE2 + [CHAOS, GATING, SUMMON]), # SORCERER
    'RUNEMAGE':     ('N', 1, BASIC({})                 + [COMBAT, NECROMANCY, DARK, SUMMON]), # DEATH KNIGHT
    'NECROMANCERA': ('N', 2, BASIC({})                 + MAGE2 + [NECROMANCY, DARK, SUMMON]), # NECROMANCER
    'REAVER':       ('N', 3, BASIC({FAITH: DARK})      + MAGE2 + [NECROMANCY, CHAOS, SUMMON]), # NETHERMAGE
    'BEASTMASTER':  ('D', 1, BASIC({})                 + MIGHT + [DARK]), # OVERLORD
    'SEER':         ('D', 2, BASIC({STAMINA: DARK})    + MAGE1 + [NECROMANCY, CHAOS]), # TRICKSTER
    'WARLOCK':      ('D', 3, BASIC({OFFENCE: DARK})    + MAGE2 + [SUMMON, NECROMANCY, CHAOS]), # WARLOCK
    'RANGERA':      ('S', 1, BASIC({FAITH: LIGHT})     + MIGHT + [AVENGER]), # RANGER
    'WARDEN':       ('S', 2, BASIC({STAMINA: DARK})    + MIGHT + [AVENGER, CHAOS]), # AVENGER
    'ENCHANTER':    ('S', 3, BASIC({})                 + MAGE2 + [LIGHT, CHAOS, SUMMON]), # DRUID
    'GUILDMASTER':  ('A', 1, BASIC({FAITH: LIGHT})     + MIGHT + [ARTIFICIER]), # ENCHANTER
    'ELEMENTALIST': ('A', 2, BASIC({OFFENCE: CHAOS})   + MAGE1 + [ARTIFICIER, SUMMON]), # CONJURER
    'WIZARDA':      ('A', 3, BASIC({FAITH: CHAOS})     + MAGE2 + [DARK, ARTIFICIER, SUMMON]), # WIZARD
    'NECROMANCER':  ('F', 1, BASIC({LEARNING: LIGHT})  + MIGHT + [RUNELORE]), # ENGINEER
    'FLAMEKEEPERA': ('F', 2, BASIC({LEARNING: DARK})   + MAGE1 + [RUNELORE, CHAOS]), # FLAMEKEEPER
    'RUNEMAGEA':    ('F', 3, BASIC({LUCK: LIGHT})      + MAGE2 + [CHAOS, RUNELORE, SUMMON]), # RUNEMAGE
    'BARBARIAN':    ('B', 1, BASIC({})                 + MIGHT + [RAGE, VOICE]), # CHIEFTAN
    'SHAMAN':       ('B', 2, BASIC({OFFENCE: LIGHT})   + MAGE1 + [RUNELORE, SUMMON]), # SHAMAN
    'WARLOCKB':     ('B', 3, BASIC({LUCK: DARK})       + MAGE1 + [NECROMANCY, CHAOS]), # WITCH
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
    ]
    return any(x in href for x in any_of) and not any(x in href for x in none_of)
    



def skills():
    root = XDB.load('GameMechanics/RefTables/Skills.xdb.bak')
    data = {s['ID'].txt: s for s in root['objects']}


    for skill in data.values():
        skill['obj']['SkillType'].txt = 'SKILLTYPE_DISABLED'
        skill['obj']['SkillPrerequisites'] = []

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
    
    blood = data[name('POWER_OF_BLOOD')]['obj']
    blood['BasicSkillID'].txt = name('LEARNING')
    blood['SkillType'].txt = 'SKILLTYPE_SPECIAL_PERK'
    blood['SkillPrerequisites'] = [dependency('SCHOLAR', 'BARBARIAN')]
    
    root.save('GameMechanics/RefTables/Skills.xdb')



def classes():
    root = XDB.load('GameMechanics/RefTables/HeroClass.xdb.bak')
    
    for data in root['objects']:
        hero = data['ID'].txt[11:]
        if hero == 'NONE': continue
        tree = [XDB.new('Item', [XDB.new('SkillID', name(s)), XDB.new('Prob', '5')]) for s in HEROES[hero][2]]
        data['obj']['SkillsProbs'] = tree

    root.save('GameMechanics/RefTables/HeroClass.xdb')

def swname(name):
    name = camel_case(name).replace('Magic', '')
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
    root = XDB.load('./GameMechanics/RefTables/Skills.xdb.bak')
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
    
    
    # CLASSES SKILL AVAILABILITY
    for id, ix, skills in HEROES.values():
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
            desc['TextFileRef'].atr['href'] = href[2]
            desc.save(f'{path}/PerkDesc{ix}.(WindowTextView).xdb')




if __name__ == '__main__':
    skills()
    skillwheel()
    classes()