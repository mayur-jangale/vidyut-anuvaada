# Sutra प.1.3.4: न विभक्तौ तुस्माः
from P_1_3 import apply_1_3_4


class Sutra134:
	def apply(self, word, pos):
		return apply_1_3_4(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'vibhakti-no-tusmah:अग्निः;flag=no'),
		('रामः', '', 'vibhakti-no-tusmah:रामः;flag=no'),
		('सीता', '', 'vibhakti-no-tusmah:सीता;flag=no'),
	]

