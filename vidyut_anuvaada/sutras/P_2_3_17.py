# Sutra प.2.3.17: मन्यकर्मण्यनादरे विभाषाऽप्राणिषु
# (Samasa (compound formation)) — manyakarmaRyanAdare viBAzA'prARizu

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.17"
SUTRA_TEXT = "मन्यकर्मण्यनादरे विभाषाऽप्राणिषु"
SUTRA_DESC = "(Samasa (compound formation)) — manyakarmaRyanAdare viBAzA'prARizu"


class Sutra2317:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

