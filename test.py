from dotenv import load_dotenv

dotenv_path = load_dotenv("/home/ahsan_dev/kerja/project/gs/.env")  # Assuming your .env file is in the same directory

if dotenv_path:  # Check if loading was successful
    print(dotenv_path["USERID"])
else:
    print("Error: Failed to load environment variables from .env")
