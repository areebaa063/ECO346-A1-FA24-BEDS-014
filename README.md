# ECO346 Assignment 1: Data Visualization Techniques for Economists

**University:** COMSATS University Islamabad, Lahore Campus   
**Course:** ECO346 — Data Visualization Techniques for Economists   
**Semester:** Fall 2026
**Student Name:** Areeba Tahir   
**Registration Number:** FA24-BEDS-014    
**Selected Variant:** Variant 6 - Balochistan Rural

---

## 1. Project Overview

This project analyzes Pakistan Social and Living Standards Measurement (PSLM) Survey 2019–20 data for rural Balochistan. It examines annual education spending and literacy rates across age groups and genders.

R is used to prepare the data, calculate weighted statistics, and create visualizations. Python is used to reproduce the literacy analysis and compare its results with R.

### Objectives

* Examine annual education spending among students in rural Balochistan.
* Calculate weighted and unweighted spending statistics.
* Compare literacy rates between men and women across age groups.
* Identify the age group with the largest gender literacy gap.
* Reproduce the literacy analysis in Python and compare it with R.
* Improve the clarity and readability of data visualizations.

---

## 2. Selected Variant and Data

**Selected variant: Variant 6 — Balochistan Rural**

| Variable                     | Selected Value |
| ---------------------------- | -------------- |
| Province                     | Balochistan    |
| Province code                | 4              |
| Area                         | Rural          |
| Area code                    | 1              |
| Household identifier         | `hhid`         |
| Household weight             | `hhweight`     |
| Literacy age range           | 10–64 years    |
| Education spending condition | `ed_total > 0` |

### Datasets

The project uses two datasets:

1. [`pslm_person_subset.csv`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/data/pslm_person_subset.csv): Contains individual-level information, including age, gender, literacy status, and annual education spending.
2. [`pslm_hh_subset.csv`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/data/pslm_hh_subset.csv): Contains household-level information, including household weights, province codes, and urban/rural classification.

The datasets are stored in the `data/` directory.

**Data source:** PSLM Survey 2019–20, provided through the course repository.

Repository: https://github.com/rafi-amiruddin/DVTE

### Data Preparation

The person and household datasets are joined using `hhid`. The analysis is restricted to rural Balochistan using province code 4 and area code 1.

The literacy sample includes individuals aged 10–64 with non-missing literacy information. The education spending sample includes individuals with annual education spending greater than zero.

Household weights (`hhweight`) are used to calculate weighted spending statistics and literacy rates.

### Sample Sizes

| Sample                                      | Number of Observations |
| ------------------------------------------- | ---------------------: |
| Persons in rural Balochistan                |                  8,463 |
| Literacy sample                             |                  5,677 |
| Students with education spending above zero |                  1,464 |

---

## 3. Question 2: Distribution of Annual Education Spending

### Method

A weighted histogram is used to examine annual education spending among students in rural Balochistan.

The horizontal axis uses a logarithmic scale because spending values vary considerably. The histogram shows weighted density, while dashed vertical lines indicate the weighted median and weighted 90th percentile.

The histogram includes spending values from Rs 100 to Rs 1,000,000. Observations outside this range are excluded from the histogram but remain included in the calculation of the spending statistics.

Weighted quantiles are calculated according to the assignment's specified method: observations are sorted by spending, cumulative household-weight shares are calculated, and the smallest spending value reaching the required percentile is selected.

### Results

| Statistic                        |    Result |
| -------------------------------- | --------: |
| Total number of students         |     1,464 |
| Weighted median spending         |  Rs 3,500 |
| Unweighted median spending       |  Rs 3,000 |
| Weighted 10th percentile         |    Rs 600 |
| Weighted 90th percentile         | Rs 18,700 |
| 90th-to-10th percentile ratio    |     31.17 |
| Students excluded from histogram |         1 |

### Figure

The weighted histogram is saved as: [`figures/distribution.svg`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/figures/distribution.svg)


### Interpretation

The weighted median annual education spending is Rs 3,500, compared with an unweighted median of Rs 3,000. The weighted 10th percentile is Rs 600, while the 90th percentile is Rs 18,700. The 90th-to-10th percentile ratio of 31.17 indicates substantial differences in education spending among students in rural Balochistan. Only one student falls outside the histogram's displayed spending range.

---

## 4. Question 3: Literacy Rates by Age Group and Gender

### Method

This analysis compares weighted literacy rates for men and women aged 10–64 in rural Balochistan.

The sample is divided into eleven five-year age bands, from 10–14 to 60–64. Each age band is plotted at its midpoint: 12, 17, 22, and so on, up to 62.

Weighted literacy rates are calculated separately for men and women using `hhweight`.

Different colours distinguish the two gender groups. Solid markers represent groups with at least 30 unweighted observations, while hollow markers represent groups with fewer than 30 observations.

The largest gender gap is identified by comparing the absolute difference between men's and women's literacy rates across the age bands.

### Complete Age-Band Table

| Age Band | Women: Count | Women: Literacy Rate (%) | Men: Count | Men: Literacy Rate (%) |
| -------- | -----------: | -----------------------: | ---------: | ---------------------: |
| 10–14    |          428 |                     40.9 |        663 |                   60.1 |
| 15–19    |          293 |                     33.3 |        477 |                   63.8 |
| 20–24    |          307 |                     22.8 |        358 |                   61.7 |
| 25–29    |          347 |                     24.8 |        355 |                   56.5 |
| 30–34    |          309 |                     15.1 |        297 |                   52.9 |
| 35–39    |          252 |                     15.0 |        266 |                   53.8 |
| 40–44    |          198 |                      7.5 |        227 |                   55.4 |
| 45–49    |          149 |                      8.2 |        181 |                   32.7 |
| 50–54    |          111 |                     14.9 |        133 |                   27.0 |
| 55–59    |           79 |                      3.5 |         95 |                   39.7 |
| 60–64    |           59 |                      1.0 |         93 |                   39.8 |

### Important Comparisons

* **Women's literacy rate, ages 15–19:** 33.3%
* **Men's literacy rate, ages 15–19:** 63.8%
* **Women's literacy rate, ages 55–59:** 3.5%
* **Men's literacy rate, ages 55–59:** 39.7%
* **Age band with the largest gender gap:** 40–44 years
* **Size of the largest gender gap:** 47.9 percentage points

### Figure

The R literacy graph is saved as: [`figures/literacy.svg`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/figures/literacy.svg)

### Interpretation

Literacy rates are higher among men than women in every age group shown. Among people aged 15–19, the rate is 63.8% for men and 33.3% for women. Among those aged 55–59, it falls to 39.7% for men and 3.5% for women. The largest gap is 47.9 percentage points in the 40–44 age group. These results highlight substantial gender differences in literacy in rural Balochistan.

### Limitation

The analysis describes weighted literacy patterns but cannot establish why these gender differences exist. Factors such as household income, access to schools, and educational opportunities may also influence literacy outcomes.

---

## 5. Question 4: Default Graph and Redesign

### Default Graph

The default scatterplot is created in R using the following code:

```r
ggplot(lit, aes(age, literate)) +
  geom_point()
```

The original graph is saved as: [`figures/default.svg`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/figures/default.svg)

### Redesigned Graph

The literacy graph from Question 3 is used as the redesigned visualization.

**File:** [`figures/literacy.svg`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/figures/literacy.svg)

### Design Changes

The redesigned graph improves the default graph in several ways:

1. **Age grouping:** Individual ages are organized into five-year age bands, making comparisons easier.
2. **Gender comparison:** Separate colours and labels distinguish men and women.
3. **Clear labels:** Descriptive axis labels and a meaningful title explain the information presented.
4. **Highlighting important findings:** The largest gender gap is marked directly on the graph.
5. **Sample-size information:** Hollow markers identify groups with fewer than 30 observations.

These changes improve clarity, comparison, and visual communication.

### What the Default Graph Shows That the Redesign Hides

The default graph displays individual observations, showing the raw relationship between age and literacy status. The redesigned graph summarizes these observations into weighted literacy rates for age groups and gender categories. This makes overall patterns easier to compare but hides individual-level variation.

---

## 6. Question 5: Reproducing the Literacy Analysis in Python

### Method

The literacy analysis is reproduced in Python using Pandas and Matplotlib. The same datasets, household weights, province and area filters, age range, and literacy sample restrictions are applied as in R.

Python calculates the number of observations and weighted literacy rates for each age band and gender. It also identifies groups with fewer than 30 observations and finds the age band with the largest gender literacy gap.

The Python results are compared with the R results to check whether the observation counts and literacy rates agree.

### Output Files

* [`figures/literacy_python.svg`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/figures/literacy_python.svg): Literacy graph created in Python.
* [`figures/band_table_python.csv`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/figures/band_table_python.csv)`: Python age-band results.
* [`figures/band_table.csv`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/figures/band_table.csv): R age-band results.

### Verification Results

The final verification values should be taken from the output of [`scripts/literacy.py`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/blob/main/scripts/literacy.py)

| Check                                         | Result                              |
| --------------------------------------------- | ----------------------------------- |
| Women's literacy rate, ages 15–19, in R       | 33.3%                               |
| Women's literacy rate, ages 15–19, in Python  | 33.3% expected if the scripts agree |
| Are observation counts identical?             | Confirm using Python output         |
| Maximum absolute difference in literacy rates | Confirm using Python output         |

The R and Python results should agree to one decimal place, as required by the assignment.

### Difference Between the Default Outputs

R and Python use different plotting systems and may apply different default settings for point appearance, spacing, and layout. To make the literacy graphs comparable, the same age-band midpoints, weighted literacy rates, axis limits, and sample restrictions are used in both implementations.

---

## 7. Project Structure

The repository is organized as follows:

```text
ECO346-A1-FA24-BEDS-014/
│
├── README.md
│
├── data/
│   ├── pslm_person_subset.csv
│   └── pslm_hh_subset.csv
│
├── scripts/
│   ├── preparation.R
│   ├── default.R
│   ├── distribution.R
│   ├── literacy.R
│   └── literacy.py
│   ├── preparation.R
│   ├── default.R
│   ├── distribution.R
│   ├── literacy.R
│   └── literacy.py
│
├── figures/
│   ├── default.svg
│   ├── distribution.svg
│   ├── literacy.svg
│   ├── literacy_python.svg
│   ├── band_table.csv
│   └── band_table_python.csv
│
└── slides/
    └── FA24-BEDS-014.pptx
```

---

## 8. How to Run the Code

### Required R Packages

* `tidyverse`
* `ggplot2`
* `svglite`
* `scales`


### Required Python Packages

* `pandas`
* `matplotlib`


## 9. Conclusion

This project uses PSLM 2019–20 data to examine annual education spending and literacy patterns in rural Balochistan.

The spending analysis shows a weighted median annual education expenditure of Rs 3,500 and a 90th-to-10th percentile ratio of 31.17, indicating substantial variation in spending.

The literacy analysis shows that men's literacy rates exceed women's rates across all age groups in the results presented. The largest observed gap is 47.9 percentage points among people aged 40–44.

Reproducing the literacy analysis in Python provides a way to check the consistency of the calculations and visualizations across programming languages.

---

## 10. Reproducibility and Version Control

- The datasets are stored in [`data/`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/tree/main/data)
- Analysis scripts in [`scripts/`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/tree/main/scripts)
- Generated graphs and tables in [`figures/`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/tree/main/figures)
- Presentation in [`slides/`](https://github.com/areebaa063/ECO346-A1-FA24-BEDS-014/tree/main/slides)

Git is used to track changes throughout the project. The default graph is committed before the redesigned graph so that the original and improved visualizations can be compared.

The public repository contains the code, datasets, generated outputs, and documentation needed to understand and reproduce the analysis.
