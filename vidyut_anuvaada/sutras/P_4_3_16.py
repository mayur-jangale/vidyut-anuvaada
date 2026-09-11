# Sutra प.4.3.16: संधिवेलाद्यृतुनक्षत्रेभ्योऽण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMDivelAdyftunakzatreByo'R

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.16"
SUTRA_TEXT = "संधिवेलाद्यृतुनक्षत्रेभ्योऽण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMDivelAdyftunakzatreByo'R"


class Sutra4316:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.16: अग्निः'),
		('रामः', '', 'प.4.3.16: रामः'),
		('सीता', '', 'प.4.3.16: सीता'),
	]

