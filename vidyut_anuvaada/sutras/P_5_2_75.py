# Sutra प.5.2.75: पार्श्वेनान्विच्छति
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pArSvenAnvicCati

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.75"
SUTRA_TEXT = "पार्श्वेनान्विच्छति"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pArSvenAnvicCati"


class Sutra5275:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.75: अग्निः'),
		('रामः', '', 'प.5.2.75: रामः'),
		('सीता', '', 'प.5.2.75: सीता'),
	]

