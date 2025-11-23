# 🎯 **RÉFÉRENCE COMPLÈTE DES TRIGGER-WORDS (TW)**

> **DOCUMENT CENTRAL** : Toutes les définitions et utilisations des trigger-words du WSurfWSpaceGlobal  
> **Navigation** : [← Documentation PowerShell](PowerShell/md/trigger-words-documentation.md) | [← Glossaire](Fab/glossaire.md)

**Version**: 1.0.0  
**Date de création**: 2 septembre 2025  
**Auteur**: Ava pour Cap'taine Fabrice  
**Mission**: Centraliser TOUTES les définitions de trigger-words en un point de référence unique

---

## 📑 **TABLE DES MATIÈRES**

1. [Principe Général](#-principe-général)
2. [Liste des Trigger-Words](#-liste-des-trigger-words)
   - [`archiv`](#archiv)
   - [`propre`](#propre)
   - [`fixdkr`](#fixdkr)
   - [`majclaud`](#majclaud)
   - [`startAva`](#startava)
   - [`drawio`](#drawio)
   - [`avatar`](#avatar)
   - [`i2v`](#i2v)
   - [`search`](#search)
   - [`s2t`](#s2t)
3. [Règles d'Usage](#-règles-dusage)

---

## 🧭 **PRINCIPE GÉNÉRAL**

Les **Trigger-Words (TW)** sont des phrases déclencheurs spécifiques qui permettent à Ava d'exécuter automatiquement des scripts et actions. Ils suivent le format standardisé :

```
tw : paramètre
```

**Règles de Normalisation (2025)** :
1. **Court** : Maximum 8 caractères
2. **Sans accent** : Aucun caractère accentué
3. **Format** : `tw : [paramètre]`

**Source de vérité** : `Fab/glossaire.md` et `Meta/RulesFabForAva.md`

---

## 📋 **LISTE DES TRIGGER-WORDS**

### 🔧 **Opérationnel & Système**

#### `archiv`
*Anciennement : archivage*
- **Syntaxe** : `archiv : [nom_projet]`
- **Action** : Crée un nouveau dossier thématique avec config Git standard
- **Script** : `PowerShell/add-context.ps1`
- **Doc** : [archivage-projets-algorithme.md](PowerShell/md/archivage-projets-algorithme.md)

#### `propre`
- **Syntaxe** : `propre : [chemin/dossier]`
- **Action** : Normalise les noms de fichiers (supprime accents, caractères spéciaux)
- **Script** : `PowerShell/propre-trigger.ps1`
- **Doc** : [nom-propre-documentation.md](PowerShell/md/nom-propre-documentation.md)

#### `fixdkr`
*Anciennement : réparer docker*
- **Syntaxe** : `fixdkr`
- **Action** : Répare Docker Desktop après arrêt incorrect
- **Script** : `PowerShell/repair-docker.ps1`
- **Doc** : [repair-docker.md](PowerShell/md/repair-docker.md)

#### `majclaud`
*Anciennement : majclaudedirectives, majcla*
- **Syntaxe** : `majclaud`
- **Action** : Synchronise CLAUDE.md avec les directives maîtresses
- **Script** : `PowerShell/MAJClaudeDirectives.ps1`

#### `startAva`
*Anciennement : AvaStart, avago*
- **Syntaxe** : `startAva`
- **Action** : Force la lecture des directives maîtresses (Gardien de démarrage)
- **Script** : `PowerShell/AVA-SYSTEM/Ava-Startup-Guardian.ps1`

### 📊 **Visuel & Diagrammes**

#### `drawio`
*Regroupe : diagrammes, Diagram, diag*
- **Syntaxe 1** : `drawio` (Génération diagramme DrawIO spécialisé)
- **Syntaxe 2** : `drawio : gen [synthese.md]` (Génère diagramme DrawIO depuis synthèse)
- **Syntaxe 3** : `drawio : install` (Installe extensions VS Code)
- **Scripts** : 
  - `Python/scripts/Missions/generate_drawio_mission5.py`
  - `Python/scripts/Missions/generate_ava_mission4_synthesis_to_diagram.py`
  - `PowerShell/install-vscode-extensions.ps1`

### 🎨 **Création & IA**

#### `avatar`
*Anciennement : Autoportrait*
- **Syntaxe** : `avatar`
- **Action** : Génère autoportrait visuel Ava
- **Script** : `Python/scripts/Missions/generate_ava_moussaillon_autoportrait.py`

#### `i2v`
- **Syntaxe** : `i2v`
- **Action** : Image To Video avec Fal.ai
- **Script** : `Python/scripts/Missions/generate_ava_mission2_i2v.py`

#### `search`
*Anciennement : SearchWeb*
- **Syntaxe** : `search : [requête]`
- **Action** : Recherche web temps réel via MCP
- **Script** : `Python/scripts/Missions/web_search_direct.py`

#### `s2t`
- **Syntaxe** : `s2t : [fichier.wav]`
- **Action** : Transcription audio → synthèse markdown intelligente
- **Script** : `AudioTools/Transcription/auto_transcription.py`

---

## ⚠️ **RÈGLES D'USAGE**

1. **Pas d'emojis** dans les commandes.
2. **Respecter la syntaxe** `tw : paramètre` (espace avant et après les deux-points).
3. **Encodage** : Les scripts appelés doivent être en UTF-8 sans BOM.