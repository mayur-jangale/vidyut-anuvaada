# Sutra प.5.4.112: गिरेश्च सेनकस्य
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — gireSca senakasya

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.112"
SUTRA_TEXT = "गिरेश्च सेनकस्य"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — gireSca senakasya"


class Sutra54112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.112: अग्निः'),
		('रामः', '', 'प.5.4.112: रामः'),
		('सीता', '', 'प.5.4.112: सीता'),
	]

