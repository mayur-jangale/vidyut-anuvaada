# Sutra प.4.3.8: मध्यान्मः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — maDyAnmaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.8"
SUTRA_TEXT = "मध्यान्मः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — maDyAnmaH"


class Sutra438:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.8: अग्निः'),
		('रामः', '', 'प.4.3.8: रामः'),
		('सीता', '', 'प.4.3.8: सीता'),
	]

