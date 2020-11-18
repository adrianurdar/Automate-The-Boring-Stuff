#! python3
# urlExtractor.py - Find website URLs from the clipboard.

import pyperclip, re

def main():
     # Copy the text from the clipboard
     text = pyperclip.paste()

     # Create a regex to identify URLs - regex taken from https://gist.github.com/gruber/8891611
     urlRegex = re.compile(r'''(
          \b
          (					               # Capture 1: entire matched URL
          (?:
          https?:				               # URL protocol and colon
          (?:
          /{1,3}				               # 1-3 slashes
          |					               # Or
          [a-z0-9%]				               # Single letter or digit or '%'
      	# (Trying not to match e.g. "URI::Escape")
          )
          |					               # Or
    		# looks like domain name followed by a slash:
          [a-z0-9.\-]+[.]
          (?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj| Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)
          /
          )
          (?:                                     # One or more:
          [^\s()<>{}\[\]]+					# Run of non-space, non-()<>{}[]
          |								# Or
          \([^\s()]*?\([^\s()]+\)[^\s()]*?\)      # Balanced parens, one level deep: (…(…)…)
          |
          \([^\s]+?\)						# Balanced parens, non-recursive: (…)
          )+
          (?:							     # End with:
          \([^\s()]*?\([^\s()]+\)[^\s()]*?\)      # Balanced parens, one level deep: (…(…)…)
          |
          \([^\s]+?\)						# Balanced parens, non-recursive: (…)
          |								# Or
          [^\s`!()\[\]{};:'".,<>?«»“”‘’]		# Not a space or one of these punct chars
          )
          |					               # Or, the following to match naked domains:
          (?:
  	     (?<!@)			                    # Not preceded by a @, avoid matching foo@_gmail.com_
          [a-z0-9]+
          (?:[.\-][a-z0-9]+)*
          [.]
          (?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj| Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)
          \b
          /?
          (?!@)			                    # Not succeeded by a @, avoid matching "foo.na" in "foo.na@example.com"
          )
          )
     )''', re.VERBOSE)

     # Find all urls in text
     matches = []
     for groups in urlRegex.findall(text):
          matches.append(groups[0])

     # Copy the result to the clipboard
     if len(matches) > 0:
          pyperclip.copy('\n'.join(matches))
          print('Copied to clipboard:')
          print('\n'.join(matches))
     else:
          # Display a message if no URLs are found
          print('No URLs were found.')


if __name__ == '__main__':
     main()
