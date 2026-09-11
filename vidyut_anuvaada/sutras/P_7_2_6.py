# Sutra प.7.2.6: ऊर्णोतेर्विभाषा
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.6"
SUTRA_TEXT = "ऊर्णोतेर्विभाषा"
SUTRA_DESC = "taddhita — continued"


class Sutra726:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.6: अग्निः'),
		('रामः', '', 'प.7.2.6: रामः'),
		('सीता', '', 'प.7.2.6: सीता'),
	]

