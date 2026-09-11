# Sutra प.4.4.108: समानोदरे शयित ओ चोदात्तः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — samAnodare Sayita o codAttaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.108"
SUTRA_TEXT = "समानोदरे शयित ओ चोदात्तः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — samAnodare Sayita o codAttaH"


class Sutra44108:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.108: अग्निः'),
		('रामः', '', 'प.4.4.108: रामः'),
		('सीता', '', 'प.4.4.108: सीता'),
	]

