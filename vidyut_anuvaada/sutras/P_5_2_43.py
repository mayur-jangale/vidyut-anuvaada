# Sutra प.5.2.43: द्वित्रिभ्यां तयस्यायज्वा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitriByAM tayasyAyajvA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.43"
SUTRA_TEXT = "द्वित्रिभ्यां तयस्यायज्वा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitriByAM tayasyAyajvA"


class Sutra5243:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.43: अग्निः'),
		('रामः', '', 'प.5.2.43: रामः'),
		('सीता', '', 'प.5.2.43: सीता'),
	]

