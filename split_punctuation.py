import unicodedata
import sys

def _is_punctuation(char):
  """Checks whether `chars` is a punctuation character."""
  cp = ord(char)
  # We treat all non-letter/number ASCII as punctuation.
  # Characters such as "^", "$", and "`" are not in the Unicode
  # Punctuation class but we treat them as punctuation anyways, for
  # consistency.
  if ((cp >= 33 and cp <= 47) or (cp >= 58 and cp <= 64) or
      (cp >= 91 and cp <= 96) or (cp >= 123 and cp <= 126)):
    return True
  cat = unicodedata.category(char)
  if cat.startswith("P"):
    return True
  return False

def _run_split_on_punc(text):
    """Splits punctuation on a piece of text."""
    chars = list(text)
    i = 0
    start_new_word = True
    output = []
    while i < len(chars):
      char = chars[i]
      if _is_punctuation(char):
        output.append([char])
        start_new_word = True
      else:
        if start_new_word:
          output.append([])
        start_new_word = False
        output[-1].append(char)
      i += 1

    return ' '.join(["".join(x) for x in output])

def replace_multi_whitespaces(line):
	return ' '.join(line.split())

def main():	

	with open(sys.argv[1], "r") as input_file:
		#if len(sys.argv) > 2:
		#	with output_file = open(sys.argv[2], "w") as output_file:
		for line in input_file:

			if line is '\n':
				print('')
			else:
				line = _run_split_on_punc(line)
				line = replace_multi_whitespaces(line)

				if line is not '':
					print(line)


if __name__ == '__main__':
    main()