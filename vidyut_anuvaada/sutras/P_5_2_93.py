# Sutra प.5.2.93: इन्द्रियमिन्द्रलिंगमिन्द्रदृष्टमिन्द्रसृष्टमिन्द्रजुष्टमिन्द्रदत्तमिति वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — indriyamindraliMgamindradfzwamindrasfzwamindrajuzwamindradattamiti vA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.93"
SUTRA_TEXT = "इन्द्रियमिन्द्रलिंगमिन्द्रदृष्टमिन्द्रसृष्टमिन्द्रजुष्टमिन्द्रदत्तमिति वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — indriyamindraliMgamindradfzwamindrasfzwamindrajuzwamindradattamiti vA"


class Sutra5293:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.93: अग्निः'),
		('रामः', '', 'प.5.2.93: रामः'),
		('सीता', '', 'प.5.2.93: सीता'),
	]

