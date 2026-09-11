# Sutra प.3.4.81: लिटस्तझयोरेशिरेच्
# lut — periphrastic future endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.81"
SUTRA_TEXT = "लिटस्तझयोरेशिरेच्"
SUTRA_DESC = "lut — periphrastic future endings"


class Sutra3481:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

