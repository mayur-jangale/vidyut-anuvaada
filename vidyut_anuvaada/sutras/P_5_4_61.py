# Sutra प.5.4.61: सपत्त्रनिष्पत्रादतिव्यथने
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sapattranizpatrAdativyaTane

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.61"
SUTRA_TEXT = "सपत्त्रनिष्पत्रादतिव्यथने"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sapattranizpatrAdativyaTane"


class Sutra5461:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.61: अग्निः'),
		('रामः', '', 'प.5.4.61: रामः'),
		('सीता', '', 'प.5.4.61: सीता'),
	]

