import pandas as pd
import numpy as np
import cufflinks as cf

# konfiguracja cufflinks
cf.set_config_file(sharing='public', theme='ggplot', offline=True)
cf.go_offline()

# wczytanie i czyszczenie danych
df = pd.read_csv('population_total.csv')
df['country'] = df['country'].astype(str).str.strip()
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['population'] = pd.to_numeric(df['population'], errors='coerce')
df = df.dropna(subset=['year', 'population'])
df['year'] = df['year'].astype(int)
df['population'] = df['population'].astype(np.int64)

# pivot: rok vs kraj
df_pivot = df.pivot_table(index='year', columns='country', values='population', aggfunc='sum').sort_index()

# wybór top 10 krajów w 2020
top10 = df_pivot.loc[2020].sort_values(ascending=False).head(10).index.tolist()
plot_df = df_pivot[top10]

# wykres interaktywny
fig = plot_df.iplot(kind='line', xTitle='Year', yTitle='Population', title='Top 10 Countries by Population Over Time', asFigure=True)
fig.show()
