from skillwheel import *

ultimates = {
    'Haven': ('HEXING_ATTACK', 'FIERCE_RETALIATION', 'BASH'),
    'Inferno': ('HEXING_ATTACK', 'SEARING_AURA', 'WOUND'),
    'Necropolis': ('HEXING_ATTACK', 'WEAKENING_STRIKE', 'BRUTALITY'),
    'Sylvan': ('HEXING_ATTACK', 'ENTANGLING_ROOTS', 'ELEMENTAL'),
    'Dungeon': ('HEXING_ATTACK', 'ACID_BLOOD', 'RIDER_CHARGE'),
    'Academy': ('HEXING_ATTACK', 'DASH', 'WEAKENING_STRIKE'),
    'Fortress': ('HEXING_ATTACK', 'MAGMA_SHIELD', 'BEAR_ROAR'),
}
# PURGE, FLAMEWAVE, AXE_OF_SLAUGHTER, STRIKE_AND_RETURN, NO_ENEMY_RETALIATION
ULTIMATES = {
    # STORM_WIND, MAGIC_CUSHION, UNSUMMON, 
    OFFENCE: 'WEAKEN_DARK',  # 
    DEFENCE: 'MAGIC_CUSHION',  # Prayer - 
    LUCK: 'ABSOLUTE_PROTECTION',  # Absolute Protection - 2 Armors
    STAMINA: 'CORRUPT_DARK', # Dragonform - 2 Dragons
    RUSH: 'CORRUPT_LIGHT',  # Evasion - 2 INI items
    LOGISTICS: 'CORRUPT_DESTRUCTIVE',  # Charge & Governor - 2 Boots

    FAITH: 'CORRUPT_SUMMONING', # Join - 2 Necro
    MACHINES: 'WEAKEN_DESTRUCTIVE',  # Steroids - 2 Dragons
    LEARNING: 'ABSOLUTE_WIZARDY',  # Spells - 2 Books

    COMBAT: 'ABSOLUTE_CHARGE',  # Anti Magic - 2 resists
    LEADERSHIP: 'EMPATHY',  # Empathy - 2 Lions

    SORCERY: 'MYSTICISM',  # Hexing - 2 staffs
    INVOCATION: 'EAGLE_EYE',  # Vampirism
    
    GATING: 'WEAKEN_LIGHT', # Instant
    NECROMANCY: 'WEAKEN_LIGHT', # Horror
    AVENGER: 'WEAKEN_LIGHT', # CUNNING_OF_THE_WOODS
    ARTIFICIER: 'WEAKEN_LIGHT',
    RUNELORE: 'WEAKEN_LIGHT',
    RAGE: 'WEAKEN_LIGHT',

    VOICE: 'EAGLE_EYE',
}