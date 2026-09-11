# Sutra प.2.3.29: अन्यारादितरर्तेदिक्छब्दाञ्चूत्तरपदाजाहियुक्ते
# (Samasa (compound formation)) — anyArAditarartedikCabdAYcUttarapadAjAhiyukte

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.29"
SUTRA_TEXT = "अन्यारादितरर्तेदिक्छब्दाञ्चूत्तरपदाजाहियुक्ते"
SUTRA_DESC = "(Samasa (compound formation)) — anyArAditarartedikCabdAYcUttarapadAjAhiyukte"


class Sutra2329:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

