import pyttsx3
import PyPDF2

pdf_path = "/Users/swayampatil/Downloads/book.pdf"

# Open the PDF file
with open(pdf_path, "rb") as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speech rate
    engine.setProperty('voice', 'english')  # Choose the voice

    # Loop through each page of the PDF file and extract the text
    for page in pdf_reader.pages:
        text = page.extract_text()

        # Convert the text to speech and play it
        engine.say(text)
        engine.runAndWait()

        # Save the speech as an MP4 file
        engine.save_to_file(text, 'book.mp4')
