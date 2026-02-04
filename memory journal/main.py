from memory_validator import text_validator
from custom_error import TextTooShortError
from datetime import datetime
import os
import json


LOG_FILE = "logs.json"

def load_memories() -> list:
    """
    Loads all memories from the JSON log file.

    Checks if the log file exists. If it does, loads the content as a list of memories.
    If the file does not exist or contains invalid JSON, returns an empty list.

    Returns:
        list: A list of memory dictionaries, each containing 'text' and 'created_at' keys.
    """
    if not os.path.exists(LOG_FILE):
        return []
    
    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        
        except (json.JSONDecodeError, TypeError):
            return []

def save_memory(memory) -> None:
    """
    Saves a single memory to the JSON log file.

    Loads existing memories, ensures they are stored as a list,
    appends the new memory, and writes the updated list back to the file.

    Args:
        memory (dict): A dictionary containing at least the keys 'text' and 'created_at'.

    Returns:
        None
    """

def add_memory() -> None:
    """
    Receive a memory from the user and save it to the JSON log file.

    Prompts the user to enter a memory text, validates its length, 
    and stores it along with the creation timestamp.

    Returns:
        None

    Raises:
        TextTooShortError: If the entered memory text is too short.
    """
    row_memory = input("--Write your memory--\n ").strip()

    try:
        text_validator(row_memory)
    except TextTooShortError as error:
        print(error)
        return
    
    memory = {
        'text': row_memory,
        'date': datetime.now().strftime("%y-%m-%d %H:%M")
    }

    save_memory(memory)

    print(f"--memory made successfully!--")

def show_memories() -> None:
    """
    Shows a preview of all available memories.
    The user can read the full memory by entering its number. 
    Returns:
        None       
    """
    pass

def generate_report():
    """
    Generates and prints a simple report of all stored memories.

    The report includes:
        - Total number of memories
        - Average length of memories (in characters)
        - Top 5 most frequently used words across all memories

    The report is printed to the console and no data is returned.

    Returns:
        None
    """
    pass

def exit_menu():
    print("-----Goodbye-----")
    SystemExit
    
MENU_ACTIONS = {
    "1": add_memory,
    "2": show_memories,
    "3": generate_report,
    "4": exit_menu
}


def main():
    while True:
        print("""
    1. Add Memory/Emotion
    2. Show All
    3. Generate Simple Report
    4. Exit
                """)
        choice = input("Choose: ").strip()
        action = MENU_ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid input")
            print("-" * 20)
            continue

if __name__ == '__main__':
    main()
