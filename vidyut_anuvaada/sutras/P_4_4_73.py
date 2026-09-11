# Sutra प.4.4.73: निकटे वसति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — nikawe vasati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.73"
SUTRA_TEXT = "निकटे वसति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — nikawe vasati"


class Sutra4473:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.73: अग्निः'),
		('रामः', '', 'प.4.4.73: रामः'),
		('सीता', '', 'प.4.4.73: सीता'),
	]

