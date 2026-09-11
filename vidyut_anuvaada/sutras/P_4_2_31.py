# Sutra प.4.2.31: वाय्वृतुपित्रुषसो यत्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — vAyvftupitruzaso yat

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.31"
SUTRA_TEXT = "वाय्वृतुपित्रुषसो यत्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — vAyvftupitruzaso yat"


class Sutra4231:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.31: अग्निः'),
		('रामः', '', 'प.4.2.31: रामः'),
		('सीता', '', 'प.4.2.31: सीता'),
	]

