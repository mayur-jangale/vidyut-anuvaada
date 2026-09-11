# Sutra प.4.3.37: नक्षत्रेभ्यो बहुलम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nakzatreByo bahulam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.37"
SUTRA_TEXT = "नक्षत्रेभ्यो बहुलम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nakzatreByo bahulam"


class Sutra4337:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.37: अग्निः'),
		('रामः', '', 'प.4.3.37: रामः'),
		('सीता', '', 'प.4.3.37: सीता'),
	]

