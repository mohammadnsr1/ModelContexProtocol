# ModelContextProtocol

This repository contains custom MCP servers and clients.

### Installation


To use this server from an MCP-compatible client, add an entry like this to your MCP servers configuration JSON:

```json
{
  "mcpServers": {
    "addition": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/mohammadnsr1/ModelContexProtocol.git",
        "mcp-server"
      ],
    }
  }
}
```

