INSERT INTO users (
    username,
    password_hash,
    role
)
VALUES
(
    'admin',
    '$2b$12$CHANGE_THIS_PASSWORD_HASH',
    'admin'
)
ON CONFLICT (username)
DO NOTHING;

INSERT INTO agents (
    name,
    team,
    status
)
VALUES
('CEO','CEO','ONLINE'),
('AI Manager','Manager','ONLINE'),
('TikTok Team','TikTok','IDLE'),
('Video Team','Video','IDLE'),
('Developer Team','Developer','IDLE'),
('Research Team','Research','IDLE'),
('Website Team','Website','IDLE');

INSERT INTO workflows (
    workflow_name,
    status
)
VALUES
('content_creation','READY'),
('video_pipeline','READY'),
('research_pipeline','READY'),
('website_pipeline','READY'),
('daily_report','READY')
ON CONFLICT DO NOTHING;

INSERT INTO settings (
    config_key,
    config_value
)
VALUES
('theme','dark'),
('language','en'),
('dashboard_refresh','5'),
('default_llm','openai')
ON CONFLICT (config_key)
DO NOTHING;
