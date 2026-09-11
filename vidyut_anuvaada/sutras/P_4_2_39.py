# Sutra प.4.2.39: गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद्वुञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — gotrokzozwroraBrarAjarAjanyarAjaputravatsamanuzyAjAdvuY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.39"
SUTRA_TEXT = "गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद्वुञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — gotrokzozwroraBrarAjarAjanyarAjaputravatsamanuzyAjAdvuY"


class Sutra4239:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.39: अग्निः'),
		('रामः', '', 'प.4.2.39: रामः'),
		('सीता', '', 'प.4.2.39: सीता'),
	]

