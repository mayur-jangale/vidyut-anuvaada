# Sutra प.7.1.15: ङसिङ्योः स्मात्स्मिनौ
# (Taddhita (secondary derivations)) — NasiNyoH smAtsminO

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.15"
SUTRA_TEXT = "ङसिङ्योः स्मात्स्मिनौ"
SUTRA_DESC = "(Taddhita (secondary derivations)) — NasiNyoH smAtsminO"


class Sutra7115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.15: अग्निः'),
		('रामः', '', 'प.7.1.15: रामः'),
		('सीता', '', 'प.7.1.15: सीता'),
	]

