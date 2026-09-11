# Sutra प.5.3.45: द्वित्र्योश्च धमुञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitryoSca DamuY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.45"
SUTRA_TEXT = "द्वित्र्योश्च धमुञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvitryoSca DamuY"


class Sutra5345:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.45: अग्निः'),
		('रामः', '', 'प.5.3.45: रामः'),
		('सीता', '', 'प.5.3.45: सीता'),
	]

