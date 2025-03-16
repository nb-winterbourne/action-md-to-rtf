import pypandoc
import pathlib

def main():
	print('hello world!')
	pypandoc.convert_file('manuscript/*.md', 'rtf', outputfile="test.docx")

main()