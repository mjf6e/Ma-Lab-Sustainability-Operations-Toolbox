#!/usr/bin/env python3
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

DATA = []

def add(name, type_, talk, role="", extra=None, links=None, emails=None, meta=None, topics=""):
    DATA.append({
        "name": name, "type": type_, "role": role, "talk": talk,
        "extra": extra, "links": links or [], "emails": emails or [],
        "meta": meta, "topics": topics
    })

# ---------------- INVENTORY & ORDERING ----------------
add("Shared Consumables Policy", "inv",
    "Lab personnel prioritize sharing consumables, reagents, and chemicals using the Quartzy inventory management system to avoid duplicate purchases.",
    role="Inventory & Resource Sharing", topics="quartzy consumables reagents chemicals shared duplicate purchases")

add("Shared Equipment Use", "inv",
    "Many items in the lab's inventory are designated for general lab use &mdash; check before assuming you need your own.",
    role="Inventory & Resource Sharing", topics="shared equipment general use")

add("Surplus Resource Management", "inv",
    "Surplus equipment, consumables, and chemicals are repaired, donated, or sent to refurbishment organizations or other end-users (MERCI, ROSE, ReUSE) rather than discarded.",
    role="Inventory & Resource Sharing", topics="surplus donate merci rose reuse refurbishment")

add("Inventory Check Before Orders", "inv",
    "Existing inventory in Quartzy must be checked before placing new orders, to prevent excessive or redundant purchasing.",
    role="Inventory & Resource Sharing", topics="quartzy inventory check before orders redundant")

add("Order Consolidation Policy", "inv",
    "Orders are consolidated into larger shipments whenever possible, reducing the environmental impact of transportation.",
    role="Inventory & Resource Sharing", topics="order consolidation shipments transportation")

add("Lab Water Use and Quality", "inv",
    "Members are trained on water-saving strategies and choosing among tap, deionized, distilled, and reverse-osmosis water. Everyone selects the water quality fit for purpose, avoiding unnecessary over-purification.",
    role="Inventory & Resource Sharing", topics="water use quality deionized distilled reverse osmosis")

add("Structured Laboratory Ordering Process", "inv",
    "A six-step process: (1) methodology development & supply list, (2) submission to ordering personnel via Quartzy, (3) inventory check in Quartzy, (4) redundancy & expiry review using FIFO, (5) order consolidation across researchers, (6) order placement only after confirming necessity.",
    role="Ordering Process",
    extra="Multiple verification steps prevent unnecessary purchases and duplicate ordering of materials already in stock.",
    topics="ordering process six steps methodology quartzy redundancy expiry consolidation placement")

add("Ongoing Inventory Management", "inv",
    "Regular audits confirm Quartzy records match physical inventory; usage tracking refines future ordering quantities and prevents overstocking; proactive communication lets researchers flag upcoming needs and changed plans early.",
    role="Ordering Process", topics="audits usage tracking proactive communication overstocking")

add("Bulk Ordering Benefits", "inv",
    "Reduces packaging waste, decreases carbon emissions from frequent deliveries, qualifies for volume discounts, lowers per-unit shipping costs, and minimizes administrative processing time.",
    role="Ordering Process", topics="bulk ordering packaging waste carbon emissions volume discounts shipping")

add("Expiration Management", "inv",
    "Implements FIFO usage, regularly reviews stock for approaching expiration dates, redistributes at-risk items to high-usage applications, and reduces hazardous waste disposal requirements.",
    role="Ordering Process", topics="expiration management fifo redistribute hazardous waste")

# ---------------- WASTE MANAGEMENT ----------------
add("The Waste Hierarchy", "waste",
    "Prevent &rarr; Reduce &rarr; Reuse &rarr; Recycle, in order of preference. No activity should begin without a plan for its waste, and recycling is treated as the last resort before disposal.",
    role="Waste Hierarchy Training", topics="waste hierarchy prevent reduce reuse recycle framework")

add("Safe Waste Disposal Guidelines", "waste",
    "Lab personnel adhere to guidelines for the safe disposal of liquid waste, separating aqueous, non-aqueous, and halogenated (chlorinated) waste when possible.",
    role="Waste Management", topics="liquid waste disposal aqueous non-aqueous halogenated chlorinated")

add("Minimizing Water-Based Vacuums", "waste",
    "Labs do not use water-vacuum aspirators or other water-based methods to create a vacuum.",
    role="Waste Management", topics="water vacuum aspirator")

add("Prevent: Digital Data Collection", "waste",
    "Using digital tools for data collection and analysis instead of paper is the highest priority in the hierarchy &mdash; it stops the waste from being generated at all.",
    role="Waste Hierarchy Training", topics="prevent digital data collection paper waste")

add("Reduce: Order Only What's Needed", "waste",
    "Order only the quantities of materials actually needed for an experiment to minimize excess waste.",
    role="Waste Hierarchy Training", topics="reduce order quantities excess waste")

add("Reuse: Glassware Over Single-Use", "waste",
    "Promote reusable lab items &mdash; glassware and containers &mdash; in place of single-use plastics.",
    role="Waste Hierarchy Training", topics="reuse glassware containers single-use plastics")

add("Recycle: Proper Segregation", "waste",
    "Educate on proper segregation of recyclable materials and the lab's specific recycling protocols.",
    role="Waste Hierarchy Training", topics="recycle segregation protocols")

add("Waste Hierarchy Hands-On Activities", "waste",
    "Waste Audit (1 hour): bins, scales, gloves, audit forms &mdash; produces baseline waste data. Reuse Challenge (1 week): identify single-use items to replace. Recycling Workshop (15 min): training on proper segregation per UVA regulations.",
    role="Waste Hierarchy Training", topics="waste audit reuse challenge recycling workshop hands-on activities")

# ---------------- ENERGY EFFICIENCY ----------------
add("Turn Off Equipment When Not in Use", "energy",
    "Ensure non-essential equipment is turned off when not actively being used; establish an end-of-day power-down routine; use power strips with switches; post reminders at workstations.",
    role="Energy Action Plan", topics="turn off equipment power down routine power strips reminders")

add("Purchase Energy-Efficient Equipment", "energy",
    "Prioritize Energy Star or similarly certified models, weigh long-term energy cost savings when budgeting, replace outdated equipment, and choose electronics certified to EPEAT or TCO standards.",
    role="Energy Action Plan", topics="energy star epeat tco certified efficient equipment purchasing")

add("Utilize Shared Equipment", "energy",
    "Coordinate with other research groups to share large equipment (freezers, centrifuges, spectrometers), set up shared scheduling systems, and consolidate experiments to avoid redundant equipment use.",
    role="Energy Action Plan", topics="shared equipment coordination scheduling consolidate experiments")

add("Optimize Freezer & Refrigerator Usage", "energy",
    "Consolidate samples to reduce the number of units needed, defrost regularly, set freezers to &minus;70&deg;C instead of &minus;80&deg;C unless absolutely necessary, and keep door seals well maintained.",
    role="Energy Action Plan", topics="freezer refrigerator -70 -80 defrost seals")

add("Optimize Lighting", "energy",
    "Turn off lights in unused rooms and storage areas, replace old lighting with LEDs, and install motion-sensor or timer-based lighting in low-traffic areas.",
    role="Energy Action Plan", topics="lighting led motion sensor timer")

add("Reduce Plug Loads", "energy",
    "Minimize plug load by consolidating equipment and removing redundant devices, use energy-saving settings on computers and monitors, and unplug chargers and small equipment to avoid phantom loads.",
    role="Energy Action Plan", topics="plug loads phantom loads energy saving settings")

add("Cold Trap & Vacuum Pump Use", "energy",
    "A cold trap must be used in line before vacuum pumps to prevent volatiles from entering the pump, and vacuum pumps must be turned off when not in use.",
    role="Energy & Environmental Practices", topics="cold trap vacuum pump volatiles")

add("Incubators & Biosafety Cabinets", "energy",
    "Incubators and biosafety cabinets must be turned off completely when not in use for extended periods.",
    role="Energy & Environmental Practices", topics="incubators biosafety cabinets off extended periods")

add("Cloud-First Data Storage Policy", "energy",
    "Storing data and files in the cloud rather than on local networks or computers reduces energy usage and improves accessibility. Each UVA OneDrive account permits up to 5 TB of storage.",
    role="Energy & Environmental Practices", topics="cloud storage onedrive 5tb energy usage")

add("Monitor & Track Energy Usage", "energy",
    "Install energy meters for real-time monitoring, conduct periodic energy audits, and use audit data to assess impact and make adjustments. Maintenance: service equipment regularly, replace worn components as needed, clean air filters monthly.",
    role="Energy Action Plan", topics="energy meters audits monitoring maintenance air filters")

add("Collaborate with Building Management", "energy",
    "Work with facility management to optimize HVAC for the lab's needs, request energy-efficient infrastructure like programmable thermostats, and advocate for building-wide sustainability initiatives.",
    role="Energy Action Plan", topics="hvac building management thermostats sustainability initiatives")

# ---------------- FIFO ----------------
add("What FIFO Means", "fifo",
    "First In, First Out: using the oldest unexpired materials first. It prevents waste by using materials before they expire, ensures accurate results by avoiding degraded reagents, and reduces cost from discarded materials.",
    role="FIFO Training", topics="fifo first in first out definition importance")

add("Labeling and Organization", "fifo",
    "All reagents, chemicals, and supplies are clearly labeled with date of receipt and expiration date. Older items sit at the front of storage, newer items at the back.",
    role="FIFO Training", topics="labeling organization date receipt expiration")

add("Inventory Checks for FIFO", "fifo",
    "Regular inventory checks confirm materials are being used in the correct order; expired items are removed promptly to avoid accidental use.",
    role="FIFO Training", topics="inventory checks expired items removal")

add("FIFO Storage Practices", "fifo",
    "Dedicated storage areas for different material types (chemicals, biological reagents) make FIFO easier to implement, and proper storage conditions extend shelf life.",
    role="FIFO Training", topics="storage practices dedicated areas shelf life")

add("FIFO Hands-On Activities", "fifo",
    "Inventory Audit: identify materials nearing expiration and reorganize. Labeling Exercise: practice color-coded date labeling. Scenario-Based Training: decide which materials to use based on FIFO.",
    role="FIFO Training", topics="inventory audit labeling exercise scenario training")

# ---------------- GREEN CHEMISTRY ----------------
add("The 12 Principles, Applied to Research Labs", "chem",
    "Green chemistry designs processes to reduce or eliminate hazardous substances. Key principles for the bench: waste prevention, atom economy, designing safer chemicals, and less hazardous chemical syntheses.",
    role="Green Chemistry Training", topics="12 principles green chemistry hazardous substances atom economy")

add("Waste Prevention (Green Chemistry)", "chem",
    "Plan experiments to minimize waste generation by scaling reactions appropriately.",
    role="Green Chemistry Training", topics="waste prevention scaling reactions")

add("Energy Efficiency (Green Chemistry)", "chem",
    "Use energy-efficient equipment and conduct reactions at ambient conditions whenever possible.",
    role="Green Chemistry Training", topics="ambient conditions energy efficient reactions")

add("Safer Solvents", "chem",
    "Replace hazardous solvents with greener alternatives, such as water or ethanol.",
    role="Green Chemistry Training", topics="safer solvents water ethanol hazardous")

add("Catalysis", "chem",
    "Incorporate catalysts to improve reaction efficiency and reduce waste.",
    role="Green Chemistry Training", topics="catalysis catalysts reaction efficiency")

add("Real-Time Monitoring (Green Chemistry)", "chem",
    "Use analytical tools to monitor reactions and prevent the formation of hazardous byproducts.",
    role="Green Chemistry Training", topics="real-time monitoring analytical tools byproducts")

add("Analytical Chemistry Adaptations", "chem",
    "Minimize sample sizes and waste in analytical methods, use non-toxic reagents and solvents, and optimize methods to reduce energy consumption and improve efficiency.",
    role="Green Chemistry Training", topics="analytical chemistry sample sizes non-toxic reagents optimize methods")

add("Green Chemistry Hands-On Activities", "chem",
    "Green Experiment Design: redesign an experiment for waste reduction, renewable feedstocks, and atom economy. Solvent Replacement Exercise: research greener alternatives. Energy Audit: identify consumption-reduction opportunities.",
    role="Green Chemistry Training", topics="green experiment design solvent replacement energy audit")

add("What Makes Chemistry Green (EPA)", "chem",
    "Per the EPA's definition, green chemistry: prevents pollution at the molecular level; applies as a philosophy across all of chemistry rather than one discipline; applies innovative solutions to real-world environmental problems; results in source reduction by preventing pollution generation; reduces negative impacts on human health and the environment; lessens or eliminates hazards from existing products and processes; and designs products and processes to reduce their intrinsic hazards.",
    role="Green Chemistry Training",
    links=[{"note":"EPA — Basics of Green Chemistry","url":"https://www.epa.gov/greenchemistry/basics-green-chemistry"}],
    topics="epa definition green chemistry pollution prevention source reduction intrinsic hazards")

add("Green Chemistry Tools & Alternatives", "chem",
    "Two reference tools the lab points to when picking a greener chemical or process: MIT's Green Chemical Alternatives Wizard, which suggests less-hazardous substitutes for common lab solvents and reagents, and DOZN, a quantitative scoring tool that rates the relative greenness of a chemical, synthetic route, or process against the 12 Principles.",
    role="Green Chemistry Training",
    links=[{"note":"MIT Green Chemistry Alternatives (EHS)","url":"https://ehs-apps.mit.edu/site/environmental-stewardship/green-chemistry"},
           {"note":"DOZN Quantitative Green Chemistry Evaluator","url":"https://www.sigmaaldrich.com/US/en/services/software-and-digital-platforms/dozn-tool"}],
    topics="mit green alternatives wizard dozn evaluator solvent substitution scoring tool")

add("Green Chemistry Champion", "chem",
    "A designated lab member oversees the implementation of sustainable practices, with regular protocol reviews and an open feedback channel for new ideas.",
    role="Green Chemistry Training", topics="green chemistry champion protocol review feedback")

# ---------------- ANIMAL RESEARCH ----------------
add("IVC Rack Usage Policy", "animal",
    "The Individual Ventilated Cages (IVC) rack must be unplugged when not in use, reducing electricity consumption, extending equipment lifespan, lowering operational costs, and minimizing carbon footprint.",
    role="Animal Research Policy", topics="ivc rack unplugged energy carbon footprint")

add("Disinfectant Minimization Policy", "animal",
    "The vivarium calculates exact disinfectant quantities needed, mixes or dilutes only the required amount, and uses prepared solutions efficiently with minimal waste.",
    role="Animal Research Policy", topics="disinfectant minimization assessment preparation implementation")

add("Environmentally Friendly Disinfectant Policy", "animal",
    "Selected disinfectants are biodegradable, have reduced toxicity to aquatic life and ecosystems, and still maintain effective sterilization against pathogens.",
    role="Animal Research Policy", topics="biodegradable reduced toxicity effective sterilization disinfectant")

add("Space Maximization Policy", "animal",
    "Maximizing rack and room density reduces heating/cooling requirements, minimizes lighting needs, lowers overall energy consumption, and decreases the physical footprint of operations.",
    role="Animal Research Policy", topics="space maximization rack density heating cooling footprint")

add("Cage Reuse and Recycling Policy", "animal",
    "Cages go through sanitization, inspection for integrity, and are returned to service; damaged cages are repaired or their materials recycled.",
    role="Animal Research Policy", topics="cage reuse recycling sanitization inspection repair")

add("Resource Sharing and Carcass Donation Policy", "animal",
    "Multiple scientists coordinate to use samples from a single animal &mdash; tissues and specimens are cataloged and distributed to multiple research teams, maximizing the scientific value of each animal.",
    role="Animal Research Policy", topics="resource sharing carcass donation sample distribution multiple studies")

add("Energy and Water Efficient Equipment Policy", "animal",
    "Cage and rack washers have been upgraded to energy- and water-efficient models, reducing environmental impact while maintaining cleanliness standards.",
    role="Animal Research Policy", topics="cage rack washers energy water efficient")

add("Animal Bedding Composting Policy", "animal",
    "Dirty animal bedding is composted whenever possible, creating a closed-loop system that reduces landfill waste and produces nutrient-rich soil amendments.",
    role="Animal Research Policy", topics="bedding composting landfill closed-loop soil")

add("Animal Food Composting Policy", "animal",
    "Unused or expired animal food is collected and segregated, processed with the appropriate carbon-nitrogen balance, and finished compost is used for landscaping or donated to community gardens.",
    role="Animal Research Policy", topics="food composting collection processing utilization community gardens")

# ---------------- SAFETY & FUME HOODS ----------------
add("Is Your Fume Hood Certified?", "safety",
    "UVA Environmental Health and Safety inspects fume hoods annually. A certification sticker on the hood indicates whether it's safe to work at.",
    role="Chemical Fume Hood Tips", emails=["ehs@virginia.edu"], topics="fume hood certification annual inspection sticker")

add("Fume Hood Safety First", "safety",
    "If the airflow monitor detects a loss of critically safe airflow, stop using the hood, secure chemicals, close the sash, and call UVA EHS to place a work order.",
    role="Chemical Fume Hood Tips", emails=["434-982-4911 — UVA Environmental Health & Safety"],
    topics="airflow monitor loss safe airflow secure chemicals work order")

add("Keep the Fume Hood Clean", "safety",
    "A clean fume hood is essential for user safety and performance. Do not store chemicals or lab materials in the hood; always work at least six inches into the hood.",
    role="Chemical Fume Hood Tips", topics="keep clean no storage six inches")

add("Shut the Sash", "safety",
    "Work with a minimal opening during experiments, and shut the sash entirely when the hood is not in use &mdash; both a safety practice and an energy-saving one.",
    role="Chemical Fume Hood Tips", topics="shut sash minimal opening energy saving")

add("Fume Hood Sash Use Policy", "safety",
    "Personnel must not work in the fume hood with the sash pulled above the sash stop (typically 18\" / 45 cm), for both safety and energy efficiency.",
    role="Environmental Practices", topics="sash stop 18 inches 45cm safety energy")

add("No Storage in Fume Hoods", "safety",
    "Chemicals, reagents, consumables, excess equipment, or containers must not be stored in fume hoods.",
    role="Environmental Practices", topics="no storage fume hoods chemicals containers")

add("Sample and Reagent Storage Policy", "safety",
    "All personnel store samples and reagents at the minimum appropriate temperature specified by manufacturer guidelines, protocols, or SOPs. Refrigeration and freezer units should precisely match the recommended range; periodic audits verify compliance.",
    role="Environmental Practices", topics="sample reagent storage minimum temperature audits sops")

add("Ambient Conditions Preference", "safety",
    "Lab personnel evaluate and, when possible, switch protocols, procedures, or reactions to ambient conditions instead of using elevated or reduced temperatures and pressures.",
    role="Environmental Practices", topics="ambient conditions elevated reduced temperature pressure")

add("Virtual Meetings and Green Travel", "safety",
    "Personnel are encouraged to use virtual meetings, alternative local transportation, and trains instead of short-haul flights for conferences and external meetings whenever feasible.",
    role="Environmental Practices", topics="virtual meetings green travel trains short-haul flights")

# ---------------- FAIR DATA ----------------
add("Findability", "fair",
    "Data has unique identifiers, facilitating reuse, reproducibility, and portability.",
    role="FAIR Data Principles", topics="findability unique identifiers reproducibility portability")

add("Accessibility", "fair",
    "Data is preserved and can be found even when the original workflow is no longer available.",
    role="FAIR Data Principles", topics="accessibility preserved workflow")

add("Interoperability", "fair",
    "Data can be easily translated from one language or management system to another.",
    role="FAIR Data Principles", topics="interoperability translated management system")

add("Reusability", "fair",
    "Data can be modified, built upon, and incorporated into other workflows.",
    role="FAIR Data Principles", topics="reusability modified workflows")

add("The Carbon Cost of Research Computing", "fair",
    "UVA Research Computing was responsible for 1,755 MTCO2e in 2024 &mdash; comparable to 236 homes' energy use for a year, 409 gas-powered vehicles driven for a year, or 4,469,212 miles driven by a gas-powered car.",
    role="FAIR Data Principles",
    links=[{"note":"Estimate your own emissions: Green Algorithms calculator","url":"https://calculator.green-algorithms.org"},
           {"note":"FAIR principles reference paper (Nature)","url":"https://www.nature.com/articles/s41597-025-04451-9"}],
    topics="carbon emissions research computing mtco2e calculator")

# ---------------- AUTOCLAVE LOG ----------------
add("Autoclave Log", "autoclave",
    "Every autoclave is tracked with a monthly cleaning and spore-testing record, plus a per-cycle log covering load description, sterility indicator tape, start/end time, and wet/dry temperature.",
    role="Equipment Records",
    extra="Keeping this current is both a safety requirement and evidence for lab certification audits.",
    links=[{"note":"Download Autoclave_Log_Sheet.xlsx","url":"Autoclave_Log_Sheet.xlsx"}],
    topics="autoclave log monthly cleaning spore testing cycle sterility temperature")

# ---------------- SOURCE DOCUMENTS ----------------
add("Laboratory Sustainability Policies", "docs",
    "The full policy document covering inventory & resource sharing, waste management, energy efficiency, environmental practices, and fume hood & safety practices.",
    role="Source PDF",
    links=[{"note":"Download Laboratory-Sustainability-Policies.pdf","url":"Laboratory-Sustainability-Policies.pdf"}],
    topics="laboratory sustainability policies pdf source document full")

add("Waste Hierarchy Principles", "docs",
    "The full training program on Prevent, Reduce, Reuse, Recycle &mdash; including practical applications, hands-on activities, and the monitoring plan.",
    role="Source PDF",
    links=[{"note":"Download Waste-Hierarchy-Principles-Dr-Mas-Lab.pdf","url":"Waste-Hierarchy-Principles-Dr-Mas-Lab.pdf"}],
    topics="waste hierarchy principles pdf source document training program")

add("Action Plan for Reducing Energy Consumption", "docs",
    "The full energy action plan &mdash; equipment shutdowns, purchasing guidance, freezer/lighting/plug-load optimization, monitoring, maintenance schedule, and building collaboration.",
    role="Source PDF",
    links=[{"note":"Download Action-Plan-for-Reducing-Energy-Consumption-in-Dr-Mas-Lab.pdf","url":"Action-Plan-for-Reducing-Energy-Consumption-in-Dr-Mas-Lab.pdf"}],
    topics="energy action plan pdf source document reducing consumption")

add("FIFO Training Program", "docs",
    "The full First In, First Out training program, including labeling, storage, hands-on activities, and continuous improvement.",
    role="Source PDF",
    links=[{"note":"Download FIFO-Training-Program-for-Dr-Mas-Lab.pdf","url":"FIFO-Training-Program-for-Dr-Mas-Lab.pdf"}],
    topics="fifo training program pdf source document")

add("Understanding the 12 Principles of Green Chemistry", "docs",
    "The full green chemistry training program &mdash; the 12 Principles, practical applications, hands-on activities, analytical chemistry adaptations, and monitoring.",
    role="Source PDF",
    links=[{"note":"Download Understanding-the-12-Principles-of-Green-Chemistry.pdf","url":"Understanding-the-12-Principles-of-Green-Chemistry.pdf"}],
    topics="12 principles green chemistry pdf source document")

add("Ordering Process", "docs",
    "The full structured laboratory ordering process, plus ongoing inventory management practices and environmental/cost optimization strategies.",
    role="Source PDF",
    links=[{"note":"Download Ordering-Process.pdf","url":"Ordering-Process.pdf"}],
    topics="ordering process pdf source document")

add("Sustainable and Responsible Animal Research Policies", "docs",
    "The full set of vivarium policies &mdash; IVC racks, disinfectant use, space maximization, cage reuse, resource sharing, and composting.",
    role="Source PDF",
    links=[{"note":"Download Sustainable_and_Responsible_Animal_Research_Policies.pdf","url":"Sustainable_and_Responsible_Animal_Research_Policies.pdf"}],
    topics="animal research policies pdf source document vivarium")

def main():
    with open(os.path.join(ROOT, "template.html"), encoding="utf-8") as f:
        template = f.read()
    out = template.replace("__DATA__", json.dumps(DATA, indent=2))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote index.html with {len(DATA)} cards")

if __name__ == "__main__":
    main()
