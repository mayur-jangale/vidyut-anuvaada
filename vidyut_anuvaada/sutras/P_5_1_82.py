# Sutra प.5.1.82: द्विगोर्यप्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvigoryap

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.82"
SUTRA_TEXT = "द्विगोर्यप्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvigoryap"


class Sutra5182:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.82: अग्निः'),
		('रामः', '', 'प.5.1.82: रामः'),
		('सीता', '', 'प.5.1.82: सीता'),
	]

