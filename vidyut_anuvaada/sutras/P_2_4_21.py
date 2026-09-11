# Sutra प.2.4.21: उपज्ञोपक्रमं तदाद्याचिख्यासायाम्
# (Samasa (compound formation)) — upajYopakramaM tadAdyAciKyAsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.2.4.21"
SUTRA_TEXT = "उपज्ञोपक्रमं तदाद्याचिख्यासायाम्"
SUTRA_DESC = "(Samasa (compound formation)) — upajYopakramaM tadAdyAciKyAsAyAm"


class Sutra2421:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

