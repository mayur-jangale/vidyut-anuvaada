# Sutra प.7.3.61: भुजन्युब्जौ पाण्युपतापयोः
# (Taddhita (secondary derivations)) — BujanyubjO pARyupatApayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.61"
SUTRA_TEXT = "भुजन्युब्जौ पाण्युपतापयोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — BujanyubjO pARyupatApayoH"


class Sutra7361:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.61: अग्निः'),
		('रामः', '', 'प.7.3.61: रामः'),
		('सीता', '', 'प.7.3.61: सीता'),
	]

