# Sutra प.6.2.127: चीरमुपमानम्
# (Sandhi (euphonic combination)) — cIramupamAnam

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.127"
SUTRA_TEXT = "चीरमुपमानम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — cIramupamAnam"


class Sutra62127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.127: अग्निः'),
		('रामः', '', 'प.6.2.127: रामः'),
		('सीता', '', 'प.6.2.127: सीता'),
	]

