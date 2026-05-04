"""
Generates a concise presentation speaker script as a Word document.
Run from the project root: python src/make_script.py
Output: outputs/presentation_script.docx
"""

import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

os.makedirs("outputs", exist_ok=True)
doc = Document()

for section in doc.sections:
    section.top_margin    = Inches(0.9)
    section.bottom_margin = Inches(0.9)
    section.left_margin   = Inches(1.1)
    section.right_margin  = Inches(1.1)

def h(text, size=13, bold=True, color=(180,0,0)):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after  = Pt(2)
    r = p.add_run(text)
    r.font.size = Pt(size); r.font.bold = bold
    r.font.color.rgb = RGBColor(*color)

def body(text, indent=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after  = Pt(4)
    if indent:
        p.paragraph_format.left_indent = Inches(0.25)
    r = p.add_run(text)
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(30,30,30)

def bullet(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent  = Inches(0.25)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after  = Pt(2)
    r = p.add_run(f"• {text}")
    r.font.size = Pt(11)

def tag(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after  = Pt(1)
    r = p.add_run(text)
    r.font.size = Pt(10); r.font.bold = True
    r.font.color.rgb = RGBColor(100,100,100)

def rule():
    p = doc.add_paragraph("─" * 70)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(4)
    for r in p.runs:
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor(200,200,200)


# ── Title ─────────────────────────────────────────────────────────────────────
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Housing Market Analysis — Presentation Script")
r.font.size = Pt(18); r.font.bold = True
r.font.color.rgb = RGBColor(180,0,0)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("ISQS 3358  ·  Spring 2026  ·  Texas Tech University")
r.font.size = Pt(11)
r.font.color.rgb = RGBColor(120,120,120)

doc.add_paragraph()
body("Speaker split:  Person 1 → Slides 1–5   |   Ethan → Slides 6, 10–12   |   Person 2 → Slides 7–9, 13–16")
body("Total time: ~13–17 min + Q&A.  Time targets per slide are in brackets.")

rule()


# ══════════════════════════════════════════════════════════════════════════════
# PART 1 — OUTLINE
# ══════════════════════════════════════════════════════════════════════════════
h("PART 1 — OUTLINE", size=14)
body("Quick reference. One look per slide should be enough.")
rule()

outline = [
    ("1", "Title",                "Person 1", "30 sec",
     ["Introduce the team", "State the topic: what drives real home prices?", "Keep it short — let the slides do the work"]),
    ("2", "Roadmap",              "Person 1", "30 sec",
     ["Walk through the 8 sections", "Tell them findings are coming — build anticipation"]),
    ("3", "Project Purpose",      "Person 1", "1.5 min",
     ["Prices rose 5× since 1984 — but only 2× in real terms", "Mortgage rates fell from 14% to 3% — huge effect on affordability",
      "Research question: which economic factors drive real home prices?"]),
    ("4", "Industry Background",  "Person 1", "1.5 min",
     ["$40T market, driven by supply/demand/financing", "Hard to model: different data frequencies, structural breaks",
      "Our approach: FRED, 7 variables, linear regression"]),
    ("5", "Datasets",             "Person 1", "1.5 min",
     ["Walk the table — what each variable is and why it's there", "Explain the frequency problem we had to solve",
      "Target variable: RealPrice = HomePrice ÷ CPI × 100"]),
    ("6", "Data Pipeline",        "ETHAN",    "1.5 min",
     ["5 steps, one command runs everything", "Weekly → monthly mean, annual → forward-fill",
      "Result: 504 clean monthly observations, 1984–2025"]),
    ("7", "Individual Trends",    "Person 2", "1.5 min",
     ["Real price: peak 2006, crash 2008, surge post-2020", "Mortgage rate: 14% → 3% → 7% — nearly mirrors the price chart",
      "Unemployment spike in 2008 lines up perfectly with the crash"]),
    ("8", "Key Relationships",    "Person 2", "1.5 min",
     ["Price vs. mortgage: as rates fell, prices rose — strong negative relationship",
      "Price vs. income (indexed): prices grew nearly 2× faster than income — the affordability gap"]),
    ("9", "Affordability",        "Person 2", "1.5 min",
     ["Nominal 5× vs. real 2× — inflation explains most of it", "Price-to-income ratio: 3.5× in 1984 → 7×+ today",
      "Homes are structurally harder to afford, even adjusted for inflation"]),
    ("10","Model Setup",          "ETHAN",    "1 min",
     ["OLS linear regression, 5 features, 1 target (RealPrice)", "Full dataset: 504 months, no train/test split",
      "Preview: R² = 0.8775"]),
    ("11","Regression Results",   "ETHAN",    "2 min",
     ["R² = 0.88 — model explains 88% of variation, strong result", "Mortgage rate: −$847 per point, biggest negative force",
      "Unemployment: −$1,338 per point", "Income, population, housing starts: all positive",
      "Note multicollinearity — trust the directions, not exact magnitudes"]),
    ("12","Actual vs Predicted",  "ETHAN",    "1 min",
     ["Blue = actual, dashed = model", "Tracks 40-year trend extremely well",
      "Short-term shocks cause noise — fundamentals set the floor"]),
    ("13","Key Findings",         "Person 2", "2 min",
     ["Income is the core positive driver", "Mortgage rate decline quietly subsidized 40 years of price growth",
      "Unemployment and prices move together — 2008 is proof", "Price-to-income doubled — affordability is worse",
      "Inflation masked the real story", "5 variables explain 88% of 40 years of prices"]),
    ("14","Limitations",          "Person 2", "1 min",
     ["National averages only — no regional detail", "Multicollinearity between income, population, and time",
      "Linear model assumes constant relationships over 40 years", "Supply gaps: zoning and land scarcity aren't captured"]),
    ("15","Conclusion",           "Person 2", "1 min",
     ["Economic fundamentals explain 88% of price variation", "Falling rates subsidized prices — now that's reversing",
      "Affordability has quietly doubled in severity since 1984"]),
    ("16","Q&A",                  "Person 2", "—",
     ["Open the floor", "Be ready for: why no train/test split? why linear? regional data?"]),
]

for num, title, who, time, points in outline:
    tag(f"Slide {num}  ·  {title}  [{who}  —  {time}]")
    for pt in points:
        bullet(pt)


rule()

# ══════════════════════════════════════════════════════════════════════════════
# PART 2 — FULL SCRIPT
# ══════════════════════════════════════════════════════════════════════════════
doc.add_page_break()
h("PART 2 — FULL SCRIPT", size=14)
body("Word-for-word. Read it out loud a few times, then go off the outline. You don't have to be exact.")
rule()

script = [
    ("1", "Title", "Person 1", "30 sec",
     "Hey everyone — thanks for having us. I'm [name], and with me today are [teammates]. "
     "We looked at a question that's going to affect most of us pretty soon: what actually drives home prices? "
     "Not what people say drives them — what forty years of data says. Let's get into it."),

    ("2", "Roadmap", "Person 1", "30 sec",
     "Quick roadmap. We'll cover why we picked this topic, where we got the data and how we cleaned it, "
     "then the model and what it found. The interesting stuff really picks up around slide seven — stay with us."),

    ("3", "Project Purpose", "Person 1", "1.5 min",
     "Why housing? It's the biggest financial decision most people will ever make. "
     "Median prices went from $79K in 1984 to over $400K today — that's a five-times increase. "
     "Sounds alarming. But when you adjust for inflation, the real increase is closer to two times. "
     "Half of that price explosion is just general inflation. "
     "We also have mortgage rates going from fourteen percent in 1984 to under three in 2021 — "
     "that shift in borrowing costs had a massive effect on what people could afford. "
     "Our research question is on the bottom of this slide: which economic factors drive "
     "inflation-adjusted home prices, and by how much?"),

    ("4", "Industry Background", "Person 1", "1.5 min",
     "The U.S. housing market is worth over forty trillion dollars and it's highly sensitive "
     "to Federal Reserve rate policy. What makes it hard to model is that supply and demand "
     "operate on different timescales — it takes years to build homes, but rates and employment "
     "can shift in months. Data also comes in at different frequencies: mortgage rates weekly, "
     "income data annually. Our approach was to pull everything from FRED — the Fed's public data "
     "platform — standardize it all to monthly, and run a regression. One pipeline, one command."),

    ("5", "Datasets", "Person 1", "1.5 min",
     "Seven series from FRED. Home price is quarterly. CPI — our inflation index — is monthly. "
     "Mortgage rate is weekly. Unemployment monthly. Median household income annual. "
     "Population and housing starts monthly. "
     "The frequency mismatch was one of our first problems — we'll explain how we handled it. "
     "And importantly, we didn't model home prices directly — we modeled real home prices. "
     "That's home price divided by CPI times a hundred. Strips out inflation so we're looking "
     "at what the housing market is actually doing."),

    ("6", "Data Pipeline", "ETHAN", "1.5 min",
     "Here's the pipeline. Five steps, and you just run main.py — it does everything automatically. "
     "First, it downloads all seven series from FRED. If you want to add a variable, you add one line. "
     "Second, it resamples. Weekly mortgage data gets averaged to a monthly mean. "
     "Annual income gets forward-filled — the yearly value holds each month until the next release. "
     "Third, everything gets merged on date with an outer join. Fourth, we calculate the real price. "
     "Fifth, the regression runs. End result: five hundred and four clean monthly observations, "
     "January 1984 through December 2025."),

    ("7", "Individual Trends", "Person 2", "1.5 min",
     "Six charts — let me hit the key ones. Real price — top left — tells the whole story: "
     "rises through the nineties, peaks in 2006, crashes in 2008, recovers, then surges hard after 2020. "
     "Mortgage rate is almost the mirror image over the long run: fourteen percent in 1984, "
     "falling to under three in 2021, then spiking back to seven. "
     "Unemployment — top right — is smooth until 2008. It doubles in about eighteen months, "
     "and when you overlay it with the price chart, the timing lines up almost exactly with the crash."),

    ("8", "Key Relationships", "Person 2", "1.5 min",
     "Now the relationships. Top chart — price versus mortgage rate. "
     "As rates fell for forty years, prices climbed. When rates reversed in 2022, prices pulled back. "
     "That's one of our strongest model results. "
     "Bottom chart — home price and median income, both indexed to 100 in 1984. "
     "Income grew, but prices grew nearly twice as fast. "
     "You can see the lines diverge, especially after 2000 and again after 2020. "
     "That gap is the affordability problem, right there in one image."),

    ("9", "Affordability", "Person 2", "1.5 min",
     "Two charts on affordability. Left: nominal versus real price. "
     "Nominal looks like a five-times explosion. Real — adjusted for inflation — is about double. "
     "Inflation explains most of the apparent increase. If you're not adjusting, you're misleading yourself. "
     "Right chart: price-to-income ratio. How many years of median income does it take to buy a home? "
     "In 1984: three and a half years. Today: over seven. "
     "That's a doubling of the affordability burden in forty years. "
     "Even after stripping out inflation, homes are significantly harder to buy. That's real."),

    ("10", "Model Setup", "ETHAN", "1 min",
     "The model — ordinary least squares linear regression. "
     "Five features: unemployment, mortgage rate, median income, population, housing starts. "
     "Target: real home price. We trained on the full dataset — all five hundred and four months. "
     "Linear regression because we care about interpretability — we want to say "
     "exactly how much each variable moves the price. I'll preview the result: R-squared of 0.8775."),

    ("11", "Regression Results", "ETHAN", "2 min",
     "Here are the results. R-squared of 0.8775 — the model explains 88% of variation in real home prices "
     "using five variables over forty years. For a simple linear model on real economic data, that's strong. "
     "Root mean squared error works out to about sixty-five hundred dollars — small relative to home prices. "
     "The coefficients: mortgage rate is negative eight forty-seven. Every one percent increase in the "
     "thirty-year rate corresponds to an $847 drop in real price. Makes sense — higher rates price buyers out. "
     "Unemployment is negative thirteen thirty-eight — job losses kill demand and force distressed selling. "
     "Income is positive — higher earnings mean higher prices. Population and housing starts also positive. "
     "One note: income, population, and time all trend upward together, so there's some multicollinearity. "
     "Trust the directions. The exact magnitudes are approximations."),

    ("12", "Actual vs Predicted", "ETHAN", "1 min",
     "Here's the model visually. Blue is the actual real price, dashed is our prediction. "
     "It tracks the forty-year trend extremely well — the 2008 crash, the recovery, the COVID surge. "
     "There's noise in the short run — shocks that five economic variables can't fully anticipate. "
     "But the long-run story is clear: fundamentals set the floor, and events push prices "
     "above or below it temporarily."),

    ("13", "Key Findings", "Person 2", "2 min",
     "Six takeaways. One — income drives prices up. As earnings grow, buyers bid more. "
     "Two — mortgage rates suppress prices. Every point up means about $847 less in real price. "
     "And the forty-year rate decline quietly subsidized growth the entire time. "
     "Three — unemployment drives prices down. 2008 is the proof. "
     "Four — affordability has genuinely worsened. Price-to-income doubled in forty years — "
     "that's not inflation, we already stripped that out. "
     "Five — inflation masked the real story. Nominal prices look scary. Real prices are much more moderate. "
     "Six — five variables explain 88% of four decades of prices. "
     "You don't need a complex model — you need the right variables."),

    ("14", "Limitations", "Person 2", "1 min",
     "What the model can't do. First — it's national data. Texas and California are completely different markets. "
     "Second — multicollinearity. Income and population both trend up over time, "
     "so their individual coefficients are harder to isolate. "
     "Third — linear model. A one percent rate move at fourteen percent isn't the same as one at three percent. "
     "Fourth — housing starts doesn't capture zoning, land scarcity, or construction costs, "
     "which matter a lot in expensive markets."),

    ("15", "Conclusion", "Person 2", "1 min",
     "To wrap up — economic performance drives the housing market, but not always how people think. "
     "The biggest story in our data is the forty-year rate decline. "
     "Fourteen percent to three percent made rising prices feel affordable because monthly payments stayed manageable. "
     "Now that's reversing, and affordability collapsed almost overnight. "
     "The price-to-income ratio tells the rest of the story — homes now take twice as many years of income "
     "to buy as they did in 1984. That's the real affordability crisis, not just the sticker price. "
     "Our model captures 88% of that story with five variables and forty years of data. Thank you."),

    ("16", "Q&A", "Person 2", "—",
     "We'd love to take any questions.\n\n"
     "If asked why no train/test split: We trained on the full dataset to get the best fit. "
     "A chronological split put the COVID era in the test set, which our historical model couldn't predict — "
     "that's a structural break, not a model failure.\n\n"
     "If asked why linear regression: Interpretability. We wanted to quantify each variable's effect. "
     "A black-box model can't give you that, and with R² of 0.88 there's no reason to go more complex.\n\n"
     "If asked about regional data: Great point — that's our main limitation. "
     "National averages smooth over huge regional variation. City-level analysis is the natural next step."),
]

for num, title, who, time, text in script:
    tag(f"Slide {num}  ·  {title}  [{who}  —  {time}]")
    body(text, indent=True)
    rule()

out = "outputs/presentation_script.docx"
doc.save(out)
print(f"Saved → {out}")
