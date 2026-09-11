# Sutra प.7.4.96: विभाषा वेष्टिचेष्ट्योः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.96"
SUTRA_TEXT = "विभाषा वेष्टिचेष्ट्योः"
SUTRA_DESC = "taddhita — continued"


class Sutra7496:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.96: अग्निः'),
		('रामः', '', 'प.7.4.96: रामः'),
		('सीता', '', 'प.7.4.96: सीता'),
	]

