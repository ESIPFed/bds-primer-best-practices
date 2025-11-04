---
name: Contributor Credit Request
about: Contributor Credit Request
title: "[CREDIT] Add contributor: "
labels: ''
assignees: ''

---

- type: textarea
  id: yaml
  attributes:
    label: Contributor YAML
    description: Edit the template below - replace YOUR_*_HERE and delete roles/types that don't apply
    value: |
      - name: YOUR_NAME_HERE
        orcid: YOUR_ORCID_HERE ((e.g. https://orcid.org/0000-0001-7418-1244)
        affiliation: YOUR_INSTITUTION_HERE
        roles:
          - Conceptualization
          - Data Curation
          - Formal Analysis
          - Funding Acquisition
          - Investigation
          - Methodology
          - Project Administration
          - Resources
          - Software
          - Supervision
          - Validation
          - Visualization
          - Writing - Original Draft
          - Writing - Review & Editing
        type: Researcher
        # Other type options (uncomment one if more appropriate):
        # type: DataCollector
        # type: DataCurator
        # type: DataManager
        # type: Distributor
        # type: Editor
        # type: HostingInstitution
        # type: Producer
        # type: ProjectLeader
        # type: ProjectManager
        # type: ProjectMember
        # type: RegistrationAgency
        # type: RegistrationAuthority
        # type: RelatedPerson
        # type: ResearchGroup
        # type: RightsHolder
        # type: Sponsor
        # type: Supervisor
        # type: WorkPackageLeader
        # type: Other
    render: yaml
  validations:
    required: true
