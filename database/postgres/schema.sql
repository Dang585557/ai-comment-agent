CREATE TABLE IF NOT EXISTS conversation_memory (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vector_documents (
    id SERIAL PRIMARY KEY,
    document_name VARCHAR(255),
    document_path TEXT,
    embedding_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ai_reports (
    id SERIAL PRIMARY KEY,
    report_type VARCHAR(100),
    report_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS settings (
    id SERIAL PRIMARY KEY,
    config_key VARCHAR(255) UNIQUE,
    config_value TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_memory_session
ON conversation_memory(session_id);

CREATE INDEX IF NOT EXISTS idx_embedding
ON vector_documents(embedding_id);

CREATE INDEX IF NOT EXISTS idx_settings_key
ON settings(config_key);
