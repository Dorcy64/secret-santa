from typing import List, Dict
import random

SANTA_MESSAGE = (
    "Oops! Correction: Ho ho ho {santa},"
    "\nWe made a little boo-boo, but guess what? You're {santee}'s Secret Santa!"
    " Let's make their holiday season sparkle with joy and fun."
    " P.S. {santee} is {age} years young."
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


def generate_santas(participants_list: List[Dict[str, str]]) -> List[Dict[str, str]]:
    if not participants_list:
        raise ValueError("Participants list is empty.")

    max_attempts = 100
    attempt = 0

    while attempt < max_attempts:
        shuffled_participants = participants_list.copy()
        random.shuffle(shuffled_participants)

        full_response = []
        valid_pairs = True
        remaining_receivers = shuffled_participants.copy()

        for giver in shuffled_participants:
            receivers = [p for p in remaining_receivers if p["id"] not in giver["dont_pair"] and p["id"] != giver["id"]]

            if not receivers:
                valid_pairs = False
                break

            receiver = random.choice(receivers)
            remaining_receivers.remove(receiver)
            full_response.append({
                "phone": giver["phone"],
                "message": generate_text(giver["name"], receiver["name"], receiver["age"]),
                "giver": giver["name"],
                "receiver": receiver["name"]
            })

        if valid_pairs:
            # Check if every participant has been assigned a Santa
            participants_names = set(p["name"] for p in participants_list)
            assigned_santas = set(s["giver"] for s in full_response)
            if participants_names != assigned_santas:
                raise ValueError("Not all participants have been assigned a Santa.")

            # Check if 'dont_pair' constraints are respected
            for santa_info in full_response:
                giver = next(p for p in participants_list if p["name"] == santa_info["giver"])
                receiver = next(p for p in participants_list if p["name"] == santa_info["receiver"])
                if receiver["id"] in giver["dont_pair"]:
                    raise ValueError(
                        (
                            f"Participant {giver['name']} was paired with {receiver['name']},"
                            "violating the 'dont_pair' constraint."
                        )
                    )

            return full_response

        attempt += 1

    raise RuntimeError("Unable to find suitable Secret Santa pairings within the maximum attempts.")
