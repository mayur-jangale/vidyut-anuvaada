# Sutra प.1.1.19: ईदूतौ च सप्तम्यर्थे
# īdūtau ca saptamyarṭe — Ī and Ū are used in seventh case sense

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.19"
SUTRA_TEXT = "ईदूतौ च सप्तम्यर्थे"
SUTRA_DESC = "īdūtau ca saptamyarṭe — Ī and Ū are used in seventh case sense"


class Sutra1119:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_19
		return apply_1_1_19(word, pos)

	EXAMPLES = [
		('ई', '', 'īdū-saptamī:ई'),
		('अग्नि', '', 'non-īdū:अग्नि'),
	]

