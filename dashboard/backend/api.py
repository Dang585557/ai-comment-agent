"""
AI-COMPANY
dashboard/backend/api.py

Dashboard API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(
    title="AI-COMPANY Dashboard API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():

    return {

        "project": "AI-COMPANY",

        "status": "ONLINE",

        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }


@app.get("/system/status")
def system_status():

    return {

        "status": "ONLINE",

        "cpu": "0%",

        "ram": "0%",

        "storage": "0%"

    }


@app.get("/dashboard/cards")
def dashboard_cards():

    return {

        "total_agents": 0,

        "active_tasks": 0,

        "completed_today": 0,

        "system_health": "Healthy",

        "storage_used": "0 GB",

        "api_calls_today": 0

    }


@app.get("/teams")
def teams():

    return [

        {

            "name": "TikTok Team",

            "status": "ONLINE"

        },

        {

            "name": "Video Team",

            "status": "ONLINE"

        },

        {

            "name": "Developer Team",

            "status": "ONLINE"

        },

        {

            "name": "Research Team",

            "status": "ONLINE"

        },

        {

            "name": "Website Team",

            "status": "ONLINE"

        }

    ]


@app.get("/devices")
def devices():

    return {

        "cloud_pc": [

            {

                "name": "Cloud PC #1",

                "status": "ONLINE"

            }

        ],

        "android": [

            {

                "name": "Android #1",

                "status": "ONLINE"

            }

        ],

        "ios": []

    }


@app.get("/logs")
def logs():

    return [

        {

            "level": "INFO",

            "message": "System Started"

        }

    ]


@app.get("/activities")
def activities():

    return [

        {

            "team": "TikTok",

            "task": "Waiting..."

        },

        {

            "team": "Video",

            "task": "Waiting..."

        },

        {

            "team": "Developer",

            "task": "Waiting..."

        }

    ]
