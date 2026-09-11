# Sutra प.1.1.32: विभाषा जसि
# (Samjna (technical definitions)) — viBAzA jasi

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.32"
SUTRA_TEXT = "विभाषा जसि"
SUTRA_DESC = "(Samjna (technical definitions)) — viBAzA jasi"


class Sutra1132:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_32
		return apply_1_1_32(word, pos)

	EXAMPLES = [
		('देवाः', 'jas', 'optional-jas:देवाः'),
		('देव', '', 'non-jas:देव'),
	]

