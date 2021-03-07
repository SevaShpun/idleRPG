ABILITY_BACKSTAB = "backstab"
ABILITY_SHIELD_SLAM = "Shield slam"
ABILITY_ASSAULT = "Assault"
ABILITY_SECOND_STRIKE = "Second strike"
ABILITY_BLEED = "Bleed"
ABILITY_JUST_EFFECT = "JUST_EFFECT"
ABILITY_TRIGGER_COMBAT_START = "combat_start"
ABILITY_TRIGGER_COMBAT_ATTACK = "combat_attack"
ABILITY_TRIGGER_COMBAT_RECEIVE_DMG = "receive_damage"
ABILITY_TRIGGERS = [ABILITY_TRIGGER_COMBAT_START, ABILITY_TRIGGER_COMBAT_ATTACK, ABILITY_TRIGGER_COMBAT_RECEIVE_DMG]
ABILITIES = [ABILITY_BACKSTAB, ABILITY_SHIELD_SLAM, ABILITY_ASSAULT, ABILITY_SECOND_STRIKE, ABILITY_BLEED,
             ABILITY_JUST_EFFECT]

ACTION_NONE = 0
ACTION_RETREAT = 1
ACTION_QUEST = 2
ACTION_DEAD = 3
ACTION_SHOP = 4

EXP_FOR_RETREAT_RATIO = 0.1

RESURRECT_TIMER = 10

MONSTER_CHANCE_ON_QUEST = 0.25
MONSTER_CHANCE_ON_RETREAT = 0.25
MONSTER_AMPLIFY_CHANCE = 0.3
MONSTER_AMPLIFY_MIN_LEVEL = 3

HEALTH_POTION_PRICE = 10
MANA_POTION_PRICE = 12

ACTIONS = [ACTION_NONE, ACTION_RETREAT, ACTION_QUEST, ACTION_DEAD, ACTION_SHOP]
ACTION_NAMES = ["unknown", "retreating", "questing", "dead", "do shopping"]

CMD_SET_CLASS_DESCRIPTION = "set_class_description"
CMD_SET_CLASS_LIST = "set_class_list"
CMD_GET_CLASS_LIST = "get_class_list"
CMD_GET_SERVER_STATS = "get_server_stats"
CMD_SERVER_STATS = "server_stats"
CMD_SERVER_OK = "server_ok"
CMD_SERVER_STARTUP = "server_startup"
CMD_SERVER_SHUTDOWN_IMMEDIATE = "shutdown_immediate"
CMD_SERVER_SHUTDOWN_NORMAL = "shutdown_normal"
CMD_CREATE_CHARACTER = "create_character"
CMD_DELETE_CHARACTER = "delete_character"
CMD_GET_CHARACTER_STATUS = "get_character_status"
CMD_FEEDBACK = "feedback"
CMD_FEEDBACK_REPLY = "reply_feedback"
CMD_FEEDBACK_RECEIVE = "feedback_receive"
CMD_GET_FEEDBACK = "get_feedback"
CMD_SENT_FEEDBACK = "sent_feedback"
CMD_CONFIRM_FEEDBACK = "confirm_feedback"

CONFIG_PARAM_CHAR_BATCH_SIZE = "CHAR_BATCH_SIZE"
CONFIG_PARAM_TURN_TIME = "TURN_TIME"
CONFIG_PARAM_LOG_LEVEL = "LOG_LEVEL"
CONFIG_PARAM_CONFIG_RELOAD_TIME = "CONFIG_RELOAD_TIME"
CONFIG_PARAM_MAX_TURNS = "DEBUG_MAX_TURNS"
CONFIG_PARAM_HALT_ON_GAME_ERRORS = "DEBUG_HALT_ON_GAME_ERROR"
CONFIG_PARAM_HALT_ON_PERSIST_ERRORS = "DEBUG_HALT_ON_PERSIST_ERROR"
CONFIG_PARAM_HALT_ON_QUEUE_ERRORS = "DEBUG_HALT_ON_QUEUE_ERROR"
CONFIG_PARAM_NEW_PATH = "CONFIG_PATH"
CONFIG_PARAM_SERVER_NAME = "SERVER_NAME"
CONFIG_PARAM_SECRET_CONST = "rokada216"
CONFIG_PARAM_DB_PORT = "DB_PORT"
CONFIG_PARAM_DB_NAME = "DB_NAME"
CONFIG_PARAM_DB_HOST = "DB_HOST"
CONFIG_PARAM_DB_USER = "DB_USER"
CONFIG_PARAM_DB_PASSWORD = "DB_PASSWORD"
CONFIG_PARAM_QUEUE_ENABLED = "QUEUE_ENABLED"
CONFIG_PARAM_QUEUE_HOST = "QUEUE_HOST"
CONFIG_PARAM_QUEUE_PORT = "QUEUE_PORT"
CONFIG_PARAM_QUEUE_BATCH_SIZE = "QUEUE_BATCH_SIZE"
CONFIG_PARAM_CHAR_HISTORY_LEN = "CHAR_HISTORY_LEN"
CONFIG_PARAM_QUEUE_USER = "QUEUE_USER"
CONFIG_PARAM_QUEUE_PASSWORD = "QUEUE_PASSWORD"
CONFIG_PARAM_QUEUE_INTERVAL_ON_SLEEP = "QUEUE_INTERVAL_ON_SLEEP"

QUEUE_NAME_INIT = "InitQueue"
QUEUE_NAME_DICT = "DictionaryQueue"
QUEUE_NAME_CMD = "CommandQueue"
QUEUE_NAME_RESPONSES = "ResponsesQueue"

LOG_CONFIG = "Config"
LOG_CHARACTER = "Character"
LOG_GAME = "Game"
LOG_MAIN_APP = "Core"
LOG_PERSIST = "Storage"
LOG_QUEUE = "Message_queue"

START_CLEAR = 1
START_RESUME = 2

ITEM_SLOT_WEAPON = 1
ITEM_SLOT_ARMOR = 2
