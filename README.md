Here's a well-structured **README.md** file based on your OCD data analysis project:

---

# Understanding Obsessive-Compulsive Disorder (OCD) Trends with Data Analysis

![Causes-of-OCD image](https://github.com/TeniOT/Understanding-Obsessive-Compulsive-Disorder-OCD-Trends-A-Data-Analysis/assets/164643376/1a08941d-5635-463c-8e65-9d53e8264732)

> Photo credit: emotionalwellnesclinic.co.uk

## Table of Contents

* [Introduction](#introduction)
* [Dataset Overview](#dataset-overview)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Key Findings](#key-findings)
* [Conclusion](#conclusion)
* [Recommendations](#recommendations)
* [References](#references)

---

## Introduction

Obsessive-Compulsive Disorder (OCD) is a mental health condition affecting millions worldwide. This project uses statistical and visual analysis to explore patterns and potential contributing factors. Our goal is to understand how demographics, symptoms, and treatment methods influence OCD trends and prevalence.

---

## Dataset Overview

* **Source**: [OCD Patient Dataset – Kaggle](https://www.kaggle.com/datasets/ohinhaque/ocd-patient-dataset-demographics-and-clinical-data/)
* **Type**: Combination of survey responses, clinical records, and research data.
* **Size**: 1500 rows × 17 columns
* **Key Variables**:

  * Age, Gender, Ethnicity
  * Y-BOCS Scores (Obsessions & Compulsions)
  * OCD Types (e.g., Harm, Washing)
  * Comorbidities (Anxiety, Depression)
  * Treatment types (e.g., Benzodiazepines, None)
* **Tools Used**: Python (Pandas, Seaborn, Matplotlib), Power BI

---

## Exploratory Data Analysis

1. **Demographics**:

   * Bar plots were used to analyze the distribution by gender and ethnicity.

2. **Diagnosis Trends**:

   * Monthly and yearly diagnosis patterns were explored.
   * Highest diagnoses were recorded in January; peak year was 2018.

3. **Symptom Severity**:

   * Y-BOCS scores were used to measure obsession and compulsion severity.
   * Gender-specific differences were noted.

4. **Types of OCD**:

   * Harm-related obsessions and washing compulsions were most common.

5. **Treatment Methods**:

   * Compared patients receiving no treatment vs. those prescribed medications.
   * Benzodiazepines were the most prescribed drug class.

6. **Correlation Analysis**:

   * Pearson correlation heatmap showed no strong linear relationships between variables.

   ![Correlation Heatmap](https://github.com/TeniOT/Exploring-correlation-in-Python-with-OCD-Dataset/assets/164643376/66ee4722-9220-4750-9cee-c729051b89f0)

---

## Key Findings

### Demographics

* Most affected age group: **25–34 years**
* Slightly higher prevalence in **Females**
* **Caucasians** lead in diagnosis, followed closely by **Hispanics**
* **Africans** have the lowest recorded OCD diagnoses

### Diagnosis Patterns

* Peak diagnosis in **January**
* Spike in **2018**, slight dip in 2019, and plateau from 2020–2022 (possibly due to COVID-19)

![Diagnosis Trends](https://github.com/TeniOT/Understanding-Obsessive-Compulsive-Disorder-OCD-Trends-A-Data-Analysis/assets/164643376/eb633b01-8ef6-4e4c-bf05-3f08d5cd3f37)

### Symptom Insights

* **Females** scored higher on obsessions
* **Males** scored higher on compulsions
* Common OCD types: Harm-related (obsessions) and Washing (compulsions)
* Comorbid anxiety and depression were frequently reported

### Treatment Analysis

* Equal number of patients on **no medication** and **Benzodiazepines**
* Benzodiazepines were the most commonly prescribed treatment
* Further exploration needed to identify specific medications prescribed

---

## Conclusion

Understanding OCD through data provides valuable insights into demographic trends, symptom patterns, and treatment effectiveness. The findings suggest:

* A higher prevalence among females and Caucasians
* Harm and washing are the most common OCD symptoms
* Need for more tailored treatment approaches based on symptom severity and comorbidity

The stable trend post-2019 might be influenced by limited healthcare access during the COVID-19 pandemic.

---

## Recommendations

* Conduct deeper research into:

  * Environmental and genetic risk factors
  * Regional access to mental health care
* Investigate underrepresentation of **African** populations
* Explore **personalized treatment strategies** for better remission outcomes
* Expand analysis to include more detailed pharmaceutical data

---

## References

* 📊 Dataset: [Kaggle OCD Patient Dataset](https://www.kaggle.com/datasets/ohinhaque/ocd-patient-dataset-demographics-and-clinical-data/)
* 🧠 Learn more about OCD: [NHS UK – OCD Overview](https://www.nhs.uk/mental-health/conditions/obsessive-compulsive-disorder-ocd/overview/)

---

Would you like help turning this into a Power BI dashboard, Jupyter notebook markdown, or even creating a project report PDF?
