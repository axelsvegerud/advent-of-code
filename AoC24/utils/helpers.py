import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_input(day):
    session = os.getenv("AOC_SESSION")
    if not session:
        raise ValueError("Missing AOC_SESSION in .env file")
    
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookies = {"session": session}
    response = requests.get(url, cookies=cookies)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch input: {response.status_code}")
    
    return response.text.strip()

def get_input(day):
    input_path = f"Inputs/day{day:02}.txt"
    if os.path.exists(input_path):
        with open(input_path) as f:
            return f.read()
    else:
        data = fetch_input(day)
        with open(input_path, "w") as f:
            f.write(data)
        return data