from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet


def export_pdf(messages):

    pdf = SimpleDocTemplate(
        "chat_export.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    for msg in messages:

        content.append(
            Paragraph(
                f"{msg['role']} : {msg['content']}",
                styles["Normal"]
            )
        )

    pdf.build(content)

    return "chat_export.pdf"