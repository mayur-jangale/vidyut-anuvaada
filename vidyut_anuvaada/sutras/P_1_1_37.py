# Sutra प.1.1.37: स्वरादिनिपातमव्ययम्
# (Samjna (technical definitions)) — svarAdinipAtamavyayam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.37"
SUTRA_TEXT = "स्वरादिनिपातमव्ययम्"
SUTRA_DESC = "(Samjna (technical definitions)) — svarAdinipAtamavyayam"


class Sutra1137:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_37
		return apply_1_1_37(word, pos)

	EXAMPLES = [
		('च', '', 'avyaya:च'),
		('तु', '', 'avyaya:तु'),
		('यथा', '', 'avyaya:यथा'),
		('देवः', '', 'non-avyaya:देवः'),
	]

