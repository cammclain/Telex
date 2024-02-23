from telegram import InlineKeyboardButton, InlineKeyboardMarkup

### Start Menu Inline Keyboard
start_inline_keyboard = [
    [
        InlineKeyboardButton("About", callback_data="about"),
        InlineKeyboardButton("Help", callback_data="help"),
    ],
    [
        InlineKeyboardButton("Commands", callback_data="commands"),
        InlineKeyboardButton("List Active Agents", callback_data="list_agents"),
    ],
    [
        InlineKeyboardButton("Management", callback_data="management"),
        InlineKeyboardButton("Settings", callback_data="settings"),
    ]
]
start_inline_markup = InlineKeyboardMarkup(start_inline_keyboard)

### Commands Menu Inline Keyboard
commands_inline_keyboard = [
    [
        InlineKeyboardButton("Checkin", callback_data="checkin"),
        InlineKeyboardButton("Execute", callback_data="execute"),
    ],
    [
        InlineKeyboardButton("Exfiltrate", callback_data="exfiltrate"),
        InlineKeyboardButton("Heartbeat", callback_data="heartbeat"),
    ],
    [
        InlineKeyboardButton("Status", callback_data="status"),
        InlineKeyboardButton("Update Agent", callback_data="update"),
    ],
    [
        InlineKeyboardButton("Back to Main Menu", callback_data="main_menu"),
    ]
]
commands_inline_markup = InlineKeyboardMarkup(commands_inline_keyboard)

### Management Commands Inline Keyboard
management_inline_keyboard = [
    [
        InlineKeyboardButton("Add User", callback_data="add_user"),
        InlineKeyboardButton("Remove User", callback_data="remove_user"),
    ],
    [
        InlineKeyboardButton("List Users", callback_data="list_users"),
        InlineKeyboardButton("Agent Management", callback_data="agent_management"),
    ],
    [
        InlineKeyboardButton("Back to Main Menu", callback_data="main_menu"),
    ]
]
management_inline_markup = InlineKeyboardMarkup(management_inline_keyboard)

### Agent Management Inline Keyboard
agent_management_inline_keyboard = [
    [
        InlineKeyboardButton("List Agents", callback_data="list_agents"),
        InlineKeyboardButton("Agent Status", callback_data="agent_status"),
    ],
    [
        InlineKeyboardButton("Activate Agent", callback_data="activate_agent"),
        InlineKeyboardButton("Deactivate Agent", callback_data="deactivate_agent"),
    ],
    [
        InlineKeyboardButton("Back to Management", callback_data="back_management"),
    ]
]
agent_management_inline_markup = InlineKeyboardMarkup(agent_management_inline_keyboard)

### Settings Inline Keyboard
settings_inline_keyboard = [
    [
        InlineKeyboardButton("Configuration", callback_data="config"),
        InlineKeyboardButton("Update Settings", callback_data="update_settings"),
    ],
    [
        InlineKeyboardButton("Back to Main Menu", callback_data="main_menu"),
    ]
]
settings_inline_markup = InlineKeyboardMarkup(settings_inline_keyboard)

