# Sutra प.5.4.20: विभाषा बहोर्धाविप्रकृष्टकाले
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA bahorDAviprakfzwakAle

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.20"
SUTRA_TEXT = "विभाषा बहोर्धाविप्रकृष्टकाले"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viBAzA bahorDAviprakfzwakAle"


class Sutra5420:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.20: अग्निः'),
		('रामः', '', 'प.5.4.20: रामः'),
		('सीता', '', 'प.5.4.20: सीता'),
	]

