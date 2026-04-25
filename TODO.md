# Team TODO — Texas Housing Analysis
**ISQS 3358 | Spring 2026**

---

## Code & Visualizations

> Run `python src/main.py` first to generate `data/processed/final_dataset.csv` and `outputs/`.
> All charts can be made in Python(notebooks/InspectBook.ipynb) (matplotlib / seaborn), Tableau, or Excel.

---

**1. Real Home Price Over Time — Line Chart**
Plot `DATE` vs `REALPRICE` from `final_dataset.csv`.
**Figures out:** How Texas home prices changed after adjusting for inflation. Shows the COVID boom (2020–2022) and the cooldown after the Fed raised rates.

---

**2. Mortgage Rate vs Real Home Price — Dual-Axis Line Chart**
Plot `MortgageRate` and `REALPRICE` on the same chart with two y-axes.
**Figures out:** Whether rising interest rates actually cooled the housing market, and how big the lag was.

---

**3. Correlation Heatmap — All Variables**
Load `final_dataset.csv`, drop `DATE`, run `df.corr()`, plot as a heatmap with seaborn.
**Figures out:** Which variables are most strongly linked to `REALPRICE`. Probably the most important analytical chart we have.

---

**4. Scatter Plots — Each Feature vs REALPRICE**
One scatter plot per variable (UnemploymentRate, MortgageRate, HousingStarts, MedianHouseholdIncome, Population) with a trend line.
**Figures out:** The individual relationship each variable has with home prices — which ones are strong, which are weak, any nonlinear patterns.


---

**5. Actual vs Predicted — Line Chart**
Plot both columns from `outputs/predictions.csv` on the same chart.
**Figures out:** How well the regression model performs. Where it's off (likely 2020–2022 COVID spike) tells us what the model doesn't capture.

---

**6. Housing Starts Over Time — Bar or Line Chart**
Plot `DATE` vs `HousingStarts` from `final_dataset.csv`.
**Figures out:** Whether new construction kept up with Texas population growth, and whether the rate hike slowdown shows up in builder activity.

---

**7. Population & Income Growth — Line Chart**
Plot `Population` and `MedianHouseholdIncome` over time (dual axis or separate panels).
**Figures out:** Whether income kept pace with population growth and home prices, or whether affordability got worse over the decade.

---

**8. Read and Summarize the Model Results**
Open `outputs/results.txt`. Write 3–5 plain-English bullet points answering:
- What is the R² — is the model a good fit?
- Which variable has the biggest effect on price?
- What does the model say drives Texas housing prices up vs down?

---
---

## Presentation Outline
*10–20 minutes. Here's a rough script of what we say and in what order.*

---

### Slide 1 — Title
> *"Texas Housing Market Analysis — What's Really Driving Home Prices?"*
> Names, class, date.

---

### Slide 2 — What Are We Doing and Why Should You Care?
> *"Texas is the second largest state in the country and one of the fastest growing. Home prices have nearly doubled over the last decade. We wanted to know — what economic forces are actually behind that? Is it interest rates? Population growth? Income? All of the above?"*
>
> *"This matters for anyone buying a home, investing in real estate, or setting housing policy. If you can predict what moves prices, you can make better decisions."*

---

### Slide 3 — Our Data (brief overview)
> *"We pulled 7 economic variables, all from the Federal Reserve's public data portal FRED, covering January 2015 through December 2025."*

List the 7 variables with a one-line description each. Mention:
- Mortgage data was weekly so we averaged it to monthly
- Income and population are annual releases so we forward-filled them month by month
- Home prices are adjusted for inflation using CPI so we're comparing apples to apples

---

### Slide 4 — Real Home Price Over Time (Chart 1)
> *"Here's the headline. Inflation-adjusted Texas home prices rose steadily from 2015 to 2022, peaked during COVID, and have come down since. But they haven't come all the way back. This is the thing we're trying to explain."*

Show the line chart. Point out the COVID spike and the post-2022 decline.

---

### Slide 5 — Mortgage Rates vs Home Prices (Chart 2)
> *"This is probably the most interesting chart. In 2022 the Fed raised rates aggressively — mortgage rates went from around 3% to over 7%. You can see home prices peak right around there and start coming down. The relationship isn't instant — there's a lag of several months — but it's clearly there."*

---

### Slide 6 — What the Data Shows (Correlation Heatmap, Chart 3)
> *"When we look at how all variables relate to each other, [point to strongest correlations]. Population and income are positively correlated with price — as Texas grows and gets wealthier, prices go up. Mortgage rate and unemployment are negatively correlated — when those go up, prices tend to come down."*

---

### Slide 7 — The Model
> *"We built a linear regression model using all of our economic variables to predict the inflation-adjusted home price. Here's what it found."*

Show the R², list the coefficients, explain in plain English which variable had the biggest effect. Point out where the model struggled (probably the COVID years) using the actual vs predicted chart.

---

### Slide 8 — Data Quality Notes
> *"A few things worth noting about the data quality."*

- October 2025 values were missing due to the government shutdown — we filled them with the previous month
- Income data is published one year behind — our 2025 income estimate is carried forward from 2024
- The home price series we used (TXUCSFRCONDOSMSAMID) is a strong proxy but not a perfect match for the original Zillow data we started with — values differ by about 1–2%
- Mortgage data required averaging weekly observations into monthly values

---

### Slide 9 — Conclusions
> *"So what did we find? Texas home prices are real and inflation-adjusted peak in 2022. Mortgage rates appear to be the single strongest short-term driver of price movement. Population growth and income support long-term price floors. The model captures the general trend well but misses the COVID shock — which tells us there are forces (like pandemic migration) that aren't captured by economic fundamentals alone."*

---

### Slide 10 — What We'd Do Differently
> *"If we had more time we'd look at city-level data instead of state-level, add supply-side data like construction permits, and try a more flexible model that can capture nonlinear effects like the COVID shock."*

Open for questions.

---
