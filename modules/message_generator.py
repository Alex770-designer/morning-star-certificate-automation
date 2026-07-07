import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY not found. Create a .env file with your API key."
    )

client = genai.Client(api_key=api_key)


def generate_message(student_name, grade):

    prompt = f"""
You are writing a personalized certificate message for a student named {student_name} who completed the Morning Star Program.

Morning Star is a 20-day summer spiritual and community program held at the Jamatkhana, where children gather for prayer, reflection, learning, friendship, and community activities. Students also participate in fun Sunday events such as games and team-building activities.

Your task is to write a unique, heartfelt certificate message.

------------------------------------------------------------
GRADE CONTEXT (IMPORTANT - FOLLOW STRICTLY)

Student Grade Group: {grade}

You MUST adapt tone, vocabulary, and sentence complexity based on this group.
Do not ignore these instructions.

GRADE ADAPTATION RULES:

Early Childhood (Birth-3, PreK, KG):
- Very simple sentences
- Warm, playful, child-like tone
- Focus on joy, kindness, prayer, friends, and learning

Elementary (1st-4th):
- Friendly and encouraging tone
- Emphasize curiosity, growth, friendship, and effort

Middle School (5th-8th):
- More mature tone
- Emphasize leadership, responsibility, faith, and character

High School (9th-12th):
- Thoughtful and reflective tone
- Emphasize maturity, service, and long-term values
------------------------------------------------------------

REQUIREMENTS:
- 120 to 170 words
- Address the student naturally by first name ({student_name})
- Congratulate them on completing Morning Star Program
- Mention spiritual growth and personal growth
- Mention friendships and memories
- Encourage continuation of values learned
- Each message must feel unique in structure and tone
- Do NOT use bullet points
- Do NOT use quotation marks
- Do NOT invent personal details

FORMAT RULES:

- The message MUST start exactly with:
Ya Ali Madad {student_name},

- The message MUST end exactly with:
With warm wishes,
The Morning Star Team

Do not add anything before or after these lines.
"""

    MAX_RETRIES = 6

    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            print(f"✓ Gemini message generated for {student_name} ({grade})")
            return response.text.strip()

        except Exception as e:
            wait_time = 2 ** attempt

            print(
                f"⚠ Gemini failed for {student_name} "
                f"(Attempt {attempt + 1}/{MAX_RETRIES})"
            )
            print(f"   Error: {e}")

            if attempt < MAX_RETRIES - 1:
                print(f"   Retrying in {wait_time} seconds...\n")
                time.sleep(wait_time)
            else:
                print("\nUsing fallback message.\n")

    # Fallback (keeps SAME format as required)
    return f"""
Ya Ali Madad {student_name},

Congratulations on completing the Morning Star Program! Your dedication, kindness, and enthusiasm throughout this journey are something to be proud of. We hope the time you spent in prayer, reflection, learning, and building friendships has given you meaningful memories and values that will continue to guide you as you grow.

We look forward to seeing you again at future Morning Star programs.

With warm wishes,
The Morning Star Team
""".strip()