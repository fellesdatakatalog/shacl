# Reasonable Ontology Templates (OTTR)

## Filer
- data-concept.xlsx
- data-organization.xlsx
- data-xlnote.xlsx
- out.ttl
- skos-tpl.ttl

### Instansdata
Data beskrives i Excel med tabOTTR syntaks for malbeskrivelse(r).

La oss ta `vcard:Organization` til eksempel fra data-organization.xlsx

| #OTTR | template                | o-skosno:Organization |
|-------|-------------------------|-----------------------|
| 1     | 2                       | 3                     |
| iri   | text+                   | auto                  |
| URI   | NAME                    | EMAIL                 |
| ex:Tolletaten | Tolletaten@@nb | Norwegian Customs Authority@@en | postmottak@toll.no |

På toppen av hvert Excel-dokument er det deklarert ei liste med prefikser (som er strøket i dette markdown-eksempelet), så følger tabellen vi ser over.

- Første rad presiserer hvilken mal (OTTR template) vi skal instansiere data mot.
- Andre rad er nummer på parameter.
- Tredje rad sier noe om datatypen vi forventer dukker opp i cellen.
- Fjerde rad er navnet på kolonnen, og
- Restrerende rader er selve dataene.


### Hvordan kjøre på Lutra
`java -jar .\lutra.jar -l .\skos-tpl.ttl -L stottr -I tabottr -f .\data.xlsx -o out.ttl`

[Siste oppdaterte publikasjon av Lutra finnes her.](https://gitlab.com/ottr/lutra/lutra)
