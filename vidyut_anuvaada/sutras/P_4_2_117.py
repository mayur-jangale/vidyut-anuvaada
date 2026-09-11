# Sutra प.4.2.117: वाहीकग्रामेभ्यश्च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vAhIkagrAmeByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.117"
SUTRA_TEXT = "वाहीकग्रामेभ्यश्च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vAhIkagrAmeByaSca"


class Sutra42117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.117: अग्निः'),
		('रामः', '', 'प.4.2.117: रामः'),
		('सीता', '', 'प.4.2.117: सीता'),
	]

