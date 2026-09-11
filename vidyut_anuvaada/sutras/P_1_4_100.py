# Sutra प.1.4.100: तङानावात्मनेपदम्
# (Samjna (technical definitions)) — taNAnAvAtmanepadam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.100"
SUTRA_TEXT = "तङानावात्मनेपदम्"
SUTRA_DESC = "(Samjna (technical definitions)) — taNAnAvAtmanepadam"


class Sutra14100:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_100
		return apply_1_4_100(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-Atmanepada:अग्निः'),
		('रामः', '', 'not-Atmanepada:रामः'),
		('सीता', '', 'not-Atmanepada:सीता'),
	]

