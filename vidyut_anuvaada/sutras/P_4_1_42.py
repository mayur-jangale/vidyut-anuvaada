# Sutra प.4.1.42: जानपदकुण्डगोणस्थलभाजनागकालनीलकुशकामुककबराद्वृत्त्यमत्रावपनाकृत्रिमाश्राणास्थौल्यवर्णानाच्छादनायोविकारमैथुनेच्छाकेशवेशेषु
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.42"
SUTRA_TEXT = "जानपदकुण्डगोणस्थलभाजनागकालनीलकुशकामुककबराद्वृत्त्यमत्रावपनाकृत्रिमाश्राणास्थौल्यवर्णानाच्छादनायोविकारमैथुनेच्छाकेशवेशेषु"
SUTRA_DESC = "supaḥ — continued"


class Sutra4142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

