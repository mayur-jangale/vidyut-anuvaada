# Sutra प.2.3.69: न लोकाव्ययनिष्ठाखलर्थतृनाम्
# (Samasa (compound formation)) — na lokAvyayanizWAKalarTatfnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.69"
SUTRA_TEXT = "न लोकाव्ययनिष्ठाखलर्थतृनाम्"
SUTRA_DESC = "(Samasa (compound formation)) — na lokAvyayanizWAKalarTatfnAm"


class Sutra2369:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

