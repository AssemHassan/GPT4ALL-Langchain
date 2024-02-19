import os
import streamlit as st
from langchain_community.llms import gpt4all
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers.json import SimpleJsonOutputParser

model_path = os.path.abspath('./local-models')

MODEL = 'orca-mini-3b-gguf2-q4_0.gguf' #Example SQL Statement: SELECT COUNT(*) FROM Experiment WHERE ExperimentType_ID IN (1,2,3)
#MODEL = 'gpt4all-models/nous-hermes-llama2-13b.Q4_0.gguf' #SQL Statement: SELECT COUNT(*) FROM Experiment GROUP BY ExpermentTypeId;
#MODEL = 'gpt4all-models/all-MiniLM-L6-v2-f16.gguf'
#MODEL = 'gpt4all-models/mistral-7b-openorca.Q4_0.gguf' #SELECT COUNT(*) as NumberOfExperiments, ExperimentTypeId FROM Experiment GROUP BY ExperimentTypeId;
#MODEL = 'gpt4all-models/mistral-7b-instruct-v0.1.Q4_0.gguf' #SELECT E.Name, COUNT(*) AS Count FROM ExperimentType ET JOIN Experiment E ON ET.Id = E.ExperimentTypeId GROUP BY E.Name ORDER BY Count DESC;
#MODEL = 'gpt4all-models/replit-code-v1_5-3b-q4_0.gguf'#?? provides suggestions of several answers
#MODEL = 'gpt4all-models/starcoder-q4_0.gguf'#??
#MODEL = 'gpt4all-models/gpt4all-falcon-q4_0.gguf'#SELECT COUNT(DISTINCT ExperimentTypeId) AS TypeCount FROM ExperimentType WHERE TypeCount = 10;

PATH = os.path.join(model_path, MODEL)

llm = gpt4all.GPT4All(model=PATH)
prompt =  ChatPromptTemplate.from_template(template="""
 given a relational database that has 2 tables:
Experiment and ExperimentType
Table ExperimentType has the following columns
Id, Name, Description with the Primary Key "Id"
Table Experiment has the following columns
Id, ExpName, ExpermentTypeId
with the primary Key "Id" and foreign key ExpermentTypeId for ExperimentType table.
Provide valid SQL statement to answer the following question: {question}?
 
 remember what is required is the SQL Statement with no additional text or explainations.
 """)

outputParser = SimpleJsonOutputParser()
#llm_chain = LLMChain(prompt=prompt, llm=llm)
llm_chain = prompt.pipe(llm);

dict = {}

st.title('🦜🔗 chat with App data')
st.info("This is using the {} model!".format(llm.model))
question = st.text_input('Enter your question here!')
if question:
    dict["question"] = question
    prompt.format(question = question)
    response = llm_chain.invoke(dict)
    #todo extract SQL and runit through your jdbc connection and wrtie back the output
    st.write(response)

