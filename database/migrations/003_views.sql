CREATE OR REPLACE VIEW active_agents AS
SELECT
    id,
    name,
    team,
    status,
    last_run
FROM agents
WHERE status IN ('ONLINE', 'IDLE');

CREATE OR REPLACE VIEW pending_tasks AS
SELECT
    id,
    agent_name,
    task_name,
    priority,
    created_at
FROM tasks
WHERE status = 'pending';

CREATE OR REPLACE VIEW completed_tasks AS
SELECT
    id,
    agent_name,
    task_name,
    finished_at
FROM tasks
WHERE status = 'completed';

CREATE OR REPLACE VIEW workflow_summary AS
SELECT
    workflow_name,
    status,
    COUNT(*) AS total
FROM workflows
GROUP BY workflow_name, status;

CREATE OR REPLACE VIEW system_logs AS
SELECT
    level,
    source,
    message,
    created_at
FROM logs
ORDER BY created_at DESC;
