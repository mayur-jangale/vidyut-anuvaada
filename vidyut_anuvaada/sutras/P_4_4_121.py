# Sutra प.4.4.121: रक्षोयातूनां हननी
# (Sup-sthāna (nominal endings) and kṛt-affixes) — rakzoyAtUnAM hananI

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.121"
SUTRA_TEXT = "रक्षोयातूनां हननी"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — rakzoyAtUnAM hananI"


class Sutra44121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.121: अग्निः'),
		('रामः', '', 'प.4.4.121: रामः'),
		('सीता', '', 'प.4.4.121: सीता'),
	]

