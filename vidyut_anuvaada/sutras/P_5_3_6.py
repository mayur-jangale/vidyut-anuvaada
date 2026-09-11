# Sutra प.5.3.6: सर्वस्य सोऽन्यतरस्यां दि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — sarvasya so'nyatarasyAM di

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.6"
SUTRA_TEXT = "सर्वस्य सोऽन्यतरस्यां दि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — sarvasya so'nyatarasyAM di"


class Sutra536:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.6: अग्निः'),
		('रामः', '', 'प.5.3.6: रामः'),
		('सीता', '', 'प.5.3.6: सीता'),
	]

