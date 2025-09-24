# Solution 1
df_high_revenue = df.query("`Revenue (Millions)` > 150").sort_values(by="Rating", ascending=False)
df_high_revenue["rating_category"] = df_high_revenue["Rating"].apply(lambda x: 'good' if x >= 7.0 else 'bad')
plt.figure(figsize=(20, 13))
sns.histplot(data=df_high_revenue, x="Rating", hue="rating_category", multiple="stack", bins='auto', palette="magma", kde=True, kde_kws={'bw_adjust': 2, 'cut': 3})

# Solution 2
sns.boxplot(x='Year', y='Rating', data=df)