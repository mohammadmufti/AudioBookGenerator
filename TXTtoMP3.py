from gtts import gTTS

def convert_text_to_speech(text_file_path, output_file_path):
    # Load text from file
    with open(text_file_path, 'r', encoding="utf-8") as text_file:
        text = text_file.read()

    # Use gTTS to generate an MP3 file from the text
    tts = gTTS(text, slow=True)
    tts.save(output_file_path)

text_file_path = input('Enter the name of the text file: ')

if text_file_path.endswith('.txt'):
    mp3_file_path = text_file_path[:-4] + '.mp3'
else:
    mp3_file_path = text_file_path + '.mp3'

convert_text_to_speech(text_file_path, mp3_file_path)

print(f'Text from {text_file_path} converted to speech and saved to {mp3_file_path}.')
