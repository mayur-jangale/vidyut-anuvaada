# Sutra प.2.4.16: विभाषा समीपे
# (Samasa (compound formation)) — viBAzA samIpe

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.16"
SUTRA_TEXT = "विभाषा समीपे"
SUTRA_DESC = "(Samasa (compound formation)) — viBAzA samIpe"


class Sutra2416:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

