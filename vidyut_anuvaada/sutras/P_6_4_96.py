# Sutra प.6.4.96: छादेर्घेऽद्व्युपसर्गस्य
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.96"
SUTRA_TEXT = "छादेर्घेऽद्व्युपसर्गस्य"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6496:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.96: अग्निः'),
		('रामः', '', 'प.6.4.96: रामः'),
		('सीता', '', 'प.6.4.96: सीता'),
	]

