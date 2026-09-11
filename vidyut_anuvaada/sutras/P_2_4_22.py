# Sutra प.2.4.22: छाया बाहुल्ये
# (Samasa (compound formation)) — CAyA bAhulye

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.22"
SUTRA_TEXT = "छाया बाहुल्ये"
SUTRA_DESC = "(Samasa (compound formation)) — CAyA bAhulye"


class Sutra2422:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

