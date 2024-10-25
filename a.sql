CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('freelancer', 'client', 'admin') DEFAULT 'client',
    bio TEXT,
    skills JSONB,  -- Array of skills for freelancers
    profile_picture VARCHAR(255),
    rating DECIMAL(3, 2),  -- Avg rating from completed projects
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_title VARCHAR(255) NOT NULL,
    project_detail TEXT NOT NULL,
    project_status ENUM('pending', 'in_progress', 'completed', 'canceled') DEFAULT 'pending',
    project_deadline DATE,
    project_budget DECIMAL(10, 2),
    project_documents JSONB,  -- Links to documents or resources
    created_by INTEGER REFERENCES users(user_id),
    workspace_id INTEGER REFERENCES workspaces(workspace_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE workspaces (
    workspace_id SERIAL PRIMARY KEY,
    workspace_name VARCHAR(255) NOT NULL,
    workspace_owner INTEGER REFERENCES users(user_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);