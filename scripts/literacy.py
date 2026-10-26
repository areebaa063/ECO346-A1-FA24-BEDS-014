# Python (Q5)
# literacy.py: Q3 band table and figure recomputed in Python (Q5)
# Variant 6: Balochistan Rural
# Run from the repository root: python scripts/04_literacy.py

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# ---- Load data ----
person = pd.read_csv("data/pslm_person_subset.csv")

hh = pd.read_csv("data/pslm_hh_subset.csv")[
    ["hhid", "hhweight", "prov_code", "urban_rural"]
]

assert hh["hhid"].is_unique

# Join person and household data
dat = person.merge(hh, on="hhid", how="left")

# Variant 6: Balochistan (province code 4), Rural (area code 1)
dat = dat[
    (dat["prov_code"] == 4) &
    (dat["urban_rural"] == 1)
]

# ---- Literacy sample: ages 10-64, literacy not missing ----
lit = dat[
    (dat["age"] >= 10) &
    (dat["age"] <= 64) &
    dat["literate"].notna()
].copy()

lit["band"] = (lit["age"] - 10) // 5
lit["mid"] = 10 + 5 * lit["band"] + 2
lit["wl"] = lit["hhweight"] * lit["literate"]

# ---- Band table: counts and weighted literacy rates ----
g = (
    lit.groupby(["band", "mid", "sex"])
    .agg(
        n=("hhid", "size"),
        wl=("wl", "sum"),
        w=("hhweight", "sum")
    )
    .reset_index()
)

g["rate"] = 100 * g["wl"] / g["w"]
g["thin"] = g["n"] < 30
g["sex_lab"] = g["sex"].map({1: "Men", 2: "Women"})

# ---- Find the largest literacy gap ----
wide = g.pivot(
    index=["band", "mid"],
    columns="sex_lab",
    values="rate"
).reset_index()

wide["gap"] = wide["Men"] - wide["Women"]
top = wide.loc[wide["gap"].abs().idxmax()]

# ---- Create the literacy graph ----
colours = {"Men": "#4adb4a", "Women": "#c02b4b"}

fig, ax = plt.subplots(figsize=(9, 5.5))

for s in ["Men", "Women"]:
    d = g[g["sex_lab"] == s].sort_values("mid")

    ax.plot(
        d["mid"], d["rate"],
        color=colours[s],
        linewidth=1.8
    )

    full = d[~d["thin"]]
    thin = d[d["thin"]]

    ax.scatter(
        full["mid"], full["rate"],
        color=colours[s],
        s=45,
        zorder=3
    )

    # Hollow markers represent cells with fewer than 30 observations
    ax.scatter(
        thin["mid"], thin["rate"],
        facecolors="white",
        edgecolors=colours[s],
        s=45,
        linewidths=1.5,
        zorder=3
    )

    last = d.iloc[-1]

    ax.text(
        last["mid"] + 0.8,
        last["rate"],
        s,
        color=colours[s],
        fontweight="bold",
        va="center"
    )

# Mark the largest gap
ax.plot(
    [top["mid"], top["mid"]],
    [top["Women"], top["Men"]],
    color="grey"
)

ax.text(
    top["mid"] + 0.6,
    (top["Men"] + top["Women"]) / 2,
    f"Largest gap, {int(10 + 5 * top['band'])}-"
    f"{int(14 + 5 * top['band'])}:\n"
    f"{abs(top['gap']):.1f} percentage points",
    va="center"
)

# Age-band labels
bands = [
    f"{10 + 5 * b}-{14 + 5 * b}"
    for b in range(11)
]

ax.set_xticks([12 + 5 * b for b in range(11)])
ax.set_xticklabels(bands)

ax.set_xlim(10, 69)
ax.set_ylim(0, 100)

ax.set_xlabel("Age band (years, plotted at band midpoint)")
ax.set_ylabel("Literacy rate (%)")

ax.set_title(
    f"In rural Balochistan, the literacy gap between men and women "
    f"is widest at ages {int(10 + 5 * top['band'])}-"
    f"{int(14 + 5 * top['band'])}: "
    f"{top['Men']:.1f}% of men vs {top['Women']:.1f}% of women",
    loc="left",
    fontsize=11,
    fontweight="bold"
)

for side in ["top", "right"]:
    ax.spines[side].set_visible(False)

ax.grid(axis="y", color="#e5e5e5")

fig.text(
    0.01, 0.01,
    f"Source: PSLM 2019-20 person file. Sample: persons aged 10-64 "
    f"in rural Balochistan with non-missing literacy "
    f"(n = {len(lit):,}). Weighted by hhweight.\n"
    f"Hollow markers indicate cells with fewer than 30 observations.",
    fontsize=8,
    ha="left",
    va="bottom"
)

fig.tight_layout(rect=(0, 0.07, 1, 1))

# Save the graph
fig.savefig("figures/literacy_python.svg")

# ---- Create the band table ----
py = g.pivot(
    index="band",
    columns="sex_lab",
    values=["n", "rate"]
)

py.columns = [f"{a}_{b}" for a, b in py.columns]
py = py.reset_index()

py["band"] = [
    f"{10 + 5 * b}-{14 + 5 * b}"
    for b in py["band"]
]

py = py[
    ["band", "n_Women", "rate_Women", "n_Men", "rate_Men"]
]

py[["rate_Women", "rate_Men"]] = (
    py[["rate_Women", "rate_Men"]].round(1)
)

py.to_csv("figures/band_table_python.csv", index=False)

# ---- Compare Python results with the R table ----
r = pd.read_csv("figures/band_table.csv")

m = r.merge(
    py,
    on="band",
    suffixes=("_R", "_Py")
)

diff = max(
    (m["rate_Women_R"] - m["rate_Women_Py"]).abs().max(),
    (m["rate_Men_R"] - m["rate_Men_Py"]).abs().max()
)

same_n = (
    (m["n_Women_R"] == m["n_Women_Py"]).all()
    and
    (m["n_Men_R"] == m["n_Men_Py"]).all()
)

# ---- Display results ----
print(py.to_string(index=False))

print("\n===== Q5 CHECK (BALOCHISTAN RURAL) =====")

print(
    "Women 15-19, Python:",
    f"{py.loc[py['band'] == '15-19', 'rate_Women'].iloc[0]:.1f}",
    "| R:",
    f"{r.loc[r['band'] == '15-19', 'rate_Women'].iloc[0]:.1f}"
)

print(
    "Counts identical:", same_n,
    "| Maximum rate difference:", round(diff, 3)
)
