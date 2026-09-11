# Sutra प.6.4.88: भुवो वुग्लुङ्लिटोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.88"
SUTRA_TEXT = "भुवो वुग्लुङ्लिटोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6488:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.88: अग्निः'),
		('रामः', '', 'प.6.4.88: रामः'),
		('सीता', '', 'प.6.4.88: सीता'),
	]

