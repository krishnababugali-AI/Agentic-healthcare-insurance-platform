# System Architecture

The platform combines agentic AI with deterministic AWS workflows for healthcare insurance operations.

## Main Flow

Provider / Application
        ↓
FastAPI
        ↓
Supervisor Agent
        ↓
Specialized Agents
        ↓
MCP Tools + RAG
        ↓
AWS Step Functions
        ↓
Enterprise Systems / Databases
        ↓
Human Review when required

## Specialized Agents

- Benefits Verification Agent
- Policy Agent
- Prior Authorization Agent
- Claims Analysis Agent
- Appeals Agent

## AWS Components

- Amazon S3
- Amazon Textract
- Amazon OpenSearch
- AWS Lambda
- Amazon SQS
- Amazon EventBridge
- AWS Step Functions
- DynamoDB
- Aurora PostgreSQL
- CloudWatch

## AI Components

- OpenAI Agents SDK
- OpenAI Responses API
- MCP
- RAG
- Structured Outputs
- Human-in-the-Loop