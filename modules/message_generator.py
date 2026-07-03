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


def generate_message(student_name):

    prompt = f"""
You are writing a personalized certificate message for a student named {student_name} who completed the Morning Star Program.

Morning Star is a 20-day summer program held at the Jamatkhana (An Ismaili Jamatkhana is the place of worship and community gathering for members of the Shia Ismaili Muslim community. It is where Ismailis come together for daily prayers, spiritual reflection, religious education, and important ceremonies such as weddings and commemorations. Beyond worship, the Jamatkhana also serves as a center for community service, learning, and strengthening social bonds through volunteerism and charitable initiatives.) where children come together each morning to:
- Strengthen their spiritual connection through prayer, reflection, and meditation.
- Learn important values such as kindness, compassion, gratitude, service, and respect.
- Build meaningful friendships within the Jamat.
- Participate in fun Sunday activities such as water games, tug-of-war, and team-building events.

Write a heartfelt message that:

• Is between 120 and 170 words.
• Addresses the student by their first name naturally.
• Congratulates them on completing Morning Star.
• Celebrates both their spiritual growth and personal growth.
• Mentions the friendships and memories they created.
• Encourages them to continue living the values they learned throughout the 20 days.
• Looks forward to seeing them at future Morning Star programs.
• Feels warm, sincere, and inspiring rather than overly formal.
• Each message should have a noticeably different writing style, sentence structure, and opening. Imagine writing 150 letters where no two feel alike.
• Do not use quotation marks.
• Do not use bullet points.
• Do not invent personal details about the student.
• You don't have to mention 20 days itself just say Morning Star Program

Begin with:

Ya Ali Madad {student_name},

End with:

With warm wishes,

The Morning Star Team
"""

    MAX_RETRIES = 6

    for attempt in range(MAX_RETRIES):

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            print(f"✓ Gemini message generated for {student_name}")

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

    # Fallback message if all retries fail
    return f"""
Dear {student_name},

Congratulations on completing another wonderful Morning Star program! Your dedication, kindness, and enthusiasm throughout this journey are something to be proud of. We hope the time you spent in prayer, reflection, learning, and building friendships has left you with memories and values that will continue to guide you in the years ahead. May you always continue to grow in faith, compassion, curiosity, and service while carrying the spirit of Morning Star wherever you go.

We look forward to seeing you again next year.

With warm wishes,

The Morning Star Team
""".strip()