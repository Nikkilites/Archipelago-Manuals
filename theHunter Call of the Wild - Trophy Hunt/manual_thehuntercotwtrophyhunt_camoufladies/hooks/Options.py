# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, Visibility, OptionSet

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50

class HuntType(Choice):
    """Pick if you wanna go on a Gold or Diamond Trophy Hunt."""
    display_name = "Hunt Type"
    option_gold = 0
    option_diamond = 1
    default = 1

class BirdMode(Choice):
    """Pick if birds will be part of your hunt. Please adjust Trophies to win to a maximum of 83 if birds are excluded""" #If Require Caller is picked, make sure that none of the DLC's that include callers are disabled."""
    display_name = "Bird Mode"
    option_excluded = 0
    option_included = 1
    #option_require_caller = 2
    #option_only_birds = 3
    default = 1

class TrophiesToWin(Range):
    """Pick how many Trophies are required to goal."""
    display_name = "Trophies to win"
    range_start = 1
    range_end = 112
    default = 3

class DLCOptionSet(OptionSet):
    """Pick which DLCs to include. Default includes every DLC."""
    display_name = "Enabled DLC"
    default = {
        "DLC - Ambusher Pack",
        "DLC - Assorted Sidearms Pack",
        "DLC - Bloodhound",
        "DLC - Bolt Action Rifle Pack",
        "DLC - Cuatro Colinas",
        "DLC - Duck and Cover Pack",
        "DLC - Emerald Coast",
        "DLC - German Shorthair",
        "DLC - High Calibur Weapon Pack",
        "DLC - High-Tech Hunting Pack",
        "DLC - Hunter Power Pack",
        "DLC - Labrador Retriever",
        "DLC - Medved-Taiga",
        "DLC - Mississippi Acres",
        "DLC - Modern Rifle Pack",
        "DLC - Rancho del Arroyo",
        "DLC - Rapid Hunt Rifle",
        "DLC - Saber 4x4 ATV",
        "DLC - Salzwiesen",
        "DLC - Silver Ridge",
        "DLC - Smoking Barrels",
        "DLC - Sundarpatan",
        "DLC - Te Awaroa",
        "DLC - Tents & Ground Blinds",
        "DLC - Treestand and Tripod Pack",
        "DLC - Vurhonga Savanna",
        "DLC - Weapon Pack 1",
        "DLC - Weapon Pack 2",
        "DLC - Weapon Pack 3",
        "DLC - Wild Goose Chase Gear",
        "DLC - Yukon Valley",
        "DLC - New England Mountains"
    }
    valid_keys = {
        "DLC - Ambusher Pack",
        "DLC - Assorted Sidearms Pack",
        "DLC - Bloodhound",
        "DLC - Bolt Action Rifle Pack",
        "DLC - Cuatro Colinas",
        "DLC - Duck and Cover Pack",
        "DLC - Emerald Coast",
        "DLC - German Shorthair",
        "DLC - High Calibur Weapon Pack",
        "DLC - High-Tech Hunting Pack",
        "DLC - Hunter Power Pack",
        "DLC - Labrador Retriever",
        "DLC - Medved-Taiga",
        "DLC - Mississippi Acres",
        "DLC - Modern Rifle Pack",
        "DLC - Rancho del Arroyo",
        "DLC - Rapid Hunt Rifle",
        "DLC - Saber 4x4 ATV",
        "DLC - Salzwiesen",
        "DLC - Silver Ridge",
        "DLC - Smoking Barrels",
        "DLC - Sundarpatan",
        "DLC - Te Awaroa",
        "DLC - Tents & Ground Blinds",
        "DLC - Treestand and Tripod Pack",
        "DLC - Vurhonga Savanna",
        "DLC - Weapon Pack 1",
        "DLC - Weapon Pack 2",
        "DLC - Weapon Pack 3",
        "DLC - Wild Goose Chase Gear",
        "DLC - Yukon Valley",
        "DLC - New England Mountains"
    }

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["hunt_type"] = HuntType
    options["trophies_to_win"] = TrophiesToWin
    options["bird_mode"] = BirdMode
    options["dlc_options"] = DLCOptionSet
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    for option in options.keys():
        if 'goal' in option:
            options[option].visibility = Visibility.none
    return options