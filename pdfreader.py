import pyttsx3 
import PyPDF2
book  = open("5 Force And Laws Of Motion.pdf","rb")
pdfreader = PyPDF2.PdfFileReader(book)
NumberOfPages = pdfreader.numPages
speaker = pyttsx3.init()
for i in range(0,NumberOfPages):
    eachPage = pdfreader.getPage(i)
    text = eachPage.extractText()
    speaker.say(text)
    speaker.runAndWait()
