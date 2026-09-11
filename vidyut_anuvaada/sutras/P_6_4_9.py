# Sutra प.6.4.9: वा षपूर्वस्य निगमे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.9"
SUTRA_TEXT = "वा षपूर्वस्य निगमे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra649:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.9: अग्निः'),
		('रामः', '', 'प.6.4.9: रामः'),
		('सीता', '', 'प.6.4.9: सीता'),
	]

