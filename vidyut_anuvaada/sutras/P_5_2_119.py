# Sutra प.5.2.119: शतसहस्रान्ताच्च निष्कात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SatasahasrAntAcca nizkAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.119"
SUTRA_TEXT = "शतसहस्रान्ताच्च निष्कात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SatasahasrAntAcca nizkAt"


class Sutra52119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.119: अग्निः'),
		('रामः', '', 'प.5.2.119: रामः'),
		('सीता', '', 'प.5.2.119: सीता'),
	]

