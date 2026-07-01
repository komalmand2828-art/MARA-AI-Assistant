from gtts import gTTS

def text_to_speech(text, lang="en"):

    tts = gTTS(
        text=text,
        lang=lang
    )

    file_name = "response.mp3"

    tts.save(file_name)

    return file_name