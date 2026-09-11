# Sutra प.5.1.94: तदस्य ब्रह्मचर्यम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasya brahmacaryam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.94"
SUTRA_TEXT = "तदस्य ब्रह्मचर्यम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasya brahmacaryam"


class Sutra5194:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.94: अग्निः'),
		('रामः', '', 'प.5.1.94: रामः'),
		('सीता', '', 'प.5.1.94: सीता'),
	]

