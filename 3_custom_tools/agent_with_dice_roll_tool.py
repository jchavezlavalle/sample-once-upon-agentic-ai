from strands import Agent
from strands import tool

@tool
def roll_dice(faces: int = 6) -> int:
    """
    Roll the dice to obtain a random number.
    Number that is a parameter called faces is by default 6 (a dice containing 6 numbers from 1 to 6)
    If not specified, dice will be of 6 faces. 
    In any case, it will return a random integer number from 1 up to faces (default to 6)

    Example: roll_dice() , response: 2
    Another example could be roll_dice(4) in this case the response being for example 1, it cannot be higher than faces argument.
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


print(roll_dice.tool_spec)  # what Strands tells the model about your tool

dice_master = Agent(
    tools=[roll_dice],
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in fantasy role-playing adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about the game mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die."""
)

dice_master("Help me create a new fantasy character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")

