# Sutra प.3.1.74: श्रुवः शृ च
# tṛjvatkṛvaccha — specific vikaraṇa patterns

from P_3_1 import apply_3_1_74

SUTRA_CODE = "प.3.1.74"
SUTRA_TEXT = "श्रुवः शृ च"
SUTRA_DESC = "tṛjvatkṛvaccha — specific vikaraṇa patterns"


class Sutra3174:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_74(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.74:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.74:root=रामः;pos='),
		('सीता', '', 'प.3.1.74:root=सीता;pos='),
	]

