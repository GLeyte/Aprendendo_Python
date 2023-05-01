import spacy

# Carregue o modelo spaCy para o português
nlp = spacy.load("pt_core_news_lg")

# Defina a lista de sintomas
sintomas = ["dor de cabeça", "febre", "tosse persistente", "fadiga", "calafrios"]

# Defina o texto a ser analisado
text = """A doença pulmonar obstrutiva crônica ou DPOC ocorre quando há obstrução da passagem de ar nos pulmões por diversas causas. A asma por exemplo é considerada uma DPOC, nesse caso, a mucosa e a redução do raio dos brônquios fazem com que o raio dos brônquios sejam reduzidos e assim o fluxo de ar é comprometido. Importante salientar que o fluxo de ar é inversamente proporcional ao raio da via respiratória elevado à quarta potência. Nesse caso, há uma redução do fluxo de ar e assim uma diminuição da ventilação pulmonar. Outra DPOC muito comum é a fibrose pulmonar na qual é formado um tecido fibroso ao redor dos aovéolos pulmonares, isso compromete a sua elastância e assim compromete a ventilação pulmonar e as trocas gasosas. Os métodos de tratamento das DPOCS são variados, no caso da asma por exemplo, podem ser utilizados bronquidilatadores para auxiliar na abertura das vias respiratórias, aumentando o seu raio e permitindo uma maior passagem de ar. Além disso, podem ser usados remédios que estimulem o sistema nervoso e gerem uma broncodilatação."""

# Analise o texto com o modelo spaCy
doc = nlp(text)

# Iterar sobre as frases do texto e verificar se elas correspondem a algum sintoma na lista de sintomas
for sent in doc.sents:
    for sintoma in sintomas:
        if sintoma in sent.text:
            print("Sintoma encontrado:", sintoma)
