# Sutra प.4.2.135: अपदातौ साल्वात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — apadAtO sAlvAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.135"
SUTRA_TEXT = "अपदातौ साल्वात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — apadAtO sAlvAt"


class Sutra42135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.135: अग्निः'),
		('रामः', '', 'प.4.2.135: रामः'),
		('सीता', '', 'प.4.2.135: सीता'),
	]

