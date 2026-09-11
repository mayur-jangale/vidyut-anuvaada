# Sutra प.5.3.81: जातिनाम्नः कन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — jAtinAmnaH kan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.81"
SUTRA_TEXT = "जातिनाम्नः कन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — jAtinAmnaH kan"


class Sutra5381:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.81: अग्निः'),
		('रामः', '', 'प.5.3.81: रामः'),
		('सीता', '', 'प.5.3.81: सीता'),
	]

