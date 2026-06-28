import random

starters = [
    "Thank you for participating in Morning Star and for bringing such",
    "We truly appreciate your involvement in Morning Star and the",
    "Thank you for being part of Morning Star and sharing your",
    "Your participation in Morning Star reflected such",
    "We are grateful for your presence in Morning Star and your",
    "It was a pleasure having you join us for Morning Star, where your",
    "Throughout Morning Star, your",
    "Every session was made brighter by your",
    "Thank you for helping make Morning Star such a meaningful experience through your",
    "Your enthusiasm throughout Morning Star was shown through your",
    "From the very beginning, your",
    "It was wonderful to see the way your",
    "Morning Star was enriched by your",
    "Your commitment to Morning Star was evident through your",
    "We sincerely appreciate the way your",
    "Every day of Morning Star was enhanced by your",
    "The program was made even more enjoyable because of your",
    "We are thankful for the kindness and",
    "Your genuine involvement and",
    "It was inspiring to witness your"
]

adjectives = [
    "great",
    "positive",
    "amazing",
    "outstanding",
    "incredible",
    "excellent",
    "remarkable",
    "fantastic",
    "strong",
    "energetic",
    "genuine",
    "kind",
    "encouraging",
    "uplifting",
    "enthusiastic",
    "thoughtful",
    "warm",
    "friendly",
    "inspiring",
    "joyful",
    "supportive",
    "compassionate",
    "dedicated",
    "consistent",
    "vibrant"
]

nouns = [
    "energy",
    "enthusiasm",
    "attitude",
    "spirit",
    "presence",
    "participation",
    "kindness",
    "optimism",
    "dedication",
    "commitment",
    "encouragement",
    "support",
    "positivity",
    "friendliness",
    "teamwork",
    "respect",
    "curiosity",
    "determination",
    "passion",
    "confidence"
]

sentence1 = [
    "Your willingness to participate wholeheartedly helped make every activity more enjoyable.",
    "Your positive attitude helped create an environment where everyone felt welcome.",
    "The encouragement you shared inspired those around you to become more involved.",
    "You consistently contributed to a warm and supportive atmosphere.",
    "Your enthusiasm helped make each day memorable.",
    "You brought positivity that brightened every gathering.",
    "Your involvement made activities more engaging for everyone.",
    "You helped strengthen the friendships formed throughout the program.",
    "Your kindness left a lasting impression on fellow participants.",
    "You demonstrated the value of encouraging and supporting others.",
    "Your smile and enthusiasm helped make every session special.",
    "You played an important role in creating a welcoming environment.",
    "Your excitement encouraged others to participate with confidence.",
    "Your genuine interactions made Morning Star even more enjoyable.",
    "You helped build a community where everyone could feel included."
]

sentence2 = [
    "Whether through conversations, teamwork, or simply showing up each day, your presence was appreciated.",
    "Every interaction you had contributed something meaningful to the experience.",
    "The memories created during Morning Star were made richer because of participants like you.",
    "Your willingness to learn and grow inspired those around you.",
    "The friendships you built reflected the welcoming spirit of Morning Star.",
    "Your contributions, both large and small, made a real difference.",
    "The excitement you brought could be felt throughout the program.",
    "You demonstrated kindness and respect in every interaction.",
    "Your dedication helped make the experience rewarding for everyone.",
    "You showed what it means to be an active member of a caring community.",
    "The energy you brought encouraged others to enjoy every moment.",
    "Your participation helped create lasting memories for everyone involved.",
    "You consistently made those around you feel included and valued.",
    "Your support of your fellow participants helped strengthen our community.",
    "You helped create an atmosphere where everyone could thrive."
]

sentence3 = [
    "Programs like Morning Star become successful because of participants like you.",
    "It is people like you who transform a program into an unforgettable experience.",
    "The friendships and memories created throughout Morning Star are a reflection of everyone's efforts.",
    "Every participant contributes something unique, and your contribution was truly appreciated.",
    "Your involvement helped shape the positive experience shared by the entire community.",
    "Your enthusiasm reminded us how meaningful shared experiences can be.",
    "Every smile, conversation, and activity helped strengthen our community.",
    "You made Morning Star a place where learning and friendship went hand in hand.",
    "The positive impact you had extended far beyond individual activities.",
    "You helped create an environment filled with encouragement and respect.",
    "Your contributions helped make Morning Star both meaningful and enjoyable.",
    "The spirit you brought made each gathering more memorable.",
    "Your participation added something truly valuable to this year's program.",
    "You exemplified the values that make Morning Star such a special experience.",
    "Your presence helped create memories that will be cherished for years to come."
]

sentence4 = [
    "We hope the friendships and experiences you gained continue to inspire you.",
    "May the lessons and memories from Morning Star remain with you for years to come.",
    "We hope you continue sharing the same positivity wherever life takes you.",
    "We look forward to seeing the wonderful things you accomplish in the future.",
    "Thank you for making Morning Star a place filled with joy and encouragement.",
    "Your participation will always be remembered with gratitude.",
    "We wish you continued success and happiness in everything you pursue.",
    "Thank you for helping make this year's program one to remember.",
    "We hope Morning Star has left you with wonderful memories and lasting friendships.",
    "May the values experienced during Morning Star continue to guide you.",
    "Thank you for sharing your unique talents with our community.",
    "We appreciate everything you contributed throughout the program.",
    "It has been a privilege to share this journey with you.",
    "Your impact on Morning Star will not be forgotten.",
    "We hope this certificate serves as a reminder of the positive difference you made."
]

closings = [
    "With sincere appreciation, thank you for helping shape such a memorable Morning Star experience.",
    "Thank you once again for being an important part of our Morning Star family.",
    "We are grateful for everything you contributed throughout the program.",
    "It was truly a joy having you with us this year.",
    "We appreciate the positivity and dedication you shared every day.",
    "Thank you for making Morning Star brighter through your participation.",
    "We wish you all the best and hope to see you again in the future.",
    "Your presence made Morning Star an even more meaningful experience.",
    "We hope you continue inspiring those around you with the same kindness and enthusiasm.",
    "Thank you for helping create a welcoming community for everyone involved.",
    "Your contributions will always be remembered with gratitude.",
    "We are proud to have shared this experience with you.",
    "Thank you for helping create lifelong memories.",
    "We hope this is only the beginning of many wonderful experiences ahead.",
    "Thank you for being such a valued member of the Morning Star community."
]

endings = [
    "With gratitude,\nThe Morning Star Team"
]

def generate_message(student_name):
    return f"""Ya Ali Madad {student_name}!

{random.choice(starters)} {random.choice(adjectives)} {random.choice(nouns)} to the program.

{random.choice(sentence1)}

{random.choice(sentence2)}

{random.choice(sentence3)}

{random.choice(sentence4)}

{random.choice(closings)}

{endings[0]}
"""