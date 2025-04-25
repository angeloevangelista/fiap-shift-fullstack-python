import time
from fastapi import FastAPI

from routers import auth

# matched = bcrypt.checkpw(
#   b"12345678",
#   b"$2b$089nLQM7kb9gK36iHUGd5jbxOIpnitlcGtx1nSVvwKXaOSlRPu.UQIpi",
# )

app = FastAPI()

@app.get("/api/health")
def health_check():
  return {
    "healthy": True,
    "timestamp": time.asctime(),
  }

app.include_router(auth.router)
