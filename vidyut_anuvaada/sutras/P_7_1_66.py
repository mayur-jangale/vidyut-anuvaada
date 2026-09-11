# Sutra प.7.1.66: उपात् प्रशंसायाम्
# (Taddhita (secondary derivations)) — upAt praSaMsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.66"
SUTRA_TEXT = "उपात् प्रशंसायाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — upAt praSaMsAyAm"


class Sutra7166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.66: अग्निः'),
		('रामः', '', 'प.7.1.66: रामः'),
		('सीता', '', 'प.7.1.66: सीता'),
	]

