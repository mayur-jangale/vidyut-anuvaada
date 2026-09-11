# Sutra प.1.2.11: लिङ्सिचावात्मनेपदेषु
# (Samjna (technical definitions)) — liNsicAvAtmanepadezu

from P_1_2 import apply_1_2_11

SUTRA_CODE = "प.1.2.11"
SUTRA_TEXT = "लिङ्सिचावात्मनेपदेषु"
SUTRA_DESC = "(Samjna (technical definitions)) — liNsicAvAtmanepadezu"


class Sutra1211:
	def apply(self, word, pos):
		return apply_1_2_11(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'parasmai-pada:अग्निः'),
		('रामः', '', 'parasmai-pada:रामः'),
		('सीता', '', 'parasmai-pada:सीता'),
	]

