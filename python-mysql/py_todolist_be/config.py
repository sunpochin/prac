from dotenv import load_dotenv
import os

load_dotenv()

# DATABASE_URL = os.getenv("MYSQL_DATABASE_URL")
DATABASE_URL = os.getenv("GCP_MYSQL")
