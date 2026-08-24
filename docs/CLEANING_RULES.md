# Data Cleaning Rules

## Dataset

**Source:** NSW Fair Trading Residential Rental Bond Lodgements  
**Year:** 2025

### Raw dataset

- 322,307 records
- 5 source variables

---

## Cleaning Rules

### 1. Exact duplicates

**Rule:** Remove records that are identical across all source fields.

**Reason:** Exact duplicate observations do not provide additional information for the rental-price analysis.

**Removed:** 19,196 records.

---

### 2. Unknown weekly rent

**Rule:** Exclude records where Weekly Rent is `U` / unknown.

**Reason:** These records cannot be used for numerical rental-price analysis.

**Remaining unknown-rent records after deduplication:** 2,347.

---

### 3. Zero or negative weekly rent

**Rule:** Exclude records where weekly rent is less than or equal to $0.

**Reason:** These values do not represent a usable positive weekly rental price.

**Removed:** 24 records.

---

### 4. Unknown bedrooms

**Rule:** Convert `U` bedroom values to NULL.

**Reason:** The source definition identifies `U` as unknown. The rental record itself remains usable even when bedroom information is unavailable.

**Records affected:** 2,133.

---

### 5. High bedroom counts

**Rule:** Retain bedroom counts greater than 9 but flag them as potential outliers.

**Reason:** These observations are unusual but cannot be conclusively classified as errors based solely on the available source data.

**Records affected:** 34.

---

### 6. Dwelling type

The source defines the following dwelling types:

| Code | Definition |
|---|---|
| F | Flat/unit |
| H | House |
| T | Terrace/townhouse/semi-detached |
| O | Other |
| U | Unknown |

**Rule:** Retain recognised and unrecognised dwelling-type values in the cleaned dataset.

A `dwelling_type_valid` flag identifies whether the value matches the documented source categories.

**Reason:** Unrecognised codes are preserved rather than assigned an unsupported meaning or silently discarded.

---

## Final Dataset

After duplicate removal and exclusion of records without a usable positive weekly rent:

**300,740 records remain for rental-price analysis.**

### Data quality summary

| Metric | Result |
|---|---:|
| Raw records | 322,307 |
| Exact duplicates removed | 19,196 |
| Unknown rent removed | 2,347 |
| Zero/negative rent removed | 24 |
| Final analysis records | 300,740 |
| Missing bedrooms retained | 2,133 |
| High-bedroom records flagged | 34 |