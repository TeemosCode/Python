#simple practice of using OCR - Tesseract
import subprocess, os
#ocr = subprocess.Popen("tesseract PathOfImageForProcess PathOfResult(InTextFormat .txt)ForSaving[.txt will be added by default, do not needa specify]")
#ocr.wait() : it usually takes a while for program to process image then save it. Waits for all process to finish b4 moving on to the next codes

if not os.path.exists("./textImages"):
	os.mkdir("textImages")
if not os.path.exists("./textResults"):
	os.mkdir("textResults")

ocr = subprocess.Popen("./textImages/loveletter.jpg ./textResults/loveLetterResult")
ocr.wait() # wait for it~~~~~
text = open("./textResults/loveLetterResult.txt").read().strip()
print(text)
text.close()

