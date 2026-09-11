# Sutra प.7.4.28: रिङ् शयग्लिङ्क्षु
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.28"
SUTRA_TEXT = "रिङ् शयग्लिङ्क्षु"
SUTRA_DESC = "taddhita — continued"


class Sutra7428:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.28: अग्निः'),
		('रामः', '', 'प.7.4.28: रामः'),
		('सीता', '', 'प.7.4.28: सीता'),
	]

