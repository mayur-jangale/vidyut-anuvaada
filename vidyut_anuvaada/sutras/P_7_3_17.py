# Sutra प.7.3.17: परिमाणान्तस्यासंज्ञाशाणयोः
# (Taddhita (secondary derivations)) — parimARAntasyAsaMjYASARayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.17"
SUTRA_TEXT = "परिमाणान्तस्यासंज्ञाशाणयोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — parimARAntasyAsaMjYASARayoH"


class Sutra7317:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.17: अग्निः'),
		('रामः', '', 'प.7.3.17: रामः'),
		('सीता', '', 'प.7.3.17: सीता'),
	]

