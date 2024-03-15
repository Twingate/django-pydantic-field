__all__ = ("PYDANTIC_V2", "PYDANTIC_V1", "PYDANTIC_VERSION")

PYDANTIC_VERSION = "1.10"
PYDANTIC_V2 = PYDANTIC_VERSION.startswith("2.")
PYDANTIC_V1 = PYDANTIC_VERSION.startswith("1.")
