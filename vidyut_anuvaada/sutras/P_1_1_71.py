# Sutra प.1.1.71: आदिरन्त्येन सहेता
# (Samjna (technical definitions)) — Adirantyena sahetA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.71"
SUTRA_TEXT = "आदिरन्त्येन सहेता"
SUTRA_DESC = "(Samjna (technical definitions)) — Adirantyena sahetA"


class Sutra1171:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_71
		return apply_1_1_71(word, pos)

	EXAMPLES = [
		('आदि', '', 'प.1.1.71:ādirantyena-sahetā;input=आदि'),
		('अग्नि', '', 'प.1.1.71:ādirantyena-sahetā;input=अग्नि'),
	]

