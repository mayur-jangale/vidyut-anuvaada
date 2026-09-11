# Sutra प.7.2.27: वा दान्तशान्तपूर्णदस्तस्पष्टच्छन्नज्ञप्ताः
# (Taddhita (secondary derivations)) — vA dAntaSAntapUrRadastaspazwacCannajYaptAH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.27"
SUTRA_TEXT = "वा दान्तशान्तपूर्णदस्तस्पष्टच्छन्नज्ञप्ताः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — vA dAntaSAntapUrRadastaspazwacCannajYaptAH"


class Sutra7227:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.27: अग्निः'),
		('रामः', '', 'प.7.2.27: रामः'),
		('सीता', '', 'प.7.2.27: सीता'),
	]

