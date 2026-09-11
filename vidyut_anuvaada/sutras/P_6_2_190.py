# Sutra प.6.2.190: पुरुषश्चान्वादिष्टः
# (Sandhi (euphonic combination)) — puruzaScAnvAdizwaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.190"
SUTRA_TEXT = "पुरुषश्चान्वादिष्टः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — puruzaScAnvAdizwaH"


class Sutra62190:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.190: अग्निः'),
		('रामः', '', 'प.6.2.190: रामः'),
		('सीता', '', 'प.6.2.190: सीता'),
	]

