CREATE INDEX IF NOT EXISTS idx_users_username
ON users(username);

CREATE INDEX IF NOT EXISTS idx_agents_team
ON agents(team);

CREATE INDEX IF NOT EXISTS idx_tasks_agent
ON tasks(agent_name);

CREATE INDEX IF NOT EXISTS idx_tasks_priority
ON tasks(priority);

CREATE INDEX IF NOT EXISTS idx_tasks_created
ON tasks(created_at);

CREATE INDEX IF NOT EXISTS idx_workflows_name
ON workflows(workflow_name);

CREATE INDEX IF NOT EXISTS idx_workflows_status
ON workflows(status);

CREATE INDEX IF NOT EXISTS idx_logs_source
ON logs(source);

CREATE INDEX IF NOT EXISTS idx_logs_created
ON logs(created_at);

CREATE INDEX IF NOT EXISTS idx_memory_created
ON conversation_memory(created_at);

CREATE INDEX IF NOT EXISTS idx_reports_created
ON ai_reports(created_at);

CREATE INDEX IF NOT EXISTS idx_api_enabled
ON api_keys(enabled);

CREATE INDEX IF NOT EXISTS idx_workflow_history_status
ON workflow_history(status);

CREATE INDEX IF NOT EXISTS idx_workflow_history_created
ON workflow_history(created_at);
