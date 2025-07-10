def stt(location):
    print(location)

    import os
    import eyed3

    folder = "output/"

    for root, dirs, files in os.walk(location):
        for m_file in files:
            if m_file.endswith('.mp3'):
                print(m_file)

                output_dir = os.path.join(root, folder)
                os.makedirs(output_dir, exist_ok=True)
                filename = os.path.join(output_dir, m_file + '.txt')

                # Local Audio transcription ------------------------------------------
                import whisper
                model = whisper.load_model("base")
                result = model.transcribe(os.path.join(root, m_file), fp16=False, language="en")
                transcription_text = result['text']
                # print(transcription_text)

                with open(filename, "w") as f:
                    f.write(transcription_text)
