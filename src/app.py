"""Basic app."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def get_test():
    """Get single test."""
    return {"name": "test"}


# def main() -> None:
#     """Start app."""
#     print("")


# if __name__ == "__main__":
#     main()
