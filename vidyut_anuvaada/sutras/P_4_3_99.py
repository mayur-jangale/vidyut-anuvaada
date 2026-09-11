# Sutra प.4.3.99: गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gotrakzatriyAKyeByo bahulaM vuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.99"
SUTRA_TEXT = "गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gotrakzatriyAKyeByo bahulaM vuY"


class Sutra4399:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.99: अग्निः'),
		('रामः', '', 'प.4.3.99: रामः'),
		('सीता', '', 'प.4.3.99: सीता'),
	]

