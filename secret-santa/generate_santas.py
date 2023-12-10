from typing import List, Dict
import random

SANTA_MESSAGE = (
    "Greetings {santa},"
    "\nYou've been chosen to be {santee}'s Secret Santa this year! Spread the joy and warmth of the holiday season. May your gifting be merry and bright! P.S. {santee} is {age} years young."
)


def generate_text(santa: str, santee: str, age: str) -> str:
    """
    Generates a message for the Secret Santa event.

    Args:
    santa (str): Name of the person who is giving the gift.
    santee (str): Name of the person who is receiving the gift.
    age (str): Age of the santee.

    Returns:
    str: A formatted Secret Santa message.
    """
    return SANTA_MESSAGE.format(santa=santa, santee=santee, age=age)


def generate_santas(participants_list: List[Dict[str, str]]) -> List[List[str]]:
    """
    Generates a list of Secret Santa pairings from a list of participants.

    Args:
    participants_list (List[Dict[str, str]]): A list of participant dictionaries.

    Returns:
    List[List[str]]: A list of lists, each containing the phone number of the santa and the generated message.
    """
    max_attempts = 100
    attempt = 0

    while attempt < max_attempts:
        shuffled_participants = participants_list.copy()
        random.shuffle(shuffled_participants)

        full_response = []
        valid_pairs = True

        for giver in shuffled_participants:
            receivers = [
                p for p in shuffled_participants if p["id"] not in giver["dont_pair"] and p["id"] != giver["id"]
            ]

            if not receivers:
                valid_pairs = False
                break

            receiver = random.choice(receivers)
            full_response.append({
                "phone": giver["phone"],
                "message": generate_text(giver["name"], receiver["name"], receiver["age"]),
                "giver": giver["name"],
                "receiver": receiver["name"]
            })

        if valid_pairs:
            # Testing if each participant has a Santa assigned
            assigned_santas = [s["giver"] for s in full_response]
            for participant in shuffled_participants:
                if participant["name"] not in assigned_santas:
                    raise ValueError(f"Participant {participant['name']} does not have a Santa assigned.")

            # Testing if 'dont_pair' constraint is respected
            for santa_info in full_response:
                giver_name = santa_info["giver"]
                giver = next(p for p in shuffled_participants if p["name"] == giver_name)
                receiver = next(p for p in shuffled_participants if p["name"] == santa_info["receiver"])

                if receiver["id"] in giver["dont_pair"]:
                    raise ValueError(f"Participant {giver['name']} was paired with {receiver['name']} "
                                     f"but they should not be paired.")

            return full_response

        attempt += 1

    raise RuntimeError("Unable to find suitable Secret Santa pairings within the maximum attempts.")
