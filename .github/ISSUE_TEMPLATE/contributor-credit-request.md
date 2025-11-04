---
name: Contributor Credit Request
about: Contributor Credit Request
title: "[CREDIT] Add contributor: "
labels: ''
assignees: ''

---

name: Contributor Credit Request
description: Request to be added as a contributor with CRediT taxonomy roles
title: "[CREDIT] Add contributor: "
labels: ["contributors", "credit"]
body:
  - type: markdown
    attributes:
      value: |
        ## Add Yourself as a Contributor
        
        **Instructions:**
        1. In the YAML template below, replace `YOUR_NAME_HERE`, `YOUR_ORCID_HERE`, and `YOUR_INSTITUTION_HERE`
        2. Delete any CRediT roles that DON'T apply to you (keep only what you contributed)
        3. Delete all type options except the ONE that applies to you (usually `Researcher`)
        4. Submit the issue
        
        Maintainers will copy your YAML directly into `contributors.yaml`
  
  - type: textarea
    id: yaml
    attributes:
      label: Contributor YAML
      description: Edit the template below - replace YOUR_*_HERE and delete roles/types that don't apply
      value: |
        ```yaml
          - name: YOUR_NAME_HERE
            orcid: YOUR_ORCID_HERE
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
            # Other type options (delete all except ONE that applies):
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
        ```
      render: yaml
    validations:
      required: true
  
  - type: textarea
    id: notes
    attributes:
      label: Additional Notes
      description: Optional - any additional context about your contributions
    validations:
      required: false
  
  - type: checkboxes
    id: agreement
    attributes:
      label: Agreement
      options:
        - label: I have edited the YAML template above with my information
          required: true
        - label: I have deleted roles that don't apply to me
          required: true
        - label: I have an ORCID ID (get one free at https://orcid.org if needed)
          required: true
        - label: I agree to be listed as a contributor in project documentation and Zenodo records
          required: true
  
  - type: markdown
    attributes:
      value: |
        ---
        **For Maintainers:** Copy the YAML block from above directly into `contributors.yaml`
