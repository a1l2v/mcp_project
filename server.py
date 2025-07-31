from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(
    name="Knowledge Base"
)


@mcp.tool()
def get_weather(city):
    # TODO implement the weather api call @a1l2v
    """get the weather of a particular city"""
    return f"The weather in {city} is windy."

def document_search(query):
    # TODO implement the document check using rag @a1l2v
    """get the ans from the document"""
    return f"It is the answer of the {query} from the document"
@mcp.tool()
def web_search(query):
    # TODO implement the web api call using some web Api @pranave-2
    """get the ans from the web"""
    return f"It is the answer of the {query} from the web"


# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")



