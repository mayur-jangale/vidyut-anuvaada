# Sutra प.5.2.112: रजःकृष्यासुतिपरिषदो वलच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — rajaHkfzyAsutiparizado valac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.112"
SUTRA_TEXT = "रजःकृष्यासुतिपरिषदो वलच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — rajaHkfzyAsutiparizado valac"


class Sutra52112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.112: अग्निः'),
		('रामः', '', 'प.5.2.112: रामः'),
		('सीता', '', 'प.5.2.112: सीता'),
	]

