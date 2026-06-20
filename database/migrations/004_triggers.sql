CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS
$$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

ALTER TABLE settings
ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

DROP TRIGGER IF EXISTS trg_settings_updated_at
ON settings;

CREATE TRIGGER trg_settings_updated_at
BEFORE UPDATE
ON settings
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

ALTER TABLE agents
ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

DROP TRIGGER IF EXISTS trg_agents_updated_at
ON agents;

CREATE TRIGGER trg_agents_updated_at
BEFORE UPDATE
ON agents
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

ALTER TABLE tasks
ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

DROP TRIGGER IF EXISTS trg_tasks_updated_at
ON tasks;

CREATE TRIGGER trg_tasks_updated_at
BEFORE UPDATE
ON tasks
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();
