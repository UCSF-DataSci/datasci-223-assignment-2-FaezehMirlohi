### 📄 **Cohort Analysis Report**

---

#### **1. Analysis Approach**

The goal was to analyze patient cohorts based on **BMI ranges** and compute:

- Average glucose level  

- Average age  

- Patient count  

First,

- Loaded a CSV and converted it to a **Parquet** file for faster access.  

- Used **Polars LazyFrame** to build an efficient processing pipeline.  

- Filtered BMI values to a valid range (10–60).  

- Assigned BMI categories: *Underweight, Normal, Overweight, Obese*.  

- Grouped data by BMI range and aggregated key health metrics.

---

#### **2. Patterns and Insights**

**Cohort Analysis Results:**

| bmi_range   | avg_glucose | patient_count | avg_age   |
|-------------|-------------|----------------|-----------|
| Normal      | 108.004737  | 664,064        | 31.888848 |
| Obese       | 126.032016  | 3,066,409      | 33.827130 |
| Underweight | 95.195115   | 26,041         | 23.980646 |
| Overweight  | 116.373363  | 1,165,360      | 32.880893 |

After running the analysis, I observe trends below:

- A concentration of patients in the *Obese* and *Overweight* ranges.

- Higher **BMI** groups showed increased **average glucose**.

- Higher **BMI** groups had slightly higher average **age**

---

#### **3. Efficient Use of Polars**

- **Lazy evaluation**: The pipeline was built using `pl.scan_parquet()` and `.pipe()` calls. This avoids loading all data into memory at once.

- **Streaming `.collect()`**: `.collect(streaming=True)` was used to allow chunked processing of large datasets.

- **Conditional logic**: `pl.when(...).then(...).otherwise(...)` was used with `pl.lit(...)` to efficiently label BMI ranges without error.

Overall, Polars provided fast, memory-efficient processing — ideal for large patient datasets.