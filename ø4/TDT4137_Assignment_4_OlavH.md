# TDT4137 - Øving 4 - Olav Reppe Husby

## Oppgave 1 &mdash; Icarus og CLARION

a) *Beskriv kort hovedmodulene i de kognitive arkitekturene ICARUS og CLARION*

**ICARUS**

ICARUS er en kognitiv arkitektur som fokuserer på fysiske agenter i en fysisk verden. ICARUS lenker kongnisjon til persepsjon og handlinger.

**CLARION**

ICARUS er en kognitiv arkitektur som fokuserer på en dualitet med tanke på representasjon av data, disse er eksplisitt og implisitt kunnskap.


b) *Gjør en sammenligning mellom de to arkitekturene med hensyn på*
1. *Underliggende filosofi og motivering*

  Icarus

  Den underliggende filosofien i Icarus er at man bør modellere et kognitivt system basert på realiteten, altså den fysiske verden.

  Icarus mener at langtidsminne og korttidsminne bør være forskjellige konsepter i et kognitivt system, siden de er forskjellige i virkelige hjerner. Icarus prøver også å bruke disse minnene på lignende måter som ekte hjerner, altså at de for eksempel bruker lignende minner for å "huske" andre minnner. De prøver også å etterligne hjernen ved å dele opp kognitiv prosessering i hente/velge/aksjon sykluser.

  CLARION

  **noe**


2. *Minnestrukturer (memories) - typer minner og hvordan innholdet representeres*

  ICARUS

  Representerer minne ved hjelp av symboler.

  Har working memory (WM), som består av persepsjon-buffere, blief memory, og korttidsminne.

  Bruker en hierarkisk struktur for langtidsminne.

  CLARION

   Representerer minne symolsk og sybsymbolsk.

   Bruker WM som midlertidig lagring.

   Langtidsminne består av en deklerativ (fastslått) del, og en procedural (genererbar) del.

3. *Kognitiv syklus – fra input til aksjon*

  ICARUS

  Perception -> Perceptual Buffer / Short Term Memory -> Goal Processing -> Skill Retrival and Selection -> Problem Soving and Learning -> Execution

  CLARION

  ???


## Oppgave 2 &mdash; Analogiresonnering

a) *Forklar følgende nøkkelord fra analogy reasoning*
1. *Analogi*
>"Analogy pervades all our thinking, our everyday speech
>and our trivial conclusions as well as artistic ways of
>expression and the highest scientific achievements."
> &mdash; <cite>Polya, How to Solve It, 1945</cite>

2. *Base*

  Base er startobjektet i analogier, altså utsagnet eller objektet man starter med.
3. *Bokstavelig likhet*

  Objekter som har mange like attributter, og som har mange like relasjoner.

4. *Relasjonell likhet*

  Objekter som har mange like relasjoner med andre objekter.


b) *Fyll inn for ???? i tabellen*

Mapping | Antall attributter mappet til målet | Antall relasjoner mappet til målet | Eksempel
--------|-------------------------------------|------------------------------------|---------
Bokstavelig Likhet|Mange|Mange|Solsystemet K5 er som Melkeveien
Analogi|Få|Mange|Et atom er som solsystemet vårt
Abstraksjon|Få|Mange|Atomet er et sentralkraftsystem
Anomall|Få|Få|Kaffe er som solsystemet vårt


c) *Forklar systematisitets-prinsippet («principle of systematicity»)*

  * Dette er at man gjerne gjør analogier basert på relasjoner i stedet for isolerte attributter.

  * Et predikat som passer inn i et system basert på relasjoner er med sannsynlig på bli valgt som måll enn et predikat basert på attributter.

  * Høyere orden relasjoner er mer ønskerlig enn lavere nivå relasjner.


d) *Analogien “En T er som en B” definerer en mapping fra basen B til målet T. Hvilke mapping- regler
foreslår Gentner (Gentner 1983) i sitt rammeverk for analogier?*

  * Retrieval
  * Elaboration
  * Justification
  * Mapping


e) *Figuren nedenfor viser en arkitektur for analogi-resonnering. Redegjør kort for MAC/FAC prinsippet,
og hvordan den virker. Hvordan er MAC/FAC koblet til Retriever og Analogy Engine
modulene?*

<!--![figur](figur.png=250x)-->
<div style="display:flex; justify-content: center; align-items:center;">
<img src="figur.png" alt="drawing" width="200"/>
</div>

  * MAC: Many Are Called, henting av "baser"
  * FAC: Few Are Chosem, velger basen


## Oppgave 3 &mdash; Case-basert resonnering

a) *Hva er hovedprinsippet bak CBR?*

  hovedprinsippet bar Case based reasoning er at man skal gjenbruke tidligere løsninger for å løse nye problemer, man skal også gjenbruke stegene som man brukte ved forrige løsning.

b) *Hvordan kan CBR kobles til menneskers kognisjon? Gi et par eksempler*

  * Humans are not relational planners
  * Human experts are not systems of rules
  * Human memory is story based

  **noe mer**

c) *Hva er en MOP i Dynamic Memory -modellen?*

  MOP: Memory Organisation Packages

  copy paste fra foilene

  "The Dynamic Memory theory suggests that memory is organised
by memory organisation packages (MOPs)
• MOPs organise situations whose activities/situations are similar,
described by a set of scenes
• MOPs have two functions
Ø They hold general knowledge
Ø They organize specific experiences (cases) of that
knowledge
• MOPs store general knowledge (schemas, scripts, norms) with
specific cases attached, in a hierarchical structure
• In understanding, problem solving, etc., the most specific
knowledge is in general the most useful one, hence cases are
favoured if available"

d) *Hva er de viktigste prinsippene for indeksering av et nytt case i casebasen, iflg Dynamic
Memory?*

copy paste

Indexes should have discriminatory power
• Indexes should capture unusual aspects of a situation
(learning from expectation failures)
• Events (cases) are indexed under norms according to
differences from the norm:
Ø a violation of the norm
Ø a specialization of the norm
Ø a generalization of the norm
