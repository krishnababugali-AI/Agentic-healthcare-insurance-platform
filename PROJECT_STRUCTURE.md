# Agentic Healthcare Insurance Claims & Prior Authorization Platform

This repository is organized as a production-oriented, modular healthcare insurance AI platform.

The architecture separates:

- API and application layers
- Agent orchestration
- OpenAI Agents SDK integration
- MCP tools
- RAG and document intelligence
- Deterministic insurance workflows
- AWS managed services
- Human-in-the-loop review
- Security and guardrails
- Observability
- Infrastructure as Code
- Automated testing and evaluation

> **Current Status:** Architecture and repository scaffold are being established. Functional modules will be implemented incrementally.

---

## Repository Structure

```text
agentic-healthcare-insurance-platform/
│
├── README.md
├── PROJECT_STRUCTURE.md
├── LICENSE
├── .gitignore
├── .dockerignore
├── .env.example
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── Makefile
│
├── app/
│   │
│   ├── __init__.py
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── health.py
│   │   ├── claims.py
│   │   ├── prior_authorization.py
│   │   ├── eligibility.py
│   │   ├── appeals.py
│   │   └── documents.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logging.py
│   │   ├── exceptions.py
│   │   ├── security.py
│   │   └── constants.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── patient.py
│   │   ├── provider.py
│   │   ├── insurance.py
│   │   ├── claim.py
│   │   ├── prior_auth.py
│   │   ├── appeal.py
│   │   ├── document.py
│   │   └── agent.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── supervisor_agent.py
│   │   ├── benefits_agent.py
│   │   ├── policy_agent.py
│   │   ├── prior_auth_agent.py
│   │   ├── claims_agent.py
│   │   ├── appeals_agent.py
│   │   ├── document_agent.py
│   │   └── human_review_agent.py
│   │
│   ├── agent_runtime/
│   │   ├── __init__.py
│   │   ├── openai_runtime.py
│   │   ├── responses_client.py
│   │   ├── agentcore_runtime.py
│   │   ├── session_manager.py
│   │   └── runtime_factory.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   │
│   │   ├── eligibility/
│   │   │   ├── eligibility_tool.py
│   │   │   └── coverage_tool.py
│   │   │
│   │   ├── claims/
│   │   │   ├── claim_lookup_tool.py
│   │   │   ├── claim_validation_tool.py
│   │   │   └── claim_status_tool.py
│   │   │
│   │   ├── prior_auth/
│   │   │   ├── authorization_lookup_tool.py
│   │   │   ├── authorization_submit_tool.py
│   │   │   └── authorization_status_tool.py
│   │   │
│   │   ├── policy/
│   │   │   ├── policy_search_tool.py
│   │   │   └── medical_necessity_tool.py
│   │   │
│   │   └── provider/
│   │       ├── provider_lookup_tool.py
│   │       └── network_status_tool.py
│   │
│   ├── mcp/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── registry.py
│   │   │
│   │   └── servers/
│   │       ├── eligibility_server.py
│   │       ├── claims_server.py
│   │       ├── prior_auth_server.py
│   │       ├── policy_server.py
│   │       └── provider_server.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── ingestion.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── indexing.py
│   │   ├── retriever.py
│   │   ├── reranker.py
│   │   ├── citations.py
│   │   └── pipeline.py
│   │
│   ├── document_processing/
│   │   ├── __init__.py
│   │   ├── processor.py
│   │   ├── textract_service.py
│   │   ├── normalization.py
│   │   ├── classification.py
│   │   └── metadata_extractor.py
│   │
│   ├── workflows/
│   │   ├── __init__.py
│   │   ├── benefits_verification.py
│   │   ├── prior_authorization.py
│   │   ├── claims_analysis.py
│   │   ├── appeals.py
│   │   ├── document_ingestion.py
│   │   └── workflow_router.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── s3_service.py
│   │   ├── sqs_service.py
│   │   ├── eventbridge_service.py
│   │   ├── dynamodb_service.py
│   │   ├── aurora_service.py
│   │   ├── opensearch_service.py
│   │   ├── step_functions_service.py
│   │   └── secrets_service.py
│   │
│   ├── guardrails/
│   │   ├── __init__.py
│   │   ├── pii_filter.py
│   │   ├── prompt_injection.py
│   │   ├── output_validation.py
│   │   ├── tool_permissions.py
│   │   └── policy_enforcement.py
│   │
│   ├── human_review/
│   │   ├── __init__.py
│   │   ├── review_queue.py
│   │   ├── escalation.py
│   │   ├── approval.py
│   │   └── audit.py
│   │
│   ├── observability/
│   │   ├── __init__.py
│   │   ├── telemetry.py
│   │   ├── tracing.py
│   │   ├── metrics.py
│   │   ├── cloudwatch.py
│   │   ├── opentelemetry.py
│   │   └── agent_tracing.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── ids.py
│       ├── timestamps.py
│       ├── retries.py
│       └── serialization.py
│
├── infrastructure/
│   │
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       ├── providers.tf
│       ├── versions.tf
│       │
│       ├── environments/
│       │   ├── dev.tfvars
│       │   ├── staging.tfvars
│       │   └── production.tfvars
│       │
│       └── modules/
│           ├── networking/
│           ├── s3/
│           ├── lambda/
│           ├── sqs/
│           ├── eventbridge/
│           ├── step_functions/
│           ├── dynamodb/
│           ├── aurora/
│           ├── opensearch/
│           ├── iam/
│           ├── monitoring/
│           └── agentcore/
│
├── lambdas/
│   ├── document_ingestion/
│   │   └── handler.py
│   │
│   ├── textract_callback/
│   │   └── handler.py
│   │
│   ├── workflow_trigger/
│   │   └── handler.py
│   │
│   └── human_review_notification/
│       └── handler.py
│
├── state_machines/
│   ├── document_ingestion.asl.json
│   ├── prior_authorization.asl.json
│   ├── claims_analysis.asl.json
│   └── appeals.asl.json
│
├── prompts/
│   ├── supervisor.md
│   ├── benefits_agent.md
│   ├── policy_agent.md
│   ├── prior_auth_agent.md
│   ├── claims_agent.md
│   └── appeals_agent.md
│
├── evaluations/
│   ├── datasets/
│   │   ├── claims_cases.json
│   │   ├── prior_auth_cases.json
│   │   └── policy_questions.json
│   │
│   ├── evaluators/
│   │   ├── groundedness.py
│   │   ├── tool_accuracy.py
│   │   ├── citation_accuracy.py
│   │   ├── policy_compliance.py
│   │   └── workflow_accuracy.py
│   │
│   └── run_evaluations.py
│
├── tests/
│   ├── unit/
│   │   ├── test_agents.py
│   │   ├── test_rag.py
│   │   ├── test_tools.py
│   │   ├── test_guardrails.py
│   │   └── test_workflows.py
│   │
│   ├── integration/
│   │   ├── test_mcp.py
│   │   ├── test_opensearch.py
│   │   ├── test_textract.py
│   │   └── test_agent_workflow.py
│   │
│   ├── e2e/
│   │   ├── test_prior_authorization.py
│   │   ├── test_claim_processing.py
│   │   └── test_appeal_generation.py
│   │
│   └── security/
│       ├── test_prompt_injection.py
│       ├── test_pii_leakage.py
│       └── test_tool_authorization.py
│
├── data/
│   ├── synthetic/
│   │   ├── policies/
│   │   ├── claims/
│   │   ├── prior_authorizations/
│   │   └── appeals/
│   │
│   └── README.md
│
├── scripts/
│   ├── bootstrap_local.sh
│   ├── ingest_documents.py
│   ├── create_indexes.py
│   ├── seed_database.py
│   └── run_evaluations.py
│
├── docs/
│   ├── architecture.md
│   ├── agent_architecture.md
│   ├── mcp_architecture.md
│   ├── rag_architecture.md
│   ├── data_flow.md
│   ├── security.md
│   ├── threat_model.md
│   ├── observability.md
│   ├── deployment.md
│   └── decisions/
│       ├── ADR-001-agent-framework.md
│       ├── ADR-002-rag-storage.md
│       └── ADR-003-workflow-orchestration.md
│
└── .github/
    └── workflows/
        ├── ci.yml
        ├── tests.yml
        ├── security.yml
        ├── terraform-plan.yml
        └── deploy.yml
```

---

# Major Application Components

## 1. FastAPI API Layer

`app/api/`

Provides external REST APIs for:

- benefits verification
- eligibility checks
- prior authorization requests
- claims analysis
- appeal workflows
- insurance document ingestion

FastAPI acts as the primary service interface between external applications and the agent/workflow layer.

---

## 2. Agent Layer

`app/agents/`

Specialized agents are separated by insurance business capability.

### Supervisor Agent

Routes requests to the appropriate specialized agent and coordinates multi-agent workflows.

### Benefits Agent

Determines:

- member eligibility
- coverage
- deductible
- copay
- coinsurance
- benefit limitations

### Policy Agent

Retrieves insurance policies and medical-necessity criteria through RAG.

### Prior Authorization Agent

Analyzes whether a requested service requires authorization and coordinates the authorization workflow.

### Claims Agent

Analyzes claim information, policy rules, supporting documentation, and potential denial reasons.

### Appeals Agent

Builds evidence-backed appeal packages from claim information, policies, medical documentation, and denial explanations.

---

# 3. OpenAI Agent Runtime

`app/agent_runtime/`

Provides the abstraction layer for:

- OpenAI Agents SDK
- OpenAI Responses API
- Amazon Bedrock AgentCore
- session management
- runtime configuration

Keeping the runtime separate from business logic allows agent implementations to evolve without tightly coupling the entire system to one execution environment.

---

# 4. MCP Integration

`app/mcp/`

Model Context Protocol servers expose enterprise healthcare capabilities as standardized agent tools.

Example MCP servers:

```text
Eligibility MCP Server
Claims MCP Server
Prior Authorization MCP Server
Policy MCP Server
Provider MCP Server
```

Agents interact with these systems through tool interfaces instead of directly accessing backend databases.

---

# 5. RAG Platform

`app/rag/`

The retrieval pipeline supports insurance documents such as:

```text
Coverage policies
Medical necessity guidelines
Prior authorization requirements
Provider manuals
Claims policies
Appeals guidelines
Benefit documents
```

Conceptual pipeline:

```text
Documents
   ↓
Amazon S3
   ↓
Amazon Textract
   ↓
Document normalization
   ↓
Chunking
   ↓
Embeddings
   ↓
Amazon OpenSearch
   ↓
Semantic Retrieval
   ↓
Reranking
   ↓
Agent Context
   ↓
Grounded Response
```

---

# 6. Deterministic Workflow Layer

`app/workflows/`

LLMs should not control every step of a healthcare insurance transaction.

Deterministic orchestration is used for sensitive business processes such as:

```text
Prior Authorization
Claims Analysis
Appeals
Document Ingestion
Human Approval
```

Amazon Step Functions coordinates long-running and deterministic workflows.

---

# 7. Event-Driven Architecture

AWS services support asynchronous processing.

```text
Amazon S3
   ↓
EventBridge
   ↓
SQS
   ↓
Lambda
   ↓
Step Functions
   ↓
AI Agents / MCP Tools
```

SQS provides buffering and retry handling between services.

---

# 8. Human-in-the-Loop

`app/human_review/`

High-impact decisions can be escalated for human review.

Example cases:

```text
Low-confidence policy interpretation
Missing clinical documents
Prior authorization exceptions
Claim denial recommendations
Appeal submission
Conflicting coverage information
```

Agents can recommend actions, while sensitive decisions remain subject to deterministic rules and human authorization.

---

# 9. Guardrails

`app/guardrails/`

Controls include:

```text
PII/PHI filtering
Prompt-injection detection
Tool authorization
Structured output validation
Agent action validation
Policy enforcement
Sensitive-operation approval
```

---

# 10. Observability

`app/observability/`

Observability uses:

```text
Amazon CloudWatch
OpenTelemetry
Agent tracing
Application metrics
Workflow metrics
Structured logs
```

Potential AI-specific metrics include:

```text
Agent latency
Tool-call latency
Token consumption
Retrieval latency
Retrieval relevance
Agent routing accuracy
Tool-selection accuracy
Groundedness
Human escalation rate
Workflow completion rate
```

---

# 11. Infrastructure

`infrastructure/terraform/`

AWS infrastructure is modeled through Terraform and separated into reusable modules.

Infrastructure components include:

```text
IAM
VPC / Networking
Amazon S3
AWS Lambda
Amazon SQS
Amazon EventBridge
AWS Step Functions
Amazon DynamoDB
Amazon Aurora PostgreSQL
Amazon OpenSearch
CloudWatch
Amazon Bedrock AgentCore
```

---

# 12. Evaluation Framework

`evaluations/`

Agents are evaluated using deterministic and model-based evaluation techniques.

Evaluation areas include:

```text
RAG groundedness
Citation accuracy
Tool-call accuracy
Agent routing
Policy retrieval quality
Workflow completion
Structured output validity
Safety
Prompt-injection resistance
PII/PHI leakage
```

Production failures can later be converted into regression evaluation cases.

---

# Development Strategy

The platform will be implemented incrementally.

```text
Phase 1
Repository architecture + FastAPI foundation

Phase 2
Synthetic healthcare insurance domain

Phase 3
RAG ingestion pipeline

Phase 4
OpenAI Agents SDK

Phase 5
MCP servers and enterprise tools

Phase 6
Prior authorization workflow

Phase 7
Claims analysis workflow

Phase 8
Appeals workflow

Phase 9
AWS event-driven processing

Phase 10
Human-in-the-loop

Phase 11
Observability and evaluation

Phase 12
Terraform and CI/CD

Phase 13
Production hardening
```

This structure is intentionally modular so each capability can be developed, tested, deployed, and evaluated independently.