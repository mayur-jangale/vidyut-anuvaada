# Sutra प.5.3.65: विन्मतोर्लुक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vinmatorluk

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.65"
SUTRA_TEXT = "विन्मतोर्लुक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vinmatorluk"


class Sutra5365:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.65: अग्निः'),
		('रामः', '', 'प.5.3.65: रामः'),
		('सीता', '', 'प.5.3.65: सीता'),
	]

