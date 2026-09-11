# Sutra प.4.2.134: मनुष्यतत्स्थयोर्वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — manuzyatatsTayorvuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.134"
SUTRA_TEXT = "मनुष्यतत्स्थयोर्वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — manuzyatatsTayorvuY"


class Sutra42134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.134: अग्निः'),
		('रामः', '', 'प.4.2.134: रामः'),
		('सीता', '', 'प.4.2.134: सीता'),
	]

