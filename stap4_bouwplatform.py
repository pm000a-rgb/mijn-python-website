# -*- coding: utf-8 -*-
"""Bouwprompt voor STAP 4 van een bestaand bouwplatform."""

bouwprompt = r'''STAP 4 — BOUW DE 4 LAATSTE MODULES VAN MIJN BESTAANDE BOUWPLATFORM.

BELANGRIJK:
Inspecteer eerst mijn bestaande applicatie. Behoud alle werkende functies, database, gebruikersrollen, beveiliging, huisstijl en navigatie. Bouw voort op wat al bestaat. Maak niets dubbel en verwijder niets dat werkt.

BOUW DE VOLGENDE MODULES:

1. OFFERTES
- Offertes maken, opslaan, wijzigen en dupliceren.
- Klanten, werkzaamheden, materialen, hoeveelheden en prijzen toevoegen.
- Arbeidskosten, kortingen, marges en btw berekenen.
- PDF-offertes genereren.
- Offertestatussen en versies beheren.
- Offertes koppelen aan klanten en projecten.

2. CALCULATIES
- Materiaalverbruik, arbeidsuren en totale kosten berekenen.
- Transport, overige kosten, winstmarges en btw toevoegen.
- Berekeningen automatisch uitvoeren en controleerbaar houden.
- Calculaties omzetten naar offertes zonder gegevens opnieuw in te voeren.
- Materiaalprijzen handmatig beheren.

3. PROJECTBEHEER
- Projecten en werven aanmaken en beheren.
- Klanten, budgetten, deadlines en medewerkers koppelen.
- Taken, voortgang, werkuren, foto's en documenten registreren.
- Projectkosten en budgetten opvolgen.
- Projectrapporten genereren.

4. PLANNING
- Dag-, week- en maandplanning.
- Kalender met taken, deadlines en projectstatussen.
- Medewerkers aan projecten en taken toewijzen.
- Achterstallige taken en planningsconflicten signaleren.
- Planning geschikt maken voor computer, tablet en smartphone.

TECHNISCHE REGELS
- Gebruik de bestaande database en authenticatie.
- Sla alle gegevens echt op.
- Scheid gegevens strikt per bouwbedrijf (tenant).
- Respecteer bestaande gebruikersrollen en rechten.
- Koppel de vier modules correct aan elkaar.
- Gebruik bestaande klanten, medewerkers en materialen.
- Bereken bedragen en btw betrouwbaar, met instelbare Belgische en Nederlandse btw-regels.
- Maak alle knoppen, formulieren en PDF-export functioneel.
- Valideer invoer en voorkom dat gebruikers gegevens van andere bedrijven kunnen lezen of wijzigen.
- Gebruik database-transacties en passende foutafhandeling.
- Bewaar audit-/versiegegevens waar nodig.
- Gebruik decimalen (geen floating-point afrondingsfouten) voor geldbedragen.
- Maak geen demo-, mock- of nepgegevens aan en laat geen placeholder-knoppen achter.

WERKWIJZE
1. Inspecteer eerst de codebase, database, architectuur, routes, componenten, authenticatie, rollen, stijl en bestaande functionaliteit.
2. Rapporteer kort wat al aanwezig is en welke onderdelen hergebruikt kunnen worden.
3. Maak een plan en voer wijzigingen uit in kleine, veilige stappen.
4. Bouw eerst databaseverbindingen/schema-aanpassingen en calculaties.
5. Bouw daarna offertes, inclusief PDF-export, statussen en versiebeheer.
6. Bouw projectbeheer en koppel dit aan klanten, calculaties, offertes, materialen, taken en werkuren.
7. Bouw planning en koppel deze aan projecten, taken, deadlines en medewerkers.
8. Gebruik migraties die veilig zijn en bestaande gegevens niet vernietigen. Wijzig uitsluitend wat noodzakelijk is.
9. Test belangrijke workflows, rechten, tenant-isolatie, berekeningen, btw, PDF-export, responsiviteit en foutscenario's.
10. Herstel fouten die tijdens het testen worden gevonden.

LEVERING
- Lever de implementatie in mijn bestaande project, niet als losse demo.
- Geef geen nepresultaten en claim geen tests die niet zijn uitgevoerd.
- Maak alle benodigde database-migraties en documenteer deze.
- Meld eerlijk welke onderdelen daadwerkelijk werken, welke tests zijn uitgevoerd en wat nog ontbreekt.
- Begin direct met STAP 4 in mijn bestaande project.
'''

if __name__ == "__main__":
    print(bouwprompt)
