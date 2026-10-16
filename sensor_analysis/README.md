# 🤖 AD2070: Lorimar Robot Troubleshooting - Sensor Analysis

## 📌 Problem Description
In the year 2070, a deployed robot (`BOT785`) encounters a malfunction in its ultrasonic distance sensor (Sensor 5). The sensor data feed produces logs containing extra strings, units, and error messages alongside distance values. 

The task is to parse these raw logs, isolate the numeric distance values, and perform statistical triage by calculating the **Mean** and **Sample Standard Deviation** rounded to 4 decimal places.

---

## 🛠️ How We Solved It

The solution is divided into two clear steps:

1. **Data Parsing:**
   * Extract only the float values representing relative distances from the sensor log tuples, discarding non-numeric descriptors.



# 📐 Statistical Formulas Used

This section outlines the mathematical formulas used to analyze the sensor data.

---


## 1. Arithmetic Mean ($\bar{x}$)
The mean is calculated by summing all individual values and dividing by the total count of values ($N$):

$$\bar{x} = \frac{\sum_{i=1}^{N} x_i}{N}$$

* **$\sum x_i$**: The sum of all distance values.
* **$N$**: The total number of data points.

---

## 2. Sample Variance ($s^2$)
Variance measures the average of the squared differences from the mean. Since we are working with a sample rather than an entire population, we use **Bessel's correction** by dividing by $N - 1$:

$$s^2 = \frac{\sum_{i=1}^{N} (x_i - \bar{x})^2}{N - 1}$$

* **$x_i$**: Each individual data point.
* **$\bar{x}$**: The calculated mean.
* **$(x_i - \bar{x})^2$**: The squared difference between each value and the mean.
* **$N - 1$**: Degrees of freedom (Sample size minus 1).

---

## 3. Sample Standard Deviation ($s$)
The standard deviation is the square root of the sample variance, bringing the unit of measurement back to its original form:

$$s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \bar{x})^2}{N - 1}}$$