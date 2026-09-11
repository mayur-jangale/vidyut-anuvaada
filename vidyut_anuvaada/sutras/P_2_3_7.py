# Sutra प.2.3.7: सप्तमीपञ्चम्यौ कारकमध्ये
# (Samasa (compound formation)) — saptamIpaYcamyO kArakamaDye

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.7"
SUTRA_TEXT = "सप्तमीपञ्चम्यौ कारकमध्ये"
SUTRA_DESC = "(Samasa (compound formation)) — saptamIpaYcamyO kArakamaDye"


class Sutra237:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

