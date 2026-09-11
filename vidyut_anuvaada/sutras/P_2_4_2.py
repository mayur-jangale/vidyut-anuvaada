# Sutra प.2.4.2: द्वन्द्वश्च प्राणितूर्यसेनाङ्गानाम्
# (Samasa (compound formation)) — dvandvaSca prARitUryasenANgAnAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.2"
SUTRA_TEXT = "द्वन्द्वश्च प्राणितूर्यसेनाङ्गानाम्"
SUTRA_DESC = "(Samasa (compound formation)) — dvandvaSca prARitUryasenANgAnAm"


class Sutra242:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

