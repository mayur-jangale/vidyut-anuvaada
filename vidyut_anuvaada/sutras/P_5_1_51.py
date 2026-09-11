# Sutra प.5.1.51: वस्नद्रव्याभ्यां ठन्कनौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vasnadravyAByAM WankanO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.51"
SUTRA_TEXT = "वस्नद्रव्याभ्यां ठन्कनौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vasnadravyAByAM WankanO"


class Sutra5151:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.51: अग्निः'),
		('रामः', '', 'प.5.1.51: रामः'),
		('सीता', '', 'प.5.1.51: सीता'),
	]

