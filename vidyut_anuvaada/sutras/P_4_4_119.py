# Sutra प.4.4.119: बर्हिषि दत्तम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — barhizi dattam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.119"
SUTRA_TEXT = "बर्हिषि दत्तम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — barhizi dattam"


class Sutra44119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.119: अग्निः'),
		('रामः', '', 'प.4.4.119: रामः'),
		('सीता', '', 'प.4.4.119: सीता'),
	]

