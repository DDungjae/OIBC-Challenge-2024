
library(ggplot2)
library(reshape2)
library(corrplot)
library(car)
df = read.csv("C:/Users/seojw/Documents/POSTECH/OIBC/OIBC_2024_DATA/data/combined.csv", encoding = "UTF8")
model = lm(smp ~ ., data = df)
summary(model)

correlation_matrix = cor(df[,])
smp_corr = correlation_matrix["smp",]
high_corr_pairs = which(abs(smp_corr) > 0.8, arr.ind = TRUE)
low_corr_pairs = which(abs(smp_corr) < 0.1, arr.ind = TRUE)
print(low_corr_pairs)

melted_correlation_matrix = melt(correlation_matrix)

melted_correlation_matrix = subset(melted_correlation_matrix, Var1 == "smp" & Var2 != "smp")

ggplot(melted_correlation_matrix, aes(x = Var2, y = Var1, fill = value)) +
  geom_tile() +
  scale_fill_gradient2(low = "red", high = "blue", mid = "white", 
                       midpoint = 0, limit = c(-1, 1), space = "Lab", 
                       name = "Correlation") +
  theme_minimal() +
  labs(title = "correlation with smp",
       x = "Variables",
       y = "") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


melted_cor_matrix = melt(cor_matrix)

ggplot(data = melted_correlation_matrix, aes(x = Var1, y = Var2, fill = value)) +
  geom_tile() +
  geom_text(aes(label = round(value, 2)), color = "black", size = 2) +  
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", midpoint = 0, 
                       limit = c(-1, 1), space = "Lab", 
                       name = "Correlation") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust = 1))

