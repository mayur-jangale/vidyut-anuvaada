# Sutra प.5.2.129: वातातिसाराभ्यां कुक् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vAtAtisArAByAM kuk ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.129"
SUTRA_TEXT = "वातातिसाराभ्यां कुक् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vAtAtisArAByAM kuk ca"


class Sutra52129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.129: अग्निः'),
		('रामः', '', 'प.5.2.129: रामः'),
		('सीता', '', 'प.5.2.129: सीता'),
	]

