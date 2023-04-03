# MAKE YOUR DATA SOFTWARE READY

## Use non-proprietary formats

### Why?

- Allows data to be useful in perpetuity by ensuring data readability and reusability across multiple platforms.
- To align better with the FAIR principles (findability, accessibility, interoperability, reusability)
- Makes data more socially equitable, supporting open science. Proprietary formats can depend on software that require licenses, which not everyone can afford/has access to.

### Key Information

- Non-proprietary formats are supported by more than one developer and can be accessed with different software systems. For example, comma separated values (CSV) format is becoming an increasingly popular non-proprietary format.
- A [proprietary file format](https://en.wikipedia.org/wiki/Proprietary_file_format) is a file format of a company, organization, or individual that contains data that is ordered and stored according to a particular encoding-scheme, designed by the company or organization to be secret or with restricted access, such that the decoding and interpretation of this stored data is easily accomplished only with particular software or hardware that the company itself has developed. There may also be costs associated with it and access may be limited. Examples include Microsoft Excel (xlsx) and ESRI shapefiles (shp).
- Many applications (e.g. Microsoft Office) allow exporting in multiple formats.


### Top 5 References

- Table of commonly used formats for common data types: https://guides.osu.edu/c.php?g=707751&p=5027409  
- A more detailed table that is specific to US Federal records management: https://www.archives.gov/records-mgmt/policy/transfer-guidance-tables.html

## Structure data in tidy/long format

![Data table taken from: https://www.datafix.com.au/BASHing/2022-01-12.html](2022-01-12_1.png)


### Why?

This is specifically intended for tabular data
- There is a clear and easy to understand structure that can make your data more machine readable and easier to analyze/visualize.
  - Clear structure: one observation per row
  - Data are as atomic as possible (e.g., don’t mix types in field)
- In the biological data community, tidy formats are more likely to work with commonly-used software
- Easier to aggregate data across multiple files

### Key Information

- Example: Each scientific name as individual columns (non-tidy/wide) vs. a single column (tidy/long) called scientific_name
- Can be tricky working with multiple column datatypes
- Don’t use colors or text formatting in tabular data, and only include column names as metadata. All other notes, definitions, etc. should be in an external metadata file (e.g. data dictionary) 

### Top 5 References

- Wickham, H. (2014). Tidy Data. Journal of Statistical Software, 59(10), 1–23. https://doi.org/10.18637/jss.v059.i10
- Data Sharing and Management Snafu in 3 Short Acts (video) https://www.youtube.com/watch?v=N2zK3sAtr-4&t=7s
- Tips for working with data in BASH https://www.datafix.com.au/BASHing/2022-01-12.html 
- Data Organization in Spreadsheets for Ecologists https://datacarpentry.org/spreadsheet-ecology-lesson/ 
- Cleaning Data and Quality Control https://edirepository.org/resources/cleaning-data-and-quality-control#data-table-structure

## Follow ISO 8601 for dates

![](https://imgs.xkcd.com/comics/iso_8601.png)


### Why?

- Internationally accepted format used across multiple schemas (e.g. Darwin Core, EML, ISO 19115)
- Removes ambiguity related to timezone, daylight savings time changes, and time of day
- Better software integration of time date/time elements

### Key Information

- Zulu = GMT = UTC: is the primary time standard by which the world regulates clocks and time. It is time relative to 0° longitude and is not adjusted for daylight saving time. (from Wikipedia).
- Conversion to UTC, or between time zones, may depend on daylight savings
- Todo: Table from Wiki showing examples of all possible formats
   - Example of date range
   - Date parts (annotated)

### Top 5 References

- ISO 8601 wiki: https://en.wikipedia.org/wiki/ISO_8601
- R package lubridate, OlsonNames()
- Python go-to package, datetime https://docs.python.org/3/library/datetime.html 
- Article on datetime uncertainty: https://www.datafix.com.au/BASHing/2020-02-12.html  
- Map of offset from UTC: https://www.timeanddate.com/time/map/ 
- Nice time converter: https://coastwatch.pfeg.noaa.gov/erddap/convert/time.html


### Is anything missing?

- How is this handled when reporting dates from paleontological and archaeological specimens?
   - Make some recommendations for these use cases.

## Match scientific names to a taxonomic authority

### Why?

- Definition: A taxonomic authority is an internationally recognized, used and actively maintained classification of species.
- To integrate or aggregate datasets, we have to have a common frame of reference for taxonomic name
- Provides an anchor for the taxonomy as scientific understanding evolves.


### Key Information

- Use an existing taxonomic authority (e.g. World Register of Marine Species : https://www.marinespecies.org/ , Integrated Taxonomic Information System : https://itis.gov/ , NCBI taxonomy : https://www.ncbi.nlm.nih.gov/taxonomy ) and include the authority who manages said information in your metadata
- List of many authorities can be found here: https://resolver.globalnames.org/data_sources
- Make yourself aware of the structure, limits, and history of the authority you are using.
- Adopt standard binomial nomenclature, when possible
- When possible, reference the unique identifier in addition to the nomenclature.
- Always save and document the originally recorded name.
- Put notes about identification uncertainty in a separate column.
- Many authorities have APIs through which you can match names to identifiers.


### Top 5 References
- R packages
  - taxize is a taxonomic toolbelt for R. taxize wraps APIs for a large suite of taxonomic databases availabe on the web.
    - https://cran.r-project.org/web/packages/taxize/index.html
    - worrms is an API client for World Register of Marine Species (<http://www.marinespecies.org/>). 
http://cran.nexr.com/web/packages/worrms/vignettes/worrms_vignette.html
    - WoRMS:  another API client for WoRMS
      - https://cran.r-project.org/web/packages/worms/index.html
    - Ritis: API client for ITIS
       - https://cran.r-project.org/web/packages/ritis/ 
- Python packages
  - WoRMS API client
    - https://github.com/iobis/pyworms
- Global Names Resolver to compare taxonomic concepts across authorities.
  - https://resolver.globalnames.org/ 
- Article: Recommendations for the Standardisation of Open Taxonomic Nomenclature for Image-Based Identifications
  - https://doi.org/10.3389/fmars.2021.620702 
- TDWG 2022 Keynote: Richard Pyle, “An Introduction to the Scientific Names of Organisms and the Taxon Concepts they Represent”
  - https://www.youtube.com/watch?v=rmTvUUjBxrI

### Is anything missing?

- Unrealistic to mandate single taxonomic database across all fields and all metadata; better to mandate inclusion of DB or reference used in each case
- Is it possible to map from one authority to another via machine readable/AI means?
  - NCBI >> GTDB works
  - Would be necessary/have to happen to have this be machine readable?
- How do we define a taxonomic authority ? 
  - International recognized, used and actively maintained 
- How do we help people go to the “correct” authority? 
  - ITIS, WORMs, AOS (https://checklist.americanornithology.org) 
  - Is there a ‘catalogue’ or decision tree for taxonomic authorities?

## Record latitude and longitude in decimal degrees in WGS84

![](https://imgs.xkcd.com/comics/coordinate_precision.png)

### Why?
- Users have to know where you collected this data, which requires a latitude, longitude, reference system and uncertainty.
- Decimal-degrees avoids special symbols (° or  ‘) which is preferable for machine readable formats
- WGS84 is a reference coordinate system that is widely used and incorporated in many GPS units and tools, and recognized as a standard by many government agencies.


### Key Information
- If possible, encourage data providers to confirm, and record, the WGS84 datum is selected prior to data collection.
- Understand and report the device/instrument uncertainty associated with your coordinates because it affects the usability of your data.
- Consider including the vertical component (altitude, depth, height off bottom, elevation, etc)
- Generally speaking, degrees-minutes-seconds (DMS) can be converted to decimal-degrees (DD) by: 
  - DD = d + (min/60) + (sec/3600)
  - Watch out for mixed formats, like degrees, decimal-minutes (DDM).
- Degrees West and South become negative in DD.
  - Values for longitude range from -180 to 180
  - Values for latitude range from -90 to 90


### Top 5 References
- Existing R/python/ESRI packages/functions
  - https://cran.r-project.org/web/packages/measurements/measurements.pdf 
  - https://eml.ecoinformatics.org/schema/index.html (find “bounding Coordinates)
  - https://cfconventions.org/Data/cf-conventions/cf-conventions-1.10/cf-conventions.html#latitude-coordinate
- Getting lat/lon to decimal degrees 
  - https://ioos.github.io/bio_mobilization_workshop/03-data-cleaning/index.html#getting-latlon-to-decimal-degrees
- Something that gives more background on precision, like this: https://www.trekview.org/blog/2021/reading-decimal-gps-coordinates-like-a-computer/#a-note-on-accuracy
Degree-Minute-Seconds -> DD calculator: https://www.fcc.gov/media/radio/dms-decimal


### Is anything missing?
- We debated whether or not decimal degrees should be emphasized at all.  Is it more important to get the data collectors to use a standard, or show data managers how to convert between standards?

## Use globally unique identifiers

### Why?
- It can be useful to have unique identifiers to unambiguously identify granules of information, e.g. dataset, collection, database, taxonomic concept, etc. This will allow users to precisely refer to the data and allow your data to remain identifiable when aggregated with other datasets.
- To be able to uniquely identify a record in your data system or across data systems.
Useful to create relational databases or merge records.
- Although it increases workload, it safeguards against confusion and inefficiency in the future.

### Key Information
- There are good reasons to keep an identifier opaque, i.e. it does not indicate anything about the content of information it points to. However, there are also transparent, or semi-opaque identifiers in use that take advantage of semantics to guide humans as well as machines.
- One way to create a unique identifier is concatenation of sampling event, location, time, enumeration of unique observation or event.
  #Station_95_Date_09JAN1997:14:35:00.000
- Some prefer using opaque identifiers.
  #10FC9784-B30F-48ED-8DB5-FF65A2A9934E
- If there is an existing globally unique identifier, it’s usually a good idea to use it (i.e. when using a taxonomic authority like WoRMS and applying their LSID).
- It is important to manage any identifiers you create, if they are not managed by an authority (e.g. DOIs).
- Important that it be persistent (consider samples possibly moving between institutions)


### Top 5 References
- Packages to generate uuids:
  - https://cran.r-project.org/web/packages/uuid/index.html 
  - https://docs.python.org/3/library/uuid.html 
  - http://guid.one/
  - https://guidgenerator.com/
- Guidance on how to use GUIDs (Globally Unique Identifiers) to meet specific requirements of the biodiversity information community
  - http://bioimages.vanderbilt.edu/pages/guid-applicability-final-2011-01.pdf
- Use of globally unique identifiers (GUIDs) to link herbarium specimen records to physical specimens
  - https://bsapubs.onlinelibrary.wiley.com/doi/full/10.1002/aps3.1027 
- A Beginner’s Guide to Persistent Identifiers
  - http://links.gbif.org/persistent_identifiers_guide_en_v1.pdf 
