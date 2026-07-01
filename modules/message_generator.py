import os
from google import genai

client = genai.Client(api_key=os.environ["certificate_automation"])


def generate_message(student_name):

    prompt = f"""
You are writing a personalized certificate message for a student named {student_name} who completed the Morning Star Program.

Morning Star is a 20-day summer program held at the Jamatkhana where children come together each morning to:
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
• Encourages them to continue living the values they learned throughout the year.
• Looks forward to seeing them at future Morning Star programs.
• Feels warm, sincere, and inspiring rather than overly formal.
• Is unique and creative. Do not reuse common phrases or clichés.
• Does not use quotation marks.
• Does not use bullet points.
• Does not invent personal details about the student.
• Ends with:

With warm wishes,

The Morning Star Team
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()