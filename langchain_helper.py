from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()



def generate_epic(problem_statement):
    llm = OpenAI(model="text-davinci-003")
    
    prompt = PromptTemplate(
        input_variables=["problem_statement"],
        template="""
        You are a worldclass Product Owner who can help to generate EPIC, Capabilities, User Stories, Scenarios, Tasks, BDD and Gherking Test Case.
        
        Generate EPIC for the following problem statement: {problem_statement}
        
        Geneate EPIC as for the Scaled Agile Framework.
        
        An EPIC should contain the following five compoents,
        
1. Epic Name: A concise and descriptive title for the epic, which helps stakeholders quickly understand what the epic is about.

2. Epic Description: A detailed narrative or explanation of the epic's purpose, context, and scope. This provides a comprehensive understanding of why the epic is important and what it aims to achieve.

3. Business Outcomes: Clearly defined business objectives or results that the epic is expected to deliver. These outcomes should align with the organization's strategic goals and provide value.

4. Leading Indicators: Metrics or key performance indicators (KPIs) that serve as early indicators of progress or success for the epic. Leading indicators help track the epic's impact and effectiveness.

5. Non-Functional Requirements: Requirements that describe the characteristics and qualities of the system or product that are not related to specific functionality. This may include performance, security, scalability, reliability, and other non-functional aspects. 
        
        If you feel like you don't have enough information to answer the question, say "Please explain your problem statement little more".
        
        Your answers should be detailed.
        """,
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    response = chain.run(problem_statement=problem_statement)
    return response

def generate_capabilities(epic_description):
    llm = OpenAI(model="text-davinci-003")
    
    prompt = PromptTemplate(
        input_variables=['epic_description'],
        template="""
        You are a worldclass Product Owner who can help to generate EPIC, Capabilities, User Stories, Scenarios, Tasks, BDD and Gherking Test Case.
    
        Based on previous context Geneate Capabilities with Acceptance Criteria for the EPIC: {epic_description}
        
        Capabilities Most of this article is devoted to describing the definition and implementation of features, as they are the most common description of system behavior.
        
        Capabilities exhibit the same characteristics and practices as features. 
        
        For each capabilities generate Acceptance Criteria
        
        Acceptance Criteria: Capability acceptance criteria determine whether the implementation is correct and delivers the business benefits
        
        For example, they: Are described using a phrase and benefit hypothesis Are sized to fit within a PI; however, they often take multiple ARTs to implement Are reasoned about and approved using the Solution Train Kanban. The Solution Train Backlog holds approved capabilities Have associated enablers to describe and bring visibility to all the technical work necessary to support the efficient development and delivery of business capabilities Are accepted by Solution Managers, who use the acceptance criteria to determine whether the functionality is fit for purpose Capabilities may originate in the local context of the solution or occur as a result of splitting portfolio epics that may cut across more than one Value Stream. Another potential source of capabilities is the Solution Context, where some aspects of the environment may require additional solution functionality.
        
        Your answers should be detailed.
        """,
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    response = chain.run(epic_description=epic_description)
    return response

def generate_features(capabilities_description):
    llm = OpenAI(model="text-davinci-003")
    
    prompt = PromptTemplate(
        input_variables=['capabilities_description'],
        template="""
        You are a worldclass Product Owner who can help to generate EPIC, Capabilities, User Stories, Scenarios, Tasks, BDD and Gherking Test Case.
    
        Capabilities must be decomposed into features to be implemented.
        
        Based on previous context Geneate Features with Acceptance Criteria for each capabilities in: {capabilities_description}
        
        Acceptance Criteria: Feature acceptance criteria determine whether the implementation is correct and delivers the business benefits
        
        Only Generate Features not user stories.
        
        Your answers should be detailed.
        """,
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    response = chain.run(capabilities_description=capabilities_description)
    print(response)
    return response


def generate_user_stories_scenarios(features_description):
    llm = OpenAI(model="text-davinci-003")
    
    prompt = PromptTemplate(
        input_variables=['features_description'],
        template="""
        You are a worldclass Product Owner who can help to generate EPIC, Capabilities, User Stories, Scenarios, Tasks, BDD and Gherking Test Case.
    
        Capabilities must be decomposed into features to be implemented.
        
        Based on previous context Geneate Users Stories with Acceptance Criteria for each Feature in: {features_description}
        
        For Each User Story List Different Scenarios and Tasks.
        
        Only Generate Features not user stories.
        
        Your answers should be detailed.
        """,
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    response = chain.run(features_description=features_description)
    print(response)
    return response

if __name__ == "__main__":
    video_url = ""
