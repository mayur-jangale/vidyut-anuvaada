# Sutra प.5.1.123: वर्णदृढादिभ्यः ष्यञ् च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — varRadfQAdiByaH zyaY ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.123"
SUTRA_TEXT = "वर्णदृढादिभ्यः ष्यञ् च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — varRadfQAdiByaH zyaY ca"


class Sutra51123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.123: अग्निः'),
		('रामः', '', 'प.5.1.123: रामः'),
		('सीता', '', 'प.5.1.123: सीता'),
	]

