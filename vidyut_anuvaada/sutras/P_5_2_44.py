# Sutra प.5.2.44: उभादुदात्तो नित्यम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — uBAdudAtto nityam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.44"
SUTRA_TEXT = "उभादुदात्तो नित्यम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — uBAdudAtto nityam"


class Sutra5244:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.44: अग्निः'),
		('रामः', '', 'प.5.2.44: रामः'),
		('सीता', '', 'प.5.2.44: सीता'),
	]

