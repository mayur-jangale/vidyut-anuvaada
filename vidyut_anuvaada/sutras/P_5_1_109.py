# Sutra प.5.1.109: प्रयोजनम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prayojanam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.109"
SUTRA_TEXT = "प्रयोजनम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prayojanam"


class Sutra51109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.109: अग्निः'),
		('रामः', '', 'प.5.1.109: रामः'),
		('सीता', '', 'प.5.1.109: सीता'),
	]

