# Sutra प.1.2.52: विशेषणानां चाजातेः
# (Samjna (technical definitions)) — viSezaRAnAM cAjAteH

from P_1_2 import apply_1_2_52

SUTRA_CODE = "प.1.2.52"
SUTRA_TEXT = "विशेषणानां चाजातेः"
SUTRA_DESC = "(Samjna (technical definitions)) — viSezaRAnAM cAjAteH"


class Sutra1252:
	def apply(self, word, pos):
		return apply_1_2_52(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-viśeṣaṇa:अग्निः'),
		('रामः', '', 'non-viśeṣaṇa:रामः'),
		('सीता', '', 'non-viśeṣaṇa:सीता'),
	]

