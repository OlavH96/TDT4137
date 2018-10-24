# TDT4137 - Øving 4 - Olav Reppe Husby

- [ ] 1.
  - [x] a)
  - [ ] b)
    - [x] 1
    - [ ] 2
    - [ ] 3
    - [ ] 4

- [ ] 2.
  - [ ] a)
  - [ ] b)
  - [ ] c)
  - [ ] d)
  - [ ] e)
- [x] 3.
  - [x] a)
  - [x] b)
  - [x] c)
  - [x] d)



## Oppgave 1 &mdash; Icarus og CLARION

a) *Beskriv kort hovedmodulene i de kognitive arkitekturene ICARUS og CLARION*


**ICARUS**

ICARUS er en kognitiv arkitektur som fokuserer på fysiske agenter i en fysisk verden. ICARUS lenker kongnisjon til persepsjon og handlinger. Hovedmodulene i ICARUS er minne (kort- og langtids-) som bruker symbolske strukturer, og kognitiv prosessering (hente, velge, handling).

**CLARION**

ICARUS er en kognitiv arkitektur som fokuserer på en dualitet med tanke på representasjon av data, disse er eksplisitt og implisitt kunnskap. CLARION består av hovedmodulene ACS (Action-Centered Subsystem), NACS (Non Action-Centered Subsystem), MS (Motivational Subsystem), og MCS (Meta-Cognitive Subsystem).


b) *Gjør en sammenligning mellom de to arkitekturene med hensyn på*
1. *Underliggende filosofi og motivering*

  **ICARUS**

  Den underliggende filosofien i Icarus er at man bør modellere et kognitivt system basert på realiteten, altså den fysiske verden.

  Icarus mener at langtidsminne og korttidsminne bør være forskjellige konsepter i et kognitivt system, siden de er forskjellige i virkelige hjerner. Icarus prøver også å bruke disse minnene på lignende måter som ekte hjerner, altså at de for eksempel bruker lignende minner for å "huske" andre minnner. De prøver også å etterligne hjernen ved å dele opp kognitiv prosessering i hente/velge/aksjon sykluser.

  Icarus prøver å skape et system som modellerer høyere nivå kognisjon hos mennesker, samtidig som det prøver å være konsistent med pykologi, prøver å framvise så mange menneskelige kognitive funksjoner som mulig, og skal kunne støtte intelligente agenter i mange forskjellige situasjoner.

  **CLARION**

  CLARION prøver å lage et system for menneskelig kognisjon med fokus på kognisjon, motivasjon, miljø interaksjonen. I CLARION prøver de å oppnå flere typer læring, slik som selvstendig-, top-down-, og bottom-up-læring. På denne måten håper de å etterligne menneskets kognisjon på best mulig måte. CLARION prøver å gjøre dette ved å dele opp systemet i subsystemene nevnt i forrige oppgave.


2. *Minnestrukturer (memories) - typer minner og hvordan innholdet representeres*

  **ICARUS**

  ICARUS velger å representere minne ved hjelp av symboler. Systemet har working memory (WM), som består av persepsjon-buffere, blief memory, og korttidsminne.
  ICARUS bruker også en hierarkisk struktur for langtidsminne, altså at minner bygger på hverandre, og at lignende minner henger sammen. ICARUS har to typer langtidsminne, et deklerativt minne som brukes for konsepter, og et procedural minne som brukes for kunnskap.

  **CLARION**

  På lik linje med ICARUS, velger også CLARION å representere minnet symolsk, men CLARION kan også lagre minne subsymbolsk.

  CLARION har Working Memory slik som ICARUS, men velger å bruke denne kun som en midlertidig lagring for informasjon.

  Langtidsminne består av en deklerativ (fastslått) del, og en procedural (genererbar) del. Den deklerative delen representerer den høyere-nivå kunnskapen i CLARION, altså konsepter og fakta. Den genererbare delen brukes på lavere nivå, og brukes derfor for å generere mer detaljebasert kunnskap basert på høyere nivå kunnskap når dette trengs.

3. *Kognitiv syklus – fra input til aksjon*

  **ICARUS**

  <div style="display:flex; justify-content: center; align-items:center;">
  <img src="ICARUS_Process.png" alt="ICARUS Process" width="400"/>
  </div>

  ICARUS har en fast syklus for hvordan input håndteres. Først sanser man noe input (Perception), så bruker man korttidsminne eller buffer for å lagre dette, og bruker konseptuelt minne for å utlede relevant kunnskap om denne inputen. Neste fase er "skill execution", der man legger problemet i minne og bruker en iterativ problemløsningsfase til å finne ut hvilken ferdighet man skal bruke for å reagere på problemet, dette gjøres ved å prøve å anvende problemet på flere forskjellige kjente ferdigheter iterativt helt til man finner en ferdighet som matcher problemet, denne løsningen vil lagres for senere bruk, altså har man lært noe om denne spesfikke problemstillingen. Ut ifra den handlingen som ble valgt kan man så legge denne i buffer og utføre denne handlingen mot miljøet. Så kan syklusen fortsette.   

  **CLARION**

  CLARION fungerer nesten som et neuralt nettverk i måten det løser problemer;
  ???

## Oppgave 2 &mdash; Analogiresonnering

a) *Forklar følgende nøkkelord fra analogy reasoning*
1. *Analogi*
>"Analogy pervades all our thinking, our everyday speech
>and our trivial conclusions as well as artistic ways of
>expression and the highest scientific achievements."
> &mdash; <cite>Polya, How to Solve It, 1945</cite>

En analogi handler om å se likheter i objekter på noen måter selv om objektene er ulike på andre måter, for så å sammenligne disse likhetene.
2. *Base*

  Base er startobjektet i analogier, altså utsagnet eller objektet man starter med.
3. *Bokstavelig likhet*

  Objekter som har mange like attributter, og som har mange like relasjoner.

4. *Relasjonell likhet*

  Objekter som har mange like relasjoner med andre objekter.

b) *Fyll inn for ???? i tabellen*

Mapping  | Antall attributter mappet til målet | Antall relasjoner mappet til målet | Eksempel
--------|-------------------------------------|------------------------------------|---------
Bokstavelig Likhet|Mange|Mange|Solsystemet K5 er som Melkeveien
Analogi|Få|Mange|Et atom er som solsystemet vårt
Abstraksjon|Få|Mange|Atomet er et sentralkraftsystem
Anomali|Få|Få|Kaffe er som solsystemet vårt


c) *Forklar systematisitets-prinsippet («principle of systematicity»)*

  * Dette er at man gjerne gjør analogier basert på relasjoner i stedet for isolerte attributter.

  * Et predikat som passer inn i et system basert på relasjoner er med sannsynlig på bli valgt som mål enn et predikat basert på attributter.

  * Høyere orden relasjoner er mer ønskerlig enn lavere nivå relasjner.


d) *Analogien “En T er som en B” definerer en mapping fra basen B til målet T. Hvilke mapping- regler
foreslår Gentner (Gentner 1983) i sitt rammeverk for analogier?*

  * Retrieval

  I denne regelen henter velger man hva som er base i analogien, og hva som er målet.
  * Elaboration

  I denne fasen utdyper man om objektene, altså man finner attributter og egenskaper i disse objektene.

  * Mapping

  I denne fasen bruker man systematisitets-prinsippet for å finne likheter i objektene basert på deres relasjoner hovedsakelig. Siden man bruker systematisitets-prinsippet finner man gjerne høyere nivå relasjoner i objektene som lettere lar seg overføre til andre objekter.
  * Justification

  I denne fasen prøver man å matche basen med målet ved å se på begge objektene sine relasjoner og bruker dette som basis for å sjekke om objektene er like på noen måte.

e) *Figuren nedenfor viser en arkitektur for analogi-resonnering. Redegjør kort for MAC/FAC prinsippet,
og hvordan den virker. Hvordan er MAC/FAC koblet til Retriever og Analogy Engine
modulene?*

<!--![figur](figur.png=250x)-->
<div style="display:flex; justify-content: center; align-items:center;">
<img src="figur.png" alt="drawing" width="200"/>
</div>

  * MAC: Many Are Called, henting av "baser"

  Denne fasen går ut på at man henter ut mange forskjellige mulige baser og bruker bokstavelig likhet for å sjekke om objektene har noen likheter.

  * FAC: Few Are Chosen, velger få baser

  Denne fasen prøver å skape en analogi mellom objektene ved å fokusere på strukturell mapping, altså om objektene har mange likheter eller ikke. De objektene med flest likheter blir dermed valgt som mål.

  I forhold til denne figuren er MAC en del av Retriever, altså modulen som henter ut baser, denne vil hente ut mange forskjellige potensielle baser som sendes vidre i systemet.

  FAC er del av Analogy-Engine i dette tilfellet; Analogy-Engine vil bruke FAC prinsippet til å velge få mål objekter basert på strukturell mapping.

## Oppgave 3 &mdash; Case-basert resonnering

a) *Hva er hovedprinsippet bak CBR?*

  Hovedprinsippet bar case based reasoning er at man skal gjenbruke tidligere løsninger for å løse nye problemer, og at man skal gjenbruke stegene som man brukte ved forrige løsning.

b) *Hvordan kan CBR kobles til menneskers kognisjon? Gi et par eksempler*

  CBR kan kobles til menneskelig kognisjon fordi mennesker bruker tidligere erfaring og løsninger nå de skal løse et lignende problem.

  Eksempler:
  - En lege som behandler en pasient basert på tidligere erfaring med lignende symptomer.
  - En matematiker som løser en ligning ved å bruke metoder som de har brukt tidligere på lignende problemer.
  - En programmerer som løser et problemer ved å anvende en kunnskap om lignende problemer. For eksempel kan man bruke kunnskap om hvordan man reverserer en liste til å finne ut en algoritme for å reversere et ord.

c) *Hva er en MOP i Dynamic Memory -modellen?*

  MOP: Memory Organisation Packages

  MOP er er en minnestruktur der minner organiseres etter likhet. MOP er generelle enheter som gjerne inneholder generell kunnskap, og spesifikke erfaringer med den kunnskapen. De gjør det slik fordi det menes at det er slik mennesker organiserer minner, ved at man har generell kunnskap om et tema, så har man eventuelt spesifikk kunnskap om temaet via erfaring.

d) *Hva er de viktigste prinsippene for indeksering av et nytt case i casebasen, iflg Dynamic
Memory?*

  De viktigste prinsippene for indeksering av et nytt case er at man bør lagre uventete aspekter i en situasjon, og at man lagrer handlinger basert på forskjeller fra den etablerte kunnskapen, altså om kunnskapen bryter normen, spesialiserer normen, eller generaliserer normen. Altså hvis man opplever en situasjon som er relatert til tidligere kunnskap, vil man ikke lære noe nytt hvis man opplever den samme situasjonen som man har opplevd før, men man vil lære noe nytt hvis situasjonen er forskjellig fra det man har lært før, for eksempel at man lærer noe som ikke passer inn i eksisterende kunnskap, eller at det passer inn, men er en mer spesialisert situasjon, eller en mer generell situasjon.
