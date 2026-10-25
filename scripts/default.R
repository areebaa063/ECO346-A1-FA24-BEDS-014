# 01_default.R: Default scatterplot for Variant 6 (Balochistan Rural)
# Question 4: R's untouched default scatterplot

# Load prepared data
source("scripts/preparation.R")

library(ggplot2)
library(svglite)

# Create figures folder if it does not exist
dir.create("figures", showWarnings = FALSE)

# Create the default scatterplot
p <- ggplot(lit, aes(x = age, y = literate)) +
  geom_point()

# Save the graph as an SVG file
ggsave("figures/default.svg", plot = p)

# Display the graph
print(p)
