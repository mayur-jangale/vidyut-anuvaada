# Sutra प.3.1.127: आनाय्योऽनित्ये
# lopo vyorvali — repeated pattern

from P_3_1 import apply_3_1_127

SUTRA_CODE = "प.3.1.127"
SUTRA_TEXT = "आनाय्योऽनित्ये"
SUTRA_DESC = "lopo vyorvali — repeated pattern"


class Sutra31127:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_127(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.127:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.127:root=रामः;pos='),
		('सीता', '', 'प.3.1.127:root=सीता;pos='),
	]

