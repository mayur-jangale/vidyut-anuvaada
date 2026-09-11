# Sutra प.1.4.18: यचि भम्
# yañ sṛjāyām — the root यज् in sṛj sense gets special treatment

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.18"
SUTRA_TEXT = "यचि भम्"
SUTRA_DESC = "yañ sṛjāyām — the root यज् in sṛj sense gets special treatment"


class Sutra1418:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_18
		return apply_1_4_18(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-sRJ:अग्निः'),
		('रामः', '', 'not-sRJ:रामः'),
		('सीता', '', 'not-sRJ:सीता'),
	]

