# Sutra प.5.4.76: अक्ष्णोऽदर्शनात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — akzRo'darSanAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.76"
SUTRA_TEXT = "अक्ष्णोऽदर्शनात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — akzRo'darSanAt"


class Sutra5476:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.76: अग्निः'),
		('रामः', '', 'प.5.4.76: रामः'),
		('सीता', '', 'प.5.4.76: सीता'),
	]

