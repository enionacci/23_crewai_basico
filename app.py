import os
import sys 
import streamlit as st
from src.basico.crew import BasicoCrew

# Adiciona o diretório `src` ao caminho de importação
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))



# Título e entrada de texto no Streamlit
st.title("Basico do CrewAI")
st.subheader("Digite um tópico para pesquisa:")
topic = st.text_input("Tópico:")

# Função para iniciar a pesquisa quando o botão for pressionado
if st.button("Iniciar Pesquisa"):
    if topic:
        # Configurando os inputs para o agente BasicoCrew
        inputs = {'topic': topic}
        
        # Executa a pesquisa com o BasicoCrew
        try:
            output = BasicoCrew().crew().kickoff(inputs=inputs)
            st.write("**Resultados da Pesquisa:**")
            st.write(output)  # Exibe a saída gerada

        except Exception as e:
            st.error(f"Ocorreu um erro durante a pesquisa: {e}")
    else:
        st.warning("Por favor, insira um tópico para continuar.")

