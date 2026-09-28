import pandas as pd # 1 passo importas o Panda e o "as" para criar apelido e escolhemos o pd usado pela comunidade.

df =  pd.DataFrame(
    {
    "Nome": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss Elizabeth",
    ],
    "Idade": [23, 36, 58],
    "Genêro": ["Masculino", "Masculino", "Femenino"],
    }
)

print(df)