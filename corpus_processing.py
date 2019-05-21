import re
import sys


#URLS_RE = re.compile(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b')
URLS_RE = re.compile(r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')

LISTING_RE = re.compile(r'^(|[a-z]?|[0-9]{0,3})(\-|\.)+( |\n)')

def remove_urls(text):
	return URLS_RE.sub('', text)

def replace_multi_whitespaces(line):
	return ' '.join(line.split())

def remove_listing(line):
	return LISTING_RE.sub('', line)

def main():	

	with open(sys.argv[1], "r") as input_file:

		for line in input_file:
			if line is '\n':
				print('')
			else:
				line = line.lower()
				line = remove_urls(line)
				line = remove_listing(line)
				line = replace_multi_whitespaces(line)

				if line is not '':
					print(line)



if __name__ == '__main__':
    main()
