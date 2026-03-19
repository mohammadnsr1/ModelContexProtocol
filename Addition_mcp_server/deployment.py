from mcp.server.fastmcp import FastMCP

mcp = FastMCP("deployment")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers together"""
    return a + b
