import pyttsx3 as pp
import PyPDF2 as pdf

book = open('cor.pdf', 'rb')
pdf_reader = pdf.PdfFileReader(book)
pages = pdf_reader.numPages
print(pages)

speaker = pp.init()
page = pdf_reader.getPage(7)
#if u wanna read page no 3, type page no 2

text = page.extractText()
speaker.say(text)

#speaker.say('first things first i m a say all the words inside my head im fired up and tired up the way the things have been oooooo')
speaker.runAndWait()

