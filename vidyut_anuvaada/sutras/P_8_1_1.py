# Sutra प.8.1.1: सर्वस्य द्वे
# anunāsikādi — beginning of anunāsika-related rules

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.1"
SUTRA_TEXT = "सर्वस्य द्वे"
SUTRA_DESC = "anunāsikādi — beginning of anunāsika-related rules"


class Sutra811:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.1: अग्निः'),
		('रामः', '', 'प.8.1.1: रामः'),
		('सीता', '', 'प.8.1.1: सीता'),
	]

