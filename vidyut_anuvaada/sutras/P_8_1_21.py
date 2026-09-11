# Sutra प.8.1.21: बहुवचनस्य वस्नसौ
# ṅamo halaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.21"
SUTRA_TEXT = "बहुवचनस्य वस्नसौ"
SUTRA_DESC = "ṅamo halaḥ — repeated"


class Sutra8121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.21: अग्निः'),
		('रामः', '', 'प.8.1.21: रामः'),
		('सीता', '', 'प.8.1.21: सीता'),
	]

