# Sutra प.1.2.54: लुब्योगाप्रख्यानात्
# (Samjna (technical definitions)) — lubyogApraKyAnAt

from P_1_2 import apply_1_2_54

SUTRA_CODE = "प.1.2.54"
SUTRA_TEXT = "लुब्योगाप्रख्यानात्"
SUTRA_DESC = "(Samjna (technical definitions)) — lubyogApraKyAnAt"


class Sutra1254:
	def apply(self, word, pos):
		return apply_1_2_54(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'lub-yoga-apraKya:अग्निः;no-explicit-usage'),
		('रामः', '', 'lub-yoga-apraKya:रामः;no-explicit-usage'),
		('सीता', '', 'lub-yoga-apraKya:सीता;no-explicit-usage'),
	]

