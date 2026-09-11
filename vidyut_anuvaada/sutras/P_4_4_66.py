# Sutra प.4.4.66: तदस्मै दीयते नियुक्तम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadasmE dIyate niyuktam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.66"
SUTRA_TEXT = "तदस्मै दीयते नियुक्तम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadasmE dIyate niyuktam"


class Sutra4466:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.66: अग्निः'),
		('रामः', '', 'प.4.4.66: रामः'),
		('सीता', '', 'प.4.4.66: सीता'),
	]

