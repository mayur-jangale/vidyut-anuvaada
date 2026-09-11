# Sutra प.7.2.44: स्वरतिसूतिसूयतिधूञूदितो वा
# (Taddhita (secondary derivations)) — svaratisUtisUyatiDUYUdito vA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.44"
SUTRA_TEXT = "स्वरतिसूतिसूयतिधूञूदितो वा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — svaratisUtisUyatiDUYUdito vA"


class Sutra7244:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.44: अग्निः'),
		('रामः', '', 'प.7.2.44: रामः'),
		('सीता', '', 'प.7.2.44: सीता'),
	]

