# Ma Lab Sustainability & Operations Toolbox

A single-page, searchable directory of Ma Lab's sustainability, safety, and operations policies —
styled after the Department of Surgery's Research Resident Virtual Toolbox (sticky search bar,
filter chips, card grid, navy/orange UVA palette).

No build step, no dependencies, and **no subfolders** — every file (the page, the logos, the
PDFs) sits flat in one folder, ready for GitHub Pages with zero folder-nesting to get wrong.

## What's on the page

- **Sticky search bar** — matches on policy name, description, and topic keywords
- **Filter chips** — Inventory & Ordering, Waste Mgmt, Energy, FIFO, Green Chemistry, Animal
  Research, Safety, FAIR Data, Autoclave, Source Documents
- **76 policy cards** pulled directly from Ma Lab's internal documents, UVA Green Labs /
  Sustainability training materials, and the lab's Genially guide
- The Ma Lab logo in the header and the UVA Sustainable Labs logo in the footer
- A contact panel with the lab's address, phone, and email
- A **Source Documents** filter with the seven original policy PDFs available as direct downloads
- An autoclave log card with the downloadable log-sheet template

## Publishing to GitHub Pages

1. Create a new GitHub repository (e.g. `ma-lab-toolbox`).
2. Unzip this package on your computer, open the unzipped folder, select **everything inside it**
   (Ctrl/Cmd+A), and drag those selected files straight into GitHub's **Add file → Upload files**
   box. Do NOT drag the outer folder itself — drag its contents.
3. Commit the changes.
4. In the repo, go to **Settings → Pages**, set **Source** to the `main` branch, `/ (root)`
   folder, then save.
5. The site publishes at `https://<your-username>.github.io/<repo-name>/` within a minute or two.
6. Sanity check: open `https://<your-username>.github.io/<repo-name>/ma-lab-logo.jpg` directly —
   it should show the logo image on its own. If it 404s, the file didn't make it to the repo root.

## Editing content

All card content lives in `generate.py` as a list of `add(...)` calls — each one is a policy
card with a category (`type`), title, description (`talk`), and optional links/emails/extra text.
File links use bare filenames only (e.g. `"Ordering-Process.pdf"`) since everything is flat.
Edit `generate.py` and re-run:

```bash
python3 generate.py
```

This regenerates `index.html` from `template.html` + the data in `generate.py`.

## Files

```
index.html                                                    # the site
template.html                                                 # HTML/CSS/JS shell
generate.py                                                   # policy content + build script
README.md
ma-lab-logo.jpg
uva-sustainable-labs-logo.jpeg
Autoclave_Log_Sheet.xlsx
Laboratory-Sustainability-Policies.pdf
Waste-Hierarchy-Principles-Dr-Mas-Lab.pdf
Action-Plan-for-Reducing-Energy-Consumption-in-Dr-Mas-Lab.pdf
FIFO-Training-Program-for-Dr-Mas-Lab.pdf
Understanding-the-12-Principles-of-Green-Chemistry.pdf
Ordering-Process.pdf
Sustainable_and_Responsible_Animal_Research_Policies.pdf
```
