# Sutra प.5.1.86: द्विगोर्वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvigorvA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.86"
SUTRA_TEXT = "द्विगोर्वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvigorvA"


class Sutra5186:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.86: अग्निः'),
		('रामः', '', 'प.5.1.86: रामः'),
		('सीता', '', 'प.5.1.86: सीता'),
	]

