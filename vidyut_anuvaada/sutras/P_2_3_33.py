# Sutra प.2.3.33: करणे च स्तोकाल्पकृच्छ्रकतिपयस्यासत्त्ववचनस्य
# (Samasa (compound formation)) — karaRe ca stokAlpakfcCrakatipayasyAsattvavacanasya

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.33"
SUTRA_TEXT = "करणे च स्तोकाल्पकृच्छ्रकतिपयस्यासत्त्ववचनस्य"
SUTRA_DESC = "(Samasa (compound formation)) — karaRe ca stokAlpakfcCrakatipayasyAsattvavacanasya"


class Sutra2333:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

