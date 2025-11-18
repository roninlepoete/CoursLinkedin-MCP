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

## 📚 Ressources complémentaires

- **MCP Docs** : https://modelcontextprotocol.io
- **OpenAI Platform** : https://platform.openai.com
- **LangChain** : https://python.langchain.com
- **LangGraph** : https://langchain-ai.github.io/langgraph/
- **Pandas** : https://pandas.pydata.org
- **HTTPX** : https://www.python-httpx.org
