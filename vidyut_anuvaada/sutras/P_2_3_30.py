# Sutra प.2.3.30: षष्ठ्यतसर्थप्रत्ययेन
# (Samasa (compound formation)) — zazWyatasarTapratyayena

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.30"
SUTRA_TEXT = "षष्ठ्यतसर्थप्रत्ययेन"
SUTRA_DESC = "(Samasa (compound formation)) — zazWyatasarTapratyayena"


class Sutra2330:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

