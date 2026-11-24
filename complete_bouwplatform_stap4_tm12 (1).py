"""Masterbouwprompt voor uitbreiding van een bestaand bouwplatform."""

bouwprompt = r"""MASTERBOUWOPDRACHT — COMPLETE BOUWPLATFORM (STAP 4 T/M 12)

DOEL
Breid mijn bestaande bouwplatform uit tot een complete, betrouwbare bedrijfsapplicatie voor bouwbedrijven, renovatie, aannemers en vakmensen. Voer wijzigingen uit in het bestaande project. Dit is een implementatieopdracht, geen ontwerp/demo.

ABSOLUUT BELANGRIJK — EERST INSPECTEREN
- Inspecteer de volledige bestaande codebase, architectuur, framework, routes, componenten, database, migraties, authenticatie, gebruikersrollen/rechten, tenantstructuur, styling, navigatie, integrations en tests.
- Behoud alle werkende functionaliteit. Verwijder geen bestaande functies, data, routes, beveiliging of onderdelen zonder aantoonbare noodzaak en mijn expliciete toestemming.
- Hergebruik bestaande tabellen, services, componenten, klanten, medewerkers, materialen, bedrijfsinstellingen en patronen. Maak geen duplicaten.
- Geen demo-data, neprecords, mockimplementaties, placeholderknoppen of niet-werkende functies.
- Als je geen toegang hebt tot een onderdeel, meld dit eerlijk en verzin geen implementatie.
- Werk in het bestaande project en maak geen losstaande nieuwe app.

FASE 0 — ARCHITECTUUR, VEILIGHEID EN DATA
1. Inventariseer bestaande functionaliteit en dependencies en maak een beknopt implementatieplan.
2. Maak wijzigingen in veilige, kleine stappen.
3. Gebruik de bestaande database en authenticatie. Maak schemawijzigingen met migraties, zonder gegevensverlies.
4. Isoleer strikt alle gegevens per bedrijf/tenant op serverniveau. Vertrouw niet op tenant-id's vanuit clientinvoer.
5. Respecteer rollen, permissies en bestaande toegangscontroles voor elke route, actie, API en bestand.
6. Gebruik validatie, veilige queries, CSRF-/XSS-/injectiebescherming waar van toepassing, veilige upload/download, foutafhandeling en logging.
7. Gebruik database-transacties waar nodig en voorkom dubbele verwerking van acties.
8. Gebruik decimalen/precisie geschikte geldtypen voor bedragen; vermijd float-afrondingsfouten.
9. Maak relevante audit trails voor financiële wijzigingen, statusveranderingen en belangrijke acties.
10. Houd de interface consistent met bestaande huisstijl en responsive navigatie.

STAP 4 — CALCULATIES, OFFERTES, PROJECTBEHEER EN PLANNING

A. CALCULATIES
- Maak, bewerk, kopieer, bewaar en archiveer calculaties.
- Bereken materiaalhoeveelheden, eenheden, snijverlies/afvalpercentage, arbeidsuren, tarieven, transport, machines, subcontractors, overige kosten, overhead, marge, korting, btw en totaal.
- Ondersteun prijs per stuk, m2, m3, meter, kg, uur, dag en configureerbare eenheden.
- Bewaar kostprijs, verkoopprijs, marge en rekenregels transparant.
- Materiaalprijzen beheren, historische prijs snapshots bewaren waar nodig.
- Berekeningen herberekenen bij wijziging van inputs en tonen hoe totals zijn opgebouwd.
- Calculatie koppelen aan klant, project/werf en offerte.
- Calculatie met behoud van gegevens omzetten naar offerte.
- Exporteren/printen waar passend.

B. OFFERTES
- Offertes maken, wijzigen, dupliceren, opslaan, archiveren en exporteren naar PDF.
- Koppel aan bestaande klanten, contactpersonen, calculaties en projecten.
- Offertelijnen voor materialen, diensten, arbeidsuren, onderaanneming, transport, hoeveelheden, eenheden en prijzen.
- Subtotalen, kosten, marges, kortingen, btw en eindtotaal.
- Instelbare btw-regels en tarieven voor België en Nederland, inclusief configureerbare uitzonderingen; laat gebruikers de toepasselijkheid controleren en forceer geen onjuiste fiscale behandeling.
- Professionele PDF-layout met bedrijfslogo, bedrijfsgegevens, klant, werfadres, voorwaarden, betalingsvoorwaarden, geldigheidsdatum, detailregels, btw-overzicht en totaalsom.
- Statussen concept, verzonden, bekeken (alleen als dit betrouwbaar gemeten wordt), goedgekeurd, afgewezen, verlopen en omgezet; statusmodel afstemmen op bestaande app.
- Versiebeheer: bewaar historiek en voorkom dat wijzigingen in verzonden offertes ongemerkt de oude versie veranderen.
- Nummering configureerbaar per bedrijf.
- Offerte acceptatie registreren; geen acceptatie simuleren.
- Koppel documenten, notities en opvolgacties.

C. PROJECTBEHEER / WERF
- Projecten en werven aanmaken, wijzigen, archiveren en bekijken.
- Koppel klant, contactpersonen, werfadres, offerte, calculatie, facturen, medewerkers en materialen.
- Projectnummer, omschrijving, status, verantwoordelijke, startdatum, deadline, budget, contractbedrag en projectdoel.
- Taken, subtaken, prioriteit, afhankelijkheden, deadlines, status, verantwoordelijke en opmerkingen.
- Projectvoortgang, budget versus werkelijke kosten, materialen, uren, onderaannemers en facturatie opvolgen.
- Foto's, documenten, plannen, bijlagen, verslagen en notities aan project koppelen.
- Overzicht van projectresultaat, kostprijs, omzet, marge, betaalstatus en budgetoverschrijding.
- Projectrapporten exporteren.
- Archivering zonder gegevensverlies.

D. PLANNING
- Dag-, week-, maand- en agendaweergave, met gebruiksvriendelijke mobiele layout.
- Medewerkers, teams, projecten, werven, taken, afspraken, deadlines en verlof plannen.
- Drag/drop alleen indien ondersteund en veilig; anders werkende bediening via formulieren.
- Filteren op medewerker, team, project, status, klant en periode.
- Conflict detecteren (overlappende inzet, dubbel gepland, relevante beschikbaarheid) en waarschuwingen tonen.
- Achterstallige taken, komende deadlines en gewijzigde planningen signaleren.
- Planning en taakstatus synchroniseren met projectbeheer en urenregistratie.
- Toon tijdzones correct indien relevant; respecteer bedrijfsinstellingen.
- Werk op computer, tablet en smartphone.

STAP 5 — FACTURATIE EN BETALINGEN
- Facturen aanmaken vanuit goedgekeurde offertes, projecten en werkregistraties, zonder gegevens opnieuw te moeten invoeren.
- Facturen handmatig aanmaken, wijzigen volgens geldige regels, dupliceren waar toegestaan, bewaren, versturen via beschikbare integratie of exporteren, en PDF maken.
- Factuurtypes: voorschot, termijn/deelfactuur, eindfactuur, creditnota en correctiedocument, waar wettelijk toegestaan.
- Nummering en serie per bedrijf, configureerbaar en met passende controle op uniekheid en wettelijke regels.
- Factuurregels, aantallen, eenheden, prijs, korting, btw, subtotalen, totaal, betaaltermijn en vervaldatum.
- Verreken voorschotten en eerder gefactureerde bedragen zorgvuldig om dubbel factureren te voorkomen.
- Registratie van betalingen: bedrag, datum, betaalmethode, referentie, notitie en gekoppelde factuur. Ondersteun gedeeltelijke betalingen en meerdere betalingen.
- Bereken resterend saldo, betaalstatus en betalingshistoriek.
- Openstaand, gedeeltelijk betaald, betaald, vervallen en betwist, met passende statusregels.
- Creditnota's en correcties met verwijzing naar oorspronkelijke documenten en controle op bedragen.
- Klantrekening/statement en overzicht van facturen en betalingen.
- Betalingsherinneringen met configureerbare termijnen, templates, preview en logging. Verstuur niet automatisch zonder expliciet ingestelde toestemming en betrouwbare integratie.
- PDF met bedrijfs- en klantgegevens, documentnummer, datums, btw-overzicht, betaalinformatie, IBAN/BIC indien bedrijfsinstelling, betalingsreferentie en wettelijke tekstvelden.
- Bewaak fiscale en wettelijke vereisten van België/Nederland via instelbare instellingen; doe geen claims van wettelijke conformiteit zonder verificatie.
- Maak exports voor boekhouding waar mogelijk, zonder een niet-werkende integratie te claimen.

STAP 6 — CRM / KLANTENBEHEER
- Hergebruik bestaande klantgegevens en klantentabel.
- Klanten, bedrijven, contactpersonen, adressen, telefoons, e-mails, btw-/bedrijfsnummers en voorkeuren beheren.
- Koppel klanten aan offertes, calculaties, projecten, facturen, betalingen, documenten, taken en communicatie.
- Klant historiek en chronologisch overzicht van relevante acties.
- Notities, afspraken, follow-up, status en verantwoordelijke medewerker.
- Zoek, filter, sorteer en archiveer.
- Import/export alleen met validatie, rechten en tenantisolatie; voorkom dubbele records.
- Duplicaten signaleren en veilige samenvoeging aanbieden als dat passend is.

STAP 7 — MATERIAAL, VOORRAAD EN LEVERANCIERS
- Materiaalcatalogus hergebruiken of uitbreiden, geen dubbele catalogus maken.
- Artikelcode, omschrijving, categorie, eenheid, aankoopprijs, verkoopprijs, leverancier, btw, voorraad, minimumvoorraad en eventueel locatie.
- Prijswijzigingen beheren met datum en historiek.
- Voorraad inboeken, uitboeken, corrigeren en reserveren voor projecten.
- Materiaalverbruik per project registreren en koppelen aan calculatie en kosten.
- Leveranciers beheren met contactgegevens, artikel-/prijsinformatie en documenten.
- Bestellingen maken, beheren, registreren, ontvangen en koppelen aan leverancier, project/werf en voorraad.
- Bestelstatussen en levering opvolgen; gedeeltelijke leveringen ondersteunen.
- Waarschuwingen voor lage voorraad en relevante bestelpunten.
- Inventaris- en voorraadrapporten.
- Zorg dat voorraadmutaties controleerbaar zijn en niet ongemerkt dubbel geboekt worden.

STAP 8 — URENREGISTRATIE EN PERSONEEL
- Medewerkers hergebruiken vanuit bestaand systeem; geen dubbele accounts aanmaken.
- Werkuren registreren per medewerker, project, taak, werf en datum.
- Begin-/eindtijd, pauze, totaal, type werk, opmerkingen en optioneel bijlagen.
- Handmatige registratie en mobiele invoer; timer alleen indien betrouwbaar en volledig werkend.
- Urenoverzicht per dag/week/maand en medewerker/project.
- Statussen: concept, ingediend, goedgekeurd, afgewezen, aangepast, volgens bestaande rollen.
- Goedkeuring door bevoegde rollen; audit trail bij wijzigingen.
- Vergelijk begrote uren met werkelijke uren en toon afwijkingen.
- Verlof en afwezigheid alleen integreren indien bestaande rechten/structuur dit ondersteunen.
- Export voor payroll/boekhouding alleen indien export werkelijk geïmplementeerd en getest is; geen loonberekeningen claimen zonder juiste regels.

STAP 9 — DOCUMENTEN, FOTO'S EN WERFDOSSIER
- Centrale documentenbibliotheek, gekoppeld aan klanten, projecten, offertes, calculaties, facturen, medewerkers en leveranciers.
- Upload/download van PDF, afbeeldingen en toegestane bestandsformaten.
- Plannen, contracten, offertes, facturen, foto's, werfverslagen, checklists en bijlagen.
- Beperk bestandstypes, bestandsgrootte en toegang; veilige opslag en toegangscontrole.
- Tenantisolatie op opslag en metadata.
- Documentnaam, categorie, datum, auteur, tags, versie en gekoppeld object.
- Preview waar veilig ondersteund.
- Documentversies waar nodig en verwijdering volgens rechten en beleid.
- Foto's per werf/project ordenen; tijdstempel en beschrijving indien beschikbaar.

STAP 10 — DASHBOARD EN RAPPORTEN
- Dashboard met cijfers die uit echte databasegegevens worden berekend.
- Overzicht omzet, offertes, goedkeuringsratio, facturen, openstaande betalingen, vervallen facturen, projectkosten, marges, budgetten, uren en voorraadwaarschuwingen.
- Filters op datum, bedrijf/tenant, project, medewerker en status, overeenkomstig gebruikersrechten.
- Projectrapporten, klantenrapporten, financiële rapporten, urenrapporten en materiaallijsten.
- Begroot versus werkelijk: kosten, uren, materiaal, inkomsten, marge en voortgang.
- Grafieken en tabellen met drill-down naar brondata.
- Exporteerbare rapporten (PDF/CSV/XLSX indien libraries/architectuur dit ondersteunen).
- Geen fake metrics; lege states duidelijk weergeven en totals controleren.

STAP 11 — AUTOMATISERING EN NOTIFICATIES
- Configureerbare waarschuwingen voor deadlines, achterstallige taken, offerte-opvolging, factuurverval, lage voorraad, planningsconflicten, budgetoverschrijding en projectstatus.
- Notificaties in app; e-mail/push alleen als integratie daadwerkelijk beschikbaar en ingesteld is.
- Gebruikers kunnen relevante notificatievoorkeuren beheren volgens rechten.
- Templates voor e-mail/berichten met preview en variabelen.
- Log verstuurde meldingen, status en eventuele fouten.
- Configureerbare automatiseringen; gebruikers kunnen ze uitschakelen.
- Geen onbevestigde automatische verzending, externe communicatie, financiële transacties of onomkeerbare acties.
- Deduplicatie en veilige retries om dubbele berichten of mutaties te voorkomen.

STAP 12 — BEDRIJFSINSTELLINGEN EN ADMINISTRATIE
- Bedrijfsprofiel, logo, adres, contactgegevens, btw-/registratienummer, IBAN/BIC en relevante documentgegevens.
- Configureerbare documentnummering, valuta, tijdzone, datum-/getalnotatie en taal.
- Belgische en Nederlandse btw-instellingen met configureerbare tarieven, regels en uitzonderingen; fiscale keuzes moeten controleerbaar zijn en door gebruiker/accountant kunnen worden ingesteld.
- Offerte-, factuur-, betalings-, project- en e-mailtemplates.
- Gebruikers, teams, rollen en permissies via bestaande authenticatie/rollenstructuur.
- Bedrijfsspecifieke instellingen strikt geïsoleerd.
- Beveiligingsinstellingen en audit logs toegankelijk volgens bevoegdheden.
- Import/export, back-up en herstel alleen via veilige, werkende processen.
- Beheer van integraties, API keys en webhooks met veilige secret storage indien architectuur dit ondersteunt.

STAP 13 — INTEGRATIE, NAVIGATIE EN UX
- Koppel alle modules via bestaande records en relaties; vermijd kopieën van dezelfde data.
- Maak logische navigatie en dashboards passend bij bestaande huisstijl.
- Elk scherm moet realistische loading-, empty-, success- en error-states bevatten.
- Alle formulieren moeten validatie, toegankelijkheid en duidelijke feedback hebben.
- Alle knoppen, menu's, filters, acties en exports moeten daadwerkelijk functioneren.
- Responsive voor desktop, tablet en mobiel.
- Zoek en filter waar gebruikers grote datasets beheren.
- Gebruik paginering/performante queries bij grote gegevensvolumes.
- Behoud bestaande routes en functies; voorkom breaking changes.
- Zorg voor consistente links tussen klant, offerte, calculatie, project, taak, planning, materiaal, uren, factuur, betaling en documenten.

STAP 14 — TESTEN EN OPLEVEREN
Voer tests uit, waar de omgeving dit ondersteunt:
1. Migraties: bestaande gegevens blijven behouden; migraties zijn herhaalbaar/veilig waar de tooling dit ondersteunt.
2. Tenant-isolatie: bedrijf A kan data, documenten en API-acties van bedrijf B niet lezen of wijzigen.
3. Autorisatie: gebruikersrollen kunnen uitsluitend toegestane acties uitvoeren.
4. Calculaties: aantallen, eenheden, kortingen, marge, btw en totals; decimalen en afronding.
5. Offerteworkflow: create/edit/duplicate/version/status/PDF, en omzetting naar project/factuur waar ondersteund.
6. Facturatie: voorschot, deelfactuur, eindfactuur, creditnota, gedeeltelijke betaling, saldo, vervaldatum en herinneringsflow.
7. Projecten: taak, deadline, budget, kosten, uren, materialen en documenten.
8. Planning: conflict detectie, filters, deadlines, responsiviteit en correcte koppelingen.
9. Voorraad: mutaties, projectverbruik, bestellingen en ontvangst.
10. Uren: registratie, goedkeuring, correcties en rapportage.
11. Uploads: toegangscontrole, bestandstype, grootte, tenantisolatie en download.
12. Dashboard: metrics overeenkomen met brondata en permissies.
13. Automatisering: triggers, deduplicatie, voorkeuren en logging.
14. UX: formulieren, navigatie, loading/empty/error states en mobiel.
15. Registreer en herstel gevonden fouten; voer regressietests uit.

IMPLEMENTATIEVOLGORDE
- Eerst inspectie en plan.
- Fase 1: schema, relaties, tenantisolatie, autorisaties en basiscalculaties.
- Fase 2: offertes en PDF/versionering.
- Fase 3: projecten, taken, planning en uren.
- Fase 4: facturatie, betalingen, creditnota's en herinneringen.
- Fase 5: CRM, voorraad, leveranciers en documenten.
- Fase 6: dashboard, rapporten, notificaties en instellingen.
- Fase 7: integratietests, regressietests, bugs en responsive UX.
Pas deze volgorde aan indien bestaande architectuur dit noodzakelijk maakt; documenteer waarom.

EINDRAPPORT
- Geef beknopt overzicht van de bestaande architectuur die is hergebruikt.
- Geef de wijzigingen en migraties weer.
- Maak een lijst van modules/functies die daadwerkelijk geïmplementeerd zijn.
- Maak een lijst van tests die daadwerkelijk zijn uitgevoerd met resultaten.
- Meld eerlijk wat niet af is, wat geblokkeerd is, welke integraties niet verbonden zijn en wat handmatig moet gebeuren.
- Vermeld geen functie als werkend of getest als dat niet aantoonbaar het geval is.
- Geen demo, mockdata, fake buttons of lege claims.
- Begin direct met inspecteren en implementeren in het bestaande project.
"""

if __name__ == "__main__":
    print(bouwprompt)
