import pandas as pd
import plotly.express as px

df = pd.read_csv("SPFB.RTS-12.18_180901_181231.csv", encoding="utf-8")
target_dates = ["07/09/18", "09/10/18", "07/11/18", "07/12/18"]
df = df[df["<DATE>"].isin(target_dates)]

df.to_csv("data.csv", index=False)

df_long = df.melt(
    id_vars=["<DATE>"],
    value_vars=["<OPEN>", "<HIGH>", "<LOW>", "<CLOSE>"],
    var_name="Показатель",
    value_name="Цена"
)

df_long["Показатель"] = df_long["Показатель"].replace({
    "<OPEN>": "Открытие",
    "<HIGH>": "Макс",
    "<LOW>": "Мин",
    "<CLOSE>": "Закрытие",
})

fig = px.box(
    df_long,
    x="<DATE>",
    y="Цена",
    color="Показатель",
    title="Ящик с усами",
    labels={"<DATE>": "Дата", "Цена": "Стоимость (пункты)"}
)

fig.update_layout(
    xaxis_tickangle=-45,
    legend_title_text="Показатели",
    template="plotly_white"
)

fig.show()
