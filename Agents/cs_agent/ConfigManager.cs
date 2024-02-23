// Manages loading and accessing configuration settings
class ConfigManager
{
    public string C2Url { get; set; }
    public string AgentId { get; set; }
    public int CheckInterval { get; set; }

    // Load configuration from a file or environment variables
    public static ConfigManager LoadConfig()
    {
        // Placeholder for actual configuration loading logic
        return new ConfigManager()
        {
            C2Url = "http://c2server.com/api/",
            AgentId = "unique_agent_id",
            CheckInterval = 60 // in seconds
        };
    }
}
