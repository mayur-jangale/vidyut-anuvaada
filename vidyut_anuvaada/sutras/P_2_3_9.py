# Sutra प.2.3.9: यस्मादधिकं यस्य चेश्वरवचनं तत्र सप्तमी
# (Samasa (compound formation)) — yasmAdaDikaM yasya ceSvaravacanaM tatra saptamI

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.9"
SUTRA_TEXT = "यस्मादधिकं यस्य चेश्वरवचनं तत्र सप्तमी"
SUTRA_DESC = "(Samasa (compound formation)) — yasmAdaDikaM yasya ceSvaravacanaM tatra saptamI"


class Sutra239:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

