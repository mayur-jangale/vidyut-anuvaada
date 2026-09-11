# Sutra प.4.3.92: शण्डिकादिभ्यो ञ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SaRqikAdiByo YyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.92"
SUTRA_TEXT = "शण्डिकादिभ्यो ञ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SaRqikAdiByo YyaH"


class Sutra4392:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.92: अग्निः'),
		('रामः', '', 'प.4.3.92: रामः'),
		('सीता', '', 'प.4.3.92: सीता'),
	]

