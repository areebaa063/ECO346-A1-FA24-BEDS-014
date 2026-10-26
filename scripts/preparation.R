
# preparation.R: Prepare data for Variant 6 (Balochistan Rural)
# Run this script from the repository root.

library(tidyverse)

# Check that both dataset files exist
stopifnot(
  file.exists("data/pslm_person_subset.csv"),
  file.exists("data/pslm_hh_subset.csv")
)

# Load datasets
person <- read_csv(
  "data/pslm_person_subset.csv",
  show_col_types = FALSE
)

hh <- read_csv(
  "data/pslm_hh_subset.csv",
  show_col_types = FALSE
)

# Variant 6: Balochistan (province code 4), Rural (area code 1)
VAR_PROV <- 4
VAR_AREA <- 1

# Select required household columns
hh_keep <- hh |>
  select(hhid, hhweight, prov_code, urban_rural)

# Check that each household ID is unique
stopifnot(!anyDuplicated(hh_keep$hhid))

# Join household information with person records
dat <- person |>
  left_join(hh_keep, by = "hhid") |>
  filter(
    prov_code == VAR_PROV,
    urban_rural == VAR_AREA
  )

# Check that every person has a household weight
stopifnot(!anyNA(dat$hhweight))

# Prepare the literacy sample for ages 10–64
lit <- dat |>
  filter(
    age >= 10,
    age <= 64,
    !is.na(literate)
  ) |>
  mutate(
    band = floor((age - 10) / 5),
    band_lab = paste0(
      10 + 5 * band, "-", 14 + 5 * band
    ),
    mid = 10 + 5 * band + 2,
    sex_lab = factor(
      sex,
      levels = c(1, 2),
      labels = c("Men", "Women")
    )
  )

# Prepare the student sample:
# Include only people with annual education spending above zero
stu <- dat |>
  filter(ed_total > 0)

# Display sample sizes
cat(
  "Variant 6 (Balochistan Rural)",
  "| Persons:", nrow(dat),
  "| Literacy sample:", nrow(lit),
  "| Students:", nrow(stu),
  "\n"
)

