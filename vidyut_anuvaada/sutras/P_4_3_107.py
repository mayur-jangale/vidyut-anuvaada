# Sutra प.4.3.107: कठचरकाल्लुक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kaWacarakAlluk

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.107"
SUTRA_TEXT = "कठचरकाल्लुक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kaWacarakAlluk"


class Sutra43107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.107: अग्निः'),
		('रामः', '', 'प.4.3.107: रामः'),
		('सीता', '', 'प.4.3.107: सीता'),
	]

