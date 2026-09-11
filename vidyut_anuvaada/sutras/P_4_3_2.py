# Sutra प.4.3.2: तस्मिन्नणि च युष्माकास्माकौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tasminnaRi ca yuzmAkAsmAkO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.2"
SUTRA_TEXT = "तस्मिन्नणि च युष्माकास्माकौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tasminnaRi ca yuzmAkAsmAkO"


class Sutra432:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.2: अग्निः'),
		('रामः', '', 'प.4.3.2: रामः'),
		('सीता', '', 'प.4.3.2: सीता'),
	]

