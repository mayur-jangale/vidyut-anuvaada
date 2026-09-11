# Sutra प.4.4.125: तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tadvAnAsAmupaDAno mantra itIzwakAsu luk ca matoH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.125"
SUTRA_TEXT = "तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tadvAnAsAmupaDAno mantra itIzwakAsu luk ca matoH"


class Sutra44125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.125: अग्निः'),
		('रामः', '', 'प.4.4.125: रामः'),
		('सीता', '', 'प.4.4.125: सीता'),
	]

