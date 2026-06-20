CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE SCHEMA IF NOT EXISTS ai_company;

SET search_path TO ai_company;

CREATE TABLE IF NOT EXISTS system_info (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    system_name VARCHAR(100) NOT NULL,
    version VARCHAR(50) NOT NULL,
    environment VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO system_info (
    system_name,
    version,
    environment
)
VALUES (
    'AI-COMPANY',
    '1.0.0',
    'development'
)
ON CONFLICT DO NOTHING;

CREATE TABLE IF NOT EXISTS api_keys (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    provider VARCHAR(100) NOT NULL,
    api_key TEXT NOT NULL,
    enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_api_provider
ON api_keys(provider);

CREATE TABLE IF NOT EXISTS workflow_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    workflow_name VARCHAR(200),
    status VARCHAR(50),
    execution_time DOUBLE PRECISION,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_workflow_name
ON workflow_history(workflow_name);
