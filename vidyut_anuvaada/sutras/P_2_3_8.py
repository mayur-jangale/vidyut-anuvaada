# Sutra प.2.3.8: कर्मप्रवचनीययुक्ते द्वितीया
# (Samasa (compound formation)) — karmapravacanIyayukte dvitIyA

from sutra_engines import apply_general

SUTRA_CODE = "प.2.3.8"
SUTRA_TEXT = "कर्मप्रवचनीययुक्ते द्वितीया"
SUTRA_DESC = "(Samasa (compound formation)) — karmapravacanIyayukte dvitIyA"


class Sutra238:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'samāsa: अग्निः'),
		('रामः', '', 'samāsa: रामः'),
		('सीता', '', 'samāsa: सीता'),
	]

