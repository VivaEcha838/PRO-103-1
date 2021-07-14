import pandas as pd
import plotly_express as px

df = pd.read_csv("Copy+of+data+-+data.csv")

fig = px.scatter(df, x="date", y="cases", size_max= 80, color="country")
fig.show()