import os
import time
import random


def generate_message(student_name, grade):

    adjectives = [
        "wonderful",
        "positive",
        "amazing",
        "kind",
        "joyful",
        "enthusiastic",
        "meaningful",
        "inspiring",
        "energetic",
        "thoughtful"
    ]

    nouns = [
        "energy",
        "spirit",
        "attitude",
        "enthusiasm",
        "participation",
        "kindness",
        "presence",
        "effort"
    ]

    middle_phrases = [
        "Your participation helped create a welcoming and memorable environment for everyone at Morning Star.",
        "You helped make each Morning Star gathering more enjoyable through your kindness and involvement.",
        "Your presence contributed to the friendships, memories, and positive experiences created throughout the program.",
        "You played an important part in making Morning Star a place filled with learning, connection, and happiness.",
        "Your involvement helped bring the Morning Star community together and made the experience special for everyone."
    ]

    closings = [
        "We are grateful for the memories you helped create and the positive spirit you brought to the program.",
        "We appreciate the kindness and enthusiasm you shared throughout Morning Star.",
        "We hope you continue carrying the values of faith, kindness, and service wherever you go.",
        "Your journey through Morning Star is something to be proud of, and we look forward to seeing you again.",
        "Thank you for being part of the Morning Star family and contributing to such a meaningful experience."
    ]


    # Adjust tone based on grade
    if grade in ["Birth-3", "PreK", "KG"]:
        opening = (
            f"We are so proud of you for being part of Morning Star! "
            f"You showed your happiness, kindness, and love for learning through every moment."
        )

    elif grade in ["1st", "2nd", "3rd", "4th"]:
        opening = (
            f"Congratulations on completing the Morning Star Program! "
            f"Your curiosity, kindness, and excitement helped make each day special."
        )

    elif grade in ["5th", "6th", "7th", "8th"]:
        opening = (
            f"Congratulations on completing the Morning Star Program! "
            f"Your dedication, positive attitude, and growing sense of responsibility reflected the true spirit of the program."
        )

    else:
        opening = (
            f"Congratulations on completing the Morning Star Program! "
            f"Your maturity, commitment, and willingness to grow spiritually and personally represent the values Morning Star encourages."
        )


    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    middle = random.choice(middle_phrases)
    closing = random.choice(closings)


    return f"""
Ya Ali Madad {student_name},

{opening}

Thank you for bringing such a {adj} {noun} to Morning Star. {middle}

{closing}

We look forward to seeing you again at future Morning Star programs.

With warm wishes,
The Morning Star Team
""".strip()