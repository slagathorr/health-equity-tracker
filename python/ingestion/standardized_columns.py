from enum import Enum

RACE_OR_HISPANIC_COL = "race_and_ethnicity"
HISPANIC_COL = "hispanic_or_latino"
RACE_COL = "race"
AGE_COL = "age"
SEX_COL = "sex"
STATE_FIPS_COL = "state_fips"
STATE_NAME_COL = "state_name"
COUNTY_FIPS_COL = "county_fips"
COUNTY_NAME_COL = "county_name"
POPULATION_COL = "population"


# TODO add Asian/Pacific Islander combined, and Indigenous combined
class Race(Enum):
  AIAN = "American Indian and Alaska Native"
  AIAN_NH = "American Indian and Alaska Native (Non-Hispanic)"
  ASIAN = "Asian"
  ASIAN_NH = "Asian (Non-Hispanic)"
  BLACK = "Black or African American"
  BLACK_NH = "Black or African American (Non-Hispanic)"
  HISP = "Hispanic or Latino"
  NHPI = "Native Hawaiian and Pacific Islander"
  NHPI_NH = "Native Hawaiian and Pacific Islander (Non-Hispanic)"
  NH = "Not Hispanic or Latino"
  OTHER = "Some other race"
  OTHER_NH = "Some other race (Non-Hispanic)"
  TOTAL = "Total"
  MULTI = "Two or more races"
  MULTI_NH = "Two or more races (Non-Hispanic)"
  WHITE = "White"
  WHITE_NH = "White (Non-Hispanic)"
