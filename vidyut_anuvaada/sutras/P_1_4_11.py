# Sutra प.1.4.11: संयोगे गुरु
# (Samjna (technical definitions)) — saMyoge guru

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.11"
SUTRA_TEXT = "संयोगे गुरु"
SUTRA_DESC = "(Samjna (technical definitions)) — saMyoge guru"


class Sutra1411:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_11
		return apply_1_4_11(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-cluster:अग्निः'),
		('रामः', '', 'no-cluster:रामः'),
		('सीता', '', 'no-cluster:सीता'),
	]

