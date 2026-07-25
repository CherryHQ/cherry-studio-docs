---
icon: chart-line
---

# Build a Gold Market Review Agent with Kimi K2.5

This case study demonstrates how to use a Cherry Studio Agent to review gold price movements: retrieve public information, align prices with event times, save sources, and generate a report that is easy to review manually.

Kimi K2.5 is the example model in this case. You can replace it with another model as long as the model can be used by Cherry Studio Agents through an **Anthropic Messages** endpoint. Models, prices, and tool compatibility can vary by provider, so verify the setup with a small task first.

{% hint style="warning" %}
This case demonstrates a research workflow and does not provide investment advice. A model can miss sources, misread data, or generate incorrect code. Do not trade directly based on generated results.
{% endhint %}

## Final Deliverables

Limit the deliverables to four files:

```text
gold-review/
├── sources.md       # Sources, publication times, retrieval times, and purposes
├── market-data.csv  # Price data actually used in this run
├── analysis.md      # Event timeline, calculations, and uncertainties
└── report.html      # Final readable report
```

These four files answer “where the information came from,” “which data was used,” “how the conclusions were reached,” and “how the results are presented.” Do not ask only for an attractive HTML file. Without the first three items, the final page is difficult to verify.

## Workflow Design

Divide the task into three stages:

| Stage | Main work | Evidence that must be retained |
| :--- | :--- | :--- |
| Data collection | Retrieve price and macroeconomic information for the specified time range | Source URL, publication time, retrieval time, and raw values |
| Event alignment | Compare significant movements with events in the same time window | Time zone, event time, price range, supporting and opposing evidence |
| Report generation | Organize charts, timelines, conclusions, and limitations | Calculation method, citation links, missing data, and risk notices |

The Agent can use the `Task` tool to delegate independent research steps to subtasks, but parallelism alone does not guarantee quality. The main task must still standardize time, units, and source conventions.

## Step 1: Prepare a Model

1. Open **Settings → Model Providers**.
2. Configure a provider that offers Kimi K2.5, or select another model suitable for tool calling.
3. Confirm that the model's endpoint types include **Anthropic Messages**.
4. Save it and complete a regular chat first, then confirm that the model appears in the Agent model selector.

The Agent model selector excludes Embedding, Rerank, and image generation models. If a model works in a regular chat but does not appear for Agents, check its endpoint type and capability labels first.

See [Model Providers](../../pre-basic/providers/) for provider configuration. If you need to add a model manually or correct its capability labels, see the model management instructions under [Custom Providers](../../pre-basic/providers/zi-ding-yi-fu-wu-shang.md#add-models-manually).

## Step 2: Prepare a Working Directory

Create an empty directory such as `gold-review` and put only the sources needed for this task inside it. Do not select your entire user directory, Downloads directory, or a project directory containing keys.

If you already have price data, place it in `market-data.csv`. Include at least:

```csv
timestamp,open,high,low,close,unit,timezone,source
2026-01-01T00:00:00Z,,,,,USD/oz,UTC,
```

You can adjust the fields, but units and time zones must be explicit. Do not combine data from different markets or sources before converting them to the same convention.

## Step 3: Create the Agent

1. Open **Library** and create an Agent.
2. Enter `Gold Market Review` as the name.
3. Select the model verified in the previous step as the primary model.
4. Add the `gold-review` directory under accessible directories.
5. Set the permission mode to **Normal Mode** first.
6. Save the Agent.

Normal Mode allows reading files but requests confirmation before editing files or running commands. Do not choose “Fully Automatic” for the first run. Retrieving financial data and writing local files both require human observation.

For details about Agent settings, see [Agents](../agent.md).

## Step 4: Add Tools

Under **Capability Extensions → Built-in Tools**, confirm that these tools are available:

| Tool | Purpose in this case | Required |
| :--- | :--- | :--- |
| `Read`, `Glob`, `Grep` | Read existing sources and find files | Yes |
| `WebSearch` | Search public information | Yes |
| `WebFetch` | Read a specified webpage | Yes |
| `Write` | Create CSV, Markdown, and HTML files | Yes |
| `Task`, `TodoWrite` | Divide tasks and track progress | Recommended |
| `Bash` | Run data processing or local validation commands | Optional |

`WebSearch`, `WebFetch`, `Write`, and `Bash` access the network or modify local content. After adding the tools, Normal Mode still requests confirmation when needed. Approve only calls required for the current step.

If a webpage requires login, presents a CAPTCHA, or prohibits automated retrieval, download the material manually and place it in the working directory. Do not ask the Agent to bypass access restrictions.

## Step 5: Install Skills as Needed

This case can be completed using only a system prompt. If you need to reuse the process, organize the stable workflow into skills, for example:

* `market-data-verifier`: Defines data fields, units, time zones, and multi-source verification.
* `event-timeline`: Defines event timeline and causal-strength labels.
* `research-report`: Defines report structure, citation format, and failure reporting.

Every installable skill must be a directory or ZIP archive containing `SKILL.md`. To install one:

1. Open **Settings → Skills**.
2. Install the skill from a directory or ZIP archive.
3. Return to **Capability Extensions → Skills** for the saved Agent.
4. Enable the required skills for the current Agent.

Skills are first stored in Cherry Studio's global skill library. After you enable one for an Agent, the app links it into `.claude/skills/` under that Agent's working directory. Do not manually copy an entire `.claude` configuration from an unknown source or overwrite skill links created by the app.

See [Skills](../../pre-basic/settings/skills.md) for complete instructions.

## Step 6: Enter the System Prompt

Place this template in the Agent's system prompt and modify it as needed:

```text
You are a market research assistant. Your task is to produce a verifiable gold market review,
not to predict returns or provide trading advice.

Working rules:
1. First confirm the instrument, market, currency, unit, time zone, and date range requested by the user.
2. Prices, interest rates, indexes, and events must come from files or tool results read during this run;
   do not fill in current values from model memory.
3. For each critical fact, record the source URL, source name, publication time, and access time for this run.
4. Verify core conclusions with at least two independent sources; if only one source is available, label it clearly.
5. Strictly distinguish facts, calculated results, interpretations, and assumptions. Do not present temporal proximity as causation.
6. If data is missing, a webpage is inaccessible, or a calculation fails, retain the gap and explain why.
7. List the plan before writing files; create or modify files only in the current working directory.
8. Produce sources.md, market-data.csv, analysis.md, and report.html as the final outputs.
9. report.html must open locally and must not embed keys or personal information.
10. End the report with “For research and learning only; not investment advice.”
```

The system prompt defines persistent rules. Put specific research dates and events in each task you send instead of hard-coding them into the system prompt.

## Step 7: Run a Source Checklist First

Do not request a complete report in the first task. Ask the Agent to propose a source plan first:

```text
First, prepare a source checklist for reviewing movements in the spot price of gold. Do not write the report yet.

Scope:
- Instrument: ask me to confirm before starting
- Quoted unit: US dollars per ounce
- Time zone: UTC
- Date range: begin retrieval only after I confirm it

Output:
1. Required data fields;
2. Types of sources you plan to use;
3. Tools you will call and why;
4. Files you will create;
5. Permissions and potential charges that require my confirmation.
```

After confirming that the plan does not expand the directory or data scope, allow it to begin collecting sources.

## Step 8: Run the Review

After confirming the scope, send:

```text
Run the review for the confirmed scope.

Requirements:
- Collect and save sources before beginning the analysis;
- Mark the time windows with the largest price changes;
- Convert all event times to UTC;
- List evidence, counterevidence, and confidence for every proposed cause;
- State the input fields and formula for every calculation;
- Put unverifiable content under “Needs verification” instead of filling it in;
- Generate report.html only after completing the intermediate Markdown files;
- Finally, report which files were created or modified and which issues remain unresolved.
```

During the run, examine three categories of tool requests closely:

1. **Network requests**: Confirm that domains match the planned sources.
2. **File writes**: Confirm that paths are inside `gold-review`.
3. **Command execution**: Confirm that commands process only this run's data and whether they install packages or access additional networks.

If a data processing library must be installed temporarily, pause and review the package name, source, and command yourself. Do not treat dependency installation as authorization that is automatically required to “continue the task.”

## Step 9: Accept Intermediate Artifacts

### Check `sources.md`

Each source should include at least:

* Source name and URL.
* Publication time of the webpage or data.
* Access time for this run.
* Which fact or data point it supports.
* Whether it requires login or a subscription, or is a secondary republication.

An inaccessible link cannot be the only evidence. Trace republished articles back to the original publisher whenever possible.

### Check `market-data.csv`

Confirm that:

* The time format and time zone are consistent.
* Price units are consistent.
* Missing values were not silently filled.
* The data range matches the task requirements.
* `source` maps to an entry in `sources.md`.

Randomly select several timestamps and compare them manually against the original source.

### Check `analysis.md`

“The price fell after an event” shows only a temporal relationship; it does not prove causation. Use this structure for each explanation:

```text
Observation:
Time window:
Supporting evidence:
Opposing or alternative explanations:
Confidence: High / Medium / Low
Still needs verification:
```

Technical indicators must also retain formulas, parameters, and input ranges. A result without its calculation process does not pass acceptance.

### Check `report.html`

Open it locally and check that:

* The page does not depend on inaccessible local absolute paths.
* Numbers in tables and charts match the CSV.
* Every critical conclusion leads back to a source.
* Missing data and limitations are not hidden in the final layout.
* The page does not contain an API Key, Cookie, username, or personal directory.

## Frequently Asked Questions

### Kimi K2.5 Does Not Appear in the Agent Model List

Confirm that the model's endpoint types include **Anthropic Messages**, and check whether the model is incorrectly marked as Embedding, Rerank, or image generation. Providers offering a model with the same name do not necessarily expose the same endpoint capabilities.

### The Agent Does Not Search the Web

Check that `WebSearch` and `WebFetch` have been added to the current Agent and that tool requests were not denied. Marketing claims that a model “supports web search” do not mean that Cherry Studio automatically provides web tools.

### An Installed Skill Does Not Work

Save the Agent and make sure it has a working directory, then enable the skill in that Agent's skill list. Placing files in the working directory does not mean that a skill is installed and linked.

### The Report File Cannot Be Created

Check whether `Write` is available, the current permission request was approved, and the target path is inside an accessible directory. Do not solve a path problem by granting access to the entire disk.

### The Data Looks Complete, but Sources Do Not Match

Stop generating the final report and ask the Agent to identify the source line for every value. Delete values without a source or mark them as needing verification instead of continuing to polish them.

## Ways to Extend the Workflow

After the basic workflow passes, add capabilities gradually:

* Connect a reviewed data service through MCP.
* Generate reviews periodically with scheduled tasks while retaining human review.
* Send a “report generated” notification through a channel instead of sending a trading conclusion directly.
* Organize stable verification rules into a team skill.

Add only one capability at a time, then recheck permissions, costs, and outputs. For further configuration, see [MCP](../mcp/), [Scheduled Tasks](../scheduled-tasks.md), and [Channels](../agent-channels.md).

Return to [Agent Case Studies](./) to view other workflows.
