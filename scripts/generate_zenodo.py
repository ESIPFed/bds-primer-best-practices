import yaml
import json
from datetime import datetime

# Read template
with open('zenodo_template.json', 'r') as f:
    zenodo_metadata = json.load(f)

# Read contributors
with open('CONTRIBUTORS.yaml', 'r') as f:
    contributors = yaml.safe_load(f)

# Separate creators (5+ roles) from contributors (< 5 roles)
creators = []
zenodo_contributors = []
cff_authors = []
cff_contributors = []

for person in contributors:
    role_count = len(person.get('roles', []))
    
    # Format name as "Last, First" for Zenodo
    name_parts = person['name'].split()
    if len(name_parts) >= 2:
        formatted_name = f"{name_parts[-1]}, {' '.join(name_parts[:-1])}"
        family_name = name_parts[-1]
        given_names = ' '.join(name_parts[:-1])
    else:
        formatted_name = person['name']
        family_name = person['name']
        given_names = ''
    
    # Zenodo entry
    zenodo_entry = {
        "name": formatted_name,
        "affiliation": person.get('affiliation', ''),
        "orcid": person.get('orcid', '').replace('https://orcid.org/', '')
    }
    
    # CFF entry
    cff_entry = {
        "family-names": family_name,
        "given-names": given_names,
        "affiliation": person.get('affiliation', ''),
        "orcid": person.get('orcid', '')
    }
    
    if role_count >= 5:
        creators.append(zenodo_entry)
        cff_authors.append(cff_entry)
    else:
        zenodo_entry['type'] = person.get('type', 'Researcher')
        zenodo_contributors.append(zenodo_entry)
        cff_contributors.append(cff_entry)

# Add creators and contributors to zenodo metadata
zenodo_metadata['creators'] = creators
zenodo_metadata['contributors'] = zenodo_contributors

# Build CITATION.cff
citation_metadata = {
    "cff-version": "1.2.0",
    "message": "If you use this guide, please cite it using these metadata.",
    "title": zenodo_metadata['title'],
    "abstract": "An introductory guide to biological data standards, developed as a companion to the ESIP Biological Data Standards Primer. This resource helps researchers organize and share biological data using community standards.",
    "authors": cff_authors,
    "keywords": zenodo_metadata['keywords'],
    "license": zenodo_metadata['license'],
    "repository-code": "https://github.com/ESIPFed/bds-primer-best-practices",
    "type": "software",
    "date-released": datetime.now().strftime("%Y-%m-%d")
}

# Add contributors if any
if cff_contributors:
    citation_metadata["contributors"] = cff_contributors

# Write zenodo.json
with open('.zenodo.json', 'w') as f:
    json.dump(zenodo_metadata, f, indent=2)

# Write CITATION.cff
with open('CITATION.cff', 'w') as f:
    yaml.dump(citation_metadata, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

print(f"Generated .zenodo.json with {len(creators)} creators and {len(zenodo_contributors)} contributors")
print(f"Generated CITATION.cff with {len(cff_authors)} authors and {len(cff_contributors)} contributors")
