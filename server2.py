from fastmcp import FastMCP
# We still need BaseModel for the shared number output type
from pydantic import BaseModel, Field

# Initialize the FastMCP object
mcp = FastMCP(name="MySimpleCalculator")

# --- Define Output Schema for ALL Math Tools ---
# We define this once since all math operations return a single float result.
class MathResult(BaseModel):
    """The result of a math operation."""
    result: float = Field(..., description="The calculated result.")


# --- Tool 1: Greeting Tool (Existing and Working) ---
@mcp.tool
def greet(name: str) -> str:
    """Returns a friendly greeting"""
    return f"Hello {name}! Its a pleasure to connect from your first MCP Server."


# --- Tool 2: Addition Tool (Working) ---
@mcp.tool
def add_numbers(a: float, b: float) -> MathResult:
    """Adds two numbers together and returns the sum (a + b)."""
    return MathResult(result=a + b)


# --- Tool 3: Subtraction Tool ---
@mcp.tool
def subtract_numbers(a: float, b: float) -> MathResult:
    """Subtracts the second number (b) from the first number (a)."""
    return MathResult(result=a - b)


# --- Tool 4: Multiplication Tool ---
@mcp.tool
def multiply_numbers(a: float, b: float) -> MathResult:
    """Multiplies two numbers together (a * b)."""
    return MathResult(result=a * b)


# --- Tool 5: Division Tool ---
@mcp.tool
def divide_numbers(a: float, b: float) -> MathResult:
    """Divides the first number (a) by the second number (b)."""
    if b == 0:
        # Prevent division by zero from crashing the server
        return MathResult(result=float('inf')) 
    return MathResult(result=a / b)


# --- Run the server ---
if __name__ == "__main__":
    mcp.run(transport="http", port="8080")