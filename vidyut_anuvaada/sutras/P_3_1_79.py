# Sutra प.3.1.79: तनादिकृञ्भ्य उः
# āṭ śānacā — āṭ augment before śānac

from P_3_1 import apply_3_1_79

SUTRA_CODE = "प.3.1.79"
SUTRA_TEXT = "तनादिकृञ्भ्य उः"
SUTRA_DESC = "āṭ śānacā — āṭ augment before śānac"


class Sutra3179:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_79(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.79:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.79:root=रामः;pos='),
		('सीता', '', 'प.3.1.79:root=सीता;pos='),
	]

