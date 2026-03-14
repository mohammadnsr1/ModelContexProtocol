from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

@mcp.tool()
def get_weather_forecast(city: str) -> str:
    return f"The weather forecast in {city} is sunny."

@mcp.tool()
def get_weather_history(city: str) -> str:
    return f"The weather history in {city} is sunny."

if __name__ == "__main__":
    mcp.run()


