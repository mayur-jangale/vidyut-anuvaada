# Sutra प.4.4.120: दूतस्य भागकर्मणी
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dUtasya BAgakarmaRI

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.120"
SUTRA_TEXT = "दूतस्य भागकर्मणी"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dUtasya BAgakarmaRI"


class Sutra44120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.120: अग्निः'),
		('रामः', '', 'प.4.4.120: रामः'),
		('सीता', '', 'प.4.4.120: सीता'),
	]

