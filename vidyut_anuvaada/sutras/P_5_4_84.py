# Sutra प.5.4.84: द्विस्तावा त्रिस्तावा वेदिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvistAvA tristAvA vediH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.84"
SUTRA_TEXT = "द्विस्तावा त्रिस्तावा वेदिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — dvistAvA tristAvA vediH"


class Sutra5484:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.84: अग्निः'),
		('रामः', '', 'प.5.4.84: रामः'),
		('सीता', '', 'प.5.4.84: सीता'),
	]

