# Sutra प.1.2.33: एकश्रुति दूरात् सम्बुद्धौ
# (Samjna (technical definitions)) — ekaSruti dUrAt sambudDO

from P_1_2 import apply_1_2_33

SUTRA_CODE = "प.1.2.33"
SUTRA_TEXT = "एकश्रुति दूरात् सम्बुद्धौ"
SUTRA_DESC = "(Samjna (technical definitions)) — ekaSruti dUrAt sambudDO"


class Sutra1233:
	def apply(self, word, pos):
		return apply_1_2_33(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-sambodhana:अग्निः'),
		('रामः', '', 'non-sambodhana:रामः'),
		('सीता', '', 'non-sambodhana:सीता'),
	]

