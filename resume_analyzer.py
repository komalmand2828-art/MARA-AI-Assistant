from pypdf import PdfReader
from config import generate_response


def analyze_resume(pdf):

    reader = PdfReader(pdf)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:

            text += extracted

    prompt = f"""
    Analyze this resume.

    Give:

    1. ATS Score /100
    2. Skills Found
    3. Missing Skills
    4. Strengths
    5. Weaknesses
    6. Suggestions

    Resume:

    {text}
    """

    return generate_response(prompt)