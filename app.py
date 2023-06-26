import plotly.express as px
import streamlit as st
import pandas as pd

st.write("hello world")
st.title('VISUALISATION')
st.subheader("merci pour votre analyse")

uploaded_file = st.file_uploader('Choisir un fichier XLSX ', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)

    groupby_column = st.selectbox(
        'What would you like to analyse?',
        ('annees','investissement', 'Croissance du PIB (% annuel)','IDE_sorties_nettes ','Taux de change ','Chomage ', "code_pays", "Exportations de biens et services "),
    )
    # -- GROUP DATAFRAME
    output_columns = ['Croissance du PIB (% annuel)', 'Exportations de biens et services ']
    df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].mean()
    st.dataframe(df_grouped)
    # -- PLOT DATAFRAME
    fig = px.bar(
        df_grouped,
        x=groupby_column,
        y='Croissance du PIB (% annuel)',
        color='Exportations de biens et services ',
        color_continuous_scale=['red', 'yellow', 'green'],
        template='plotly_white',
        title=f'<b>Croissance du PIB (% annuel) & Exportations de biens et services  by {groupby_column}</b>'
    )
    st.plotly_chart(fig)
