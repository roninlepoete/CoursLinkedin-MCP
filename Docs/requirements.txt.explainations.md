# 📦 Explications détaillées - requirements.txt

## Liste des packages installés

```
mcp[cli]==1.10.1
openai==1.75.0
python-dotenv
requests
httpx
pandas
langchain
langchain-openai
langgraph
```

---

## 1️⃣ **mcp[cli]==1.10.1**

**Fonction :** Model Context Protocol - SDK Python pour créer/utiliser des serveurs MCP

**Rôle :**
- Créer des serveurs MCP en Python
- Client MCP pour interagir avec des serveurs
- `[cli]` = extras pour outils en ligne de commande

**Usage typique :**
```python
from mcp.server import Server

server = Server("my-mcp-server")

@server.tool()
def get_weather(city: str) -> str:
    return f"Weather in {city}: Sunny"
```

**Documentation :** https://modelcontextprotocol.io

---

## 2️⃣ **openai==1.75.0**

**Fonction :** SDK officiel OpenAI pour interagir avec GPT-4, GPT-3.5, etc.

**Rôle :**
- Appeler les APIs OpenAI (chat, embeddings, etc.)
- Function calling
- Assistants API
- Génération de texte, images (DALL-E), audio

**Usage typique :**
```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

**Documentation :** https://platform.openai.com/docs

---

## 3️⃣ **python-dotenv**

**Fonction :** Charger les variables d'environnement depuis un fichier `.env`

**Rôle :**
- Stocker les clés API de façon sécurisée
- Configuration sans hardcoder dans le code
- Séparation config dev/prod

**Usage typique :**
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Charge le fichier .env
api_key = os.getenv("OPENAI_API_KEY")
```

**Fichier .env :**
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxx
DATABASE_URL=postgresql://localhost/mydb
DEBUG=True
```

**Documentation :** https://github.com/theskumar/python-dotenv

---

## 4️⃣ **requests**

**Fonction :** Bibliothèque HTTP simple et élégante

**Rôle :**
- Faire des requêtes HTTP (GET, POST, PUT, DELETE)
- Appeler des APIs REST
- Alternative plus simple à urllib
- Support cookies, sessions, authentification

**Usage typique :**
```python
import requests

# GET request
response = requests.get("https://api.example.com/data")
data = response.json()

# POST request
payload = {"name": "Fabrice", "email": "fab@example.com"}
response = requests.post("https://api.example.com/users", json=payload)
```

**Documentation :** https://requests.readthedocs.io

---

## 5️⃣ **httpx**

**Fonction :** Client HTTP moderne avec support async

**Rôle :**
- Requêtes HTTP synchrones ET asynchrones
- Alternative moderne à `requests`
- Support HTTP/2
- Compatible avec FastAPI, asyncio

**Usage typique :**
```python
import httpx

# Sync
response = httpx.get("https://api.example.com")
print(response.json())

# Async
async with httpx.AsyncClient() as client:
    response = await client.get("https://api.example.com")
    data = response.json()
```

**Pourquoi httpx ET requests ?**
- `requests` : Simple, synchrone, très répandu
- `httpx` : Moderne, async, HTTP/2

**Documentation :** https://www.python-httpx.org

---

## 6️⃣ **pandas**

**Fonction :** Manipulation et analyse de données tabulaires

**Rôle :**
- Lire/écrire CSV, Excel, JSON, SQL
- Transformer des datasets (filtrer, grouper, agréger)
- Analyse de données
- Nettoyage de données

**Usage typique :**
```python
import pandas as pd

# Lire CSV
df = pd.read_csv("data.csv")

# Afficher aperçu
print(df.head())

# Filtrer
df_filtered = df[df['age'] > 30]

# Statistiques
print(df.describe())

# Sauvegarder
df_filtered.to_csv("filtered_data.csv", index=False)
```

**Documentation :** https://pandas.pydata.org

---

## 7️⃣ **langchain**

**Fonction :** Framework pour construire des applications LLM

**Rôle :**
- Créer des chaînes de prompts
- Orchestrer des agents
- RAG (Retrieval Augmented Generation)
- Memory (mémoire de conversation)
- Tools (outils pour agents)
- Document loaders

**Usage typique :**
```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Traduis le texte suivant en anglais : {text}"
)
chain = LLMChain(llm=llm, prompt=template)
result = chain.run(text="Bonjour le monde")
```

**Composants principaux :**
- **Chains** : Séquences d'opérations LLM
- **Agents** : Systèmes autonomes avec outils
- **Memory** : Conversation history
- **Retrievers** : Recherche de documents
- **Tools** : Fonctions appelables par agents

**Documentation :** https://python.langchain.com

---

## 8️⃣ **langchain-openai**

**Fonction :** Intégration OpenAI pour LangChain

**Rôle :**
- Utiliser GPT-4/GPT-3.5 dans LangChain
- Embeddings OpenAI pour RAG
- Chat models OpenAI
- Remplace l'ancienne intégration dans langchain core

**Usage typique :**
```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Chat model
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7
)
response = llm.invoke("Explique-moi les agents IA")

# Embeddings pour RAG
embeddings = OpenAIEmbeddings()
vector = embeddings.embed_query("Mon texte")
```

**Documentation :** https://python.langchain.com/docs/integrations/platforms/openai

---

## 9️⃣ **langgraph**

**Fonction :** Framework pour construire des agents avec graphes d'état

**Rôle :**
- Créer des workflows agentic complexes
- Agents multi-étapes avec conditions
- Graphes d'état pour orchestration
- Alternative moderne et plus flexible à LangChain Agents

**Usage typique :**
```python
from langgraph.graph import StateGraph, END

# Définir les états
class AgentState:
    messages: list
    plan: str
    done: bool

# Créer le graphe
graph = StateGraph(AgentState)

# Ajouter les nœuds
graph.add_node("planner", plan_action)
graph.add_node("executor", execute_action)
graph.add_node("evaluator", evaluate_result)

# Ajouter les transitions
graph.add_edge("planner", "executor")
graph.add_conditional_edges(
    "evaluator",
    should_continue,
    {
        "continue": "planner",
        "end": END
    }
)

# Compiler et exécuter
agent = graph.compile()
result = agent.invoke(initial_state)
```

**Avantages vs LangChain Agents :**
- ✅ Contrôle granulaire du workflow
- ✅ Visualisation du graphe
- ✅ Debuggabilité supérieure
- ✅ Gestion d'état explicite

**Documentation :** https://langchain-ai.github.io/langgraph/

---

## 🎯 Résumé par catégorie

| Package | Catégorie | Rôle principal |
|---------|-----------|----------------|
| **mcp** | MCP | Créer/utiliser serveurs MCP |
| **openai** | LLM | Appeler GPT-4 directement |
| **python-dotenv** | Config | Gérer variables d'environnement |
| **requests** | HTTP | Requêtes HTTP simples (sync) |
| **httpx** | HTTP | Requêtes HTTP modernes (async) |
| **pandas** | Data | Manipulation de données |
| **langchain** | Framework | Orchestration LLM |
| **langchain-openai** | Intégration | OpenAI dans LangChain |
| **langgraph** | Agents | Agents avec graphes d'état |

---

## 🔥 Stack typique pour agent MCP

```python
# 1. Configuration
from dotenv import load_dotenv
import os
load_dotenv()

# 2. LLM
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))

# 3. Agent avec LangGraph
from langgraph.graph import StateGraph

# Définir workflow agent
graph = StateGraph()
graph.add_node("think", think_step)
graph.add_node("act", action_step)
graph.add_edge("think", "act")
agent = graph.compile()

# 4. Serveur MCP
from mcp.server import Server
server = Server("my-agent")

@server.tool()
def process_data(data: str) -> str:
    # Utiliser l'agent
    result = agent.invoke({"input": data})
    return result

# 5. HTTP pour APIs externes
import httpx
async with httpx.AsyncClient() as client:
    response = await client.get("https://api.example.com/data")
    external_data = response.json()
```

---

## 💡 Pourquoi cette stack ?

**C'est un ensemble complet pour :**
- ✅ Créer des **agents IA** (langchain, langgraph)
- ✅ Utiliser des **LLM** (openai, langchain-openai)
- ✅ Construire des **serveurs MCP** (mcp)
- ✅ Faire des **requêtes HTTP** (requests, httpx)
- ✅ Analyser des **données** (pandas)
- ✅ Gérer la **config sécurisée** (python-dotenv)

**Parfait pour un cours sur les agents IA avec MCP !** 🚀

---

---

## 🔀 LangChain vs LangGraph : Comparaison approfondie

### Vision Flow Chart

**LangChain** = Séquence linéaire ou chaîne simple  
**LangGraph** = Graphe d'état avec nœuds décisionnels

---

### 🔗 **LangChain (Chains)**

**Architecture :** Pipeline linéaire ou séquentiel

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Input   │───→│ Step 1  │───→│ Step 2  │───→│ Output  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
```

**Caractéristiques :**
- ✅ Flux **linéaire** (A → B → C)
- ⚠️ Conditions **limitées** (if/else simples)
- ❌ Pas de **boucles** complexes
- ❌ Pas de **branchements** conditionnels avancés
- ✅ Simple et rapide pour workflows **prédictifs**

**Exemple LangChain classique :**
```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Chaîne linéaire simple
chain = (
    PromptTemplate.from_template("Résume : {text}")
    | llm
    | StrOutputParser()
)

result = chain.invoke({"text": "Mon long texte..."})
```

**Flow Chart LangChain :**
```
START
  ↓
[Prompt Template] ← Input
  ↓
[LLM Call]
  ↓
[Output Parser]
  ↓
END
```

---

### 🌐 **LangGraph (Graphes d'État)**

**Architecture :** Graphe avec nœuds et transitions conditionnelles

```
                    ┌─────────┐
              ┌────→│ Node A  │────┐
              │     └─────────┘    │
┌─────────┐   │                    ↓      ┌─────────┐
│ START   │───┤     ┌─────────┐   ?   ───→│  END    │
└─────────┘   │     │ Node B  │───┘      └─────────┘
              └────→└─────────┘
```

**Caractéristiques :**
- ✅ **Nœuds décisionnels** (conditions complexes)
- ✅ **Boucles** et cycles (retry, itération)
- ✅ **Branches parallèles**
- ✅ **État partagé** entre nœuds
- ✅ Gestion **explicite des transitions**
- ✅ **Visualisation** du graphe
- ✅ **Debuggabilité** supérieure

**Exemple LangGraph avec décisions :**
```python
from langgraph.graph import StateGraph, END

# Définir l'état partagé
class AgentState(TypedDict):
    messages: list
    plan: str
    iterations: int
    done: bool

# Créer le graphe
graph = StateGraph(AgentState)

# Ajouter les nœuds
graph.add_node("planner", plan_step)
graph.add_node("executor", execute_step)
graph.add_node("evaluator", evaluate_step)

# Transitions simples
graph.add_edge("planner", "executor")

# Transition CONDITIONNELLE (décision)
def should_continue(state):
    if state["done"]:
        return "end"
    elif state["iterations"] > 5:
        return "retry"
    else:
        return "continue"

graph.add_conditional_edges(
    "evaluator",
    should_continue,
    {
        "continue": "planner",  # Boucle
        "retry": "executor",     # Retry
        "end": END              # Fin
    }
)

# Compiler
agent = graph.compile()
```

**Flow Chart LangGraph :**
```
START
  ↓
[Planner Node]
  ↓
[Executor Node]
  ↓
[Evaluator Node]
  ↓
  ? (Decision Node)
  ├─ done=True → END
  ├─ iterations>5 → [Executor] (retry)
  └─ else → [Planner] (loop)
```

---

### 📊 Comparaison détaillée

| Critère | LangChain | LangGraph |
|---------|-----------|-----------|
| **Type** | Pipeline/Chain | Graphe d'état |
| **Flux** | Linéaire (A→B→C) | Graphe (branches, boucles) |
| **Décisions** | If/else basique | Nœuds conditionnels avancés |
| **Boucles** | ❌ Difficile | ✅ Natif |
| **État** | Implicite | ✅ Explicite partagé |
| **Branches parallèles** | ❌ Non | ✅ Oui |
| **Visualisation** | ⚠️ Limitée | ✅ Graphe complet |
| **Debug** | ⚠️ Moyen | ✅ Excellent |
| **Complexité** | 🟢 Simple | 🟡 Moyenne |
| **Use case** | Workflows simples | Agents complexes |

---

### 🎯 Nœuds dans LangGraph

#### **1. Nœuds de Traitement (Processing Nodes)**
```python
def process_node(state: AgentState):
    # Traitement des données
    result = llm.invoke(state["messages"])
    state["messages"].append(result)
    return state
```

**Flow :**
```
[Input State] → [Process] → [Output State]
```

#### **2. Nœuds Décisionnels (Decision Nodes)**
```python
def decision_node(state: AgentState) -> str:
    if state["score"] > 0.8:
        return "success"
    elif state["retries"] < 3:
        return "retry"
    else:
        return "fail"
```

**Flow :**
```
        [State]
          ↓
    [Decision ?]
    ├─ success → [Success Node]
    ├─ retry → [Retry Node]
    └─ fail → [Fail Node]
```

#### **3. Nœuds d'Entrée/Sortie (I/O Nodes)**
```python
def input_node(state: AgentState):
    # Charge données externes
    data = fetch_from_api()
    state["external_data"] = data
    return state

def output_node(state: AgentState):
    # Formatte et sauvegarde
    save_to_database(state["result"])
    return state
```

**Flow :**
```
[START] → [Input Node] → ... → [Output Node] → [END]
```

#### **4. Nœuds d'Exécution (Action Nodes)**
```python
def action_node(state: AgentState):
    # Exécute un outil
    tool_result = execute_tool(state["action"])
    state["observations"].append(tool_result)
    return state
```

**Flow :**
```
[Plan] → [Execute Tool] → [Observe] → [Evaluate]
```

---

### 🔥 Exemple concret : Agent ReAct

#### **Version LangChain (limitée)**
```python
# LangChain Agent - Flux linéaire
agent = initialize_agent(
    tools=[search_tool, calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Pas de contrôle granulaire du workflow
result = agent.run("Quel est le PIB de la France ?")
```

**Flow Chart (boîte noire) :**
```
[Input] → [Agent (boîte noire)] → [Output]
          ↓ (invisible)
          [Think] → [Act] → [Observe] → (loop?)
```

#### **Version LangGraph (contrôle total)**
```python
from langgraph.graph import StateGraph, END

class ReActState(TypedDict):
    input: str
    thoughts: list
    actions: list
    observations: list
    answer: str
    iterations: int

graph = StateGraph(ReActState)

# Nœud : Raisonnement
def think_node(state):
    thought = llm.invoke(f"Pense à comment résoudre : {state['input']}")
    state["thoughts"].append(thought)
    return state

# Nœud : Décision d'action
def decide_action_node(state):
    action = llm.invoke(f"Quelle action ? {state['thoughts'][-1]}")
    state["actions"].append(action)
    return state

# Nœud : Exécution
def execute_node(state):
    result = execute_tool(state["actions"][-1])
    state["observations"].append(result)
    state["iterations"] += 1
    return state

# Nœud décisionnel : Continuer ?
def should_continue(state):
    if "réponse finale" in state["observations"][-1]:
        return "finish"
    elif state["iterations"] >= 5:
        return "max_iterations"
    else:
        return "continue"

# Construction du graphe
graph.add_node("think", think_node)
graph.add_node("decide", decide_action_node)
graph.add_node("execute", execute_node)
graph.add_node("finish", finish_node)

# Transitions
graph.set_entry_point("think")
graph.add_edge("think", "decide")
graph.add_edge("decide", "execute")

# Transition conditionnelle
graph.add_conditional_edges(
    "execute",
    should_continue,
    {
        "continue": "think",      # Boucle ReAct
        "finish": "finish",       # Terminer
        "max_iterations": END     # Stop forcé
    }
)

agent = graph.compile()
```

**Flow Chart (contrôle total) :**
```
START
  ↓
[Think Node]
  ↓
[Decide Action Node]
  ↓
[Execute Node]
  ↓
  ? [Decision: should_continue?]
  ├─ "continue" → [Think Node] (BOUCLE ReAct)
  ├─ "finish" → [Finish Node] → END
  └─ "max_iterations" → END
```

---

### 💡 Quand utiliser quoi ?

#### **Utilise LangChain Chains quand :**
- ✅ Workflow **simple et linéaire**
- ✅ Pas de décisions complexes
- ✅ Rapidité de développement
- ✅ Prototype simple

**Exemples :**
- Résumé de texte
- Traduction
- Q&A simple sur documents

#### **Utilise LangGraph quand :**
- ✅ **Agents avec décisions** complexes
- ✅ **Boucles** et retry logic
- ✅ **Branches conditionnelles**
- ✅ **État partagé** entre étapes
- ✅ Besoin de **debuggabilité**
- ✅ Workflows **adaptatifs**

**Exemples :**
- Agents ReAct autonomes
- Systèmes multi-agents
- Workflows avec validation/retry
- Pipelines de décision complexes

---

### 🎯 Visualisation comparative

#### **LangChain Chain**
```
Input → Step1 → Step2 → Step3 → Output
```
**Avantage :** Simple  
**Limite :** Pas de décisions/boucles

#### **LangGraph Graph**
```
           ┌──────────┐
     ┌────→│  Step2   │─────┐
     │     └──────────┘     │
     │                      ↓
┌────┴────┐            ┌────┴────┐
│  Step1  │            │  Step4  │
└────┬────┘            └────┬────┘
     │                      │
     │     ┌──────────┐     │
     └────→│  Step3   │─────┘
           └──────────┘
```
**Avantage :** Contrôle total, décisions, boucles  
**Trade-off :** Plus complexe à setup

---

### 🔧 Types de nœuds en détail

| Type de Nœud | Rôle | Exemple LangGraph |
|--------------|------|-------------------|
| **Processing** | Traitement données | `llm.invoke()`, transformation |
| **Decision** | Branchement conditionnel | `if/elif/else` → routes |
| **I/O** | Lecture/Écriture externe | API calls, DB, fichiers |
| **Action** | Exécution outils | Tools, fonctions |
| **Merge** | Fusion branches parallèles | Combine résultats |
| **Loop** | Répétition | Retry, itération |

---

### 📚 Ressources complémentaires

- **MCP Docs** : https://modelcontextprotocol.io
- **OpenAI Platform** : https://platform.openai.com
- **LangChain** : https://python.langchain.com
- **LangGraph** : https://langchain-ai.github.io/langgraph/
- **LangGraph Tutorials** : https://langchain-ai.github.io/langgraph/tutorials/
- **Pandas** : https://pandas.pydata.org
- **HTTPX** : https://www.python-httpx.org
