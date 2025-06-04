import os
from dotenv import load_dotenv
print(f"""          *** TEST SCRIPT ***
      ENV "TESTING12" = {os.getenv("TESTING12", "not set")}

""")
