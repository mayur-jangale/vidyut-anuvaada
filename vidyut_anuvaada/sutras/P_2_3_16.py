# Sutra प.2.3.16: नमःस्वस्तिस्वाहास्वधालम्वषड्योगाच्च
# (Samasa (compound formation)) — namaHsvastisvAhAsvaDAlamvazaqyogAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.16"
SUTRA_TEXT = "नमःस्वस्तिस्वाहास्वधालम्वषड्योगाच्च"
SUTRA_DESC = "(Samasa (compound formation)) — namaHsvastisvAhAsvaDAlamvazaqyogAcca"


class Sutra2316:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

