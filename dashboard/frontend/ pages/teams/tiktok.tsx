import DashboardLayout from "../../components/DashboardLayout";
import AgentCard from "../../components/AgentCard";

export default function TikTokTeamPage() {

    const agents = [

        {
            name: "TikTok Manager",
            role: "Team Leader",
            status: "ONLINE",
            currentTask: "Managing TikTok Team",
            progress: 100,
        },

        {
            name: "Content Agent",
            role: "Content Creator",
            status: "ONLINE",
            currentTask: "Creating 10 TikTok Posts",
            progress: 72,
        },

        {
            name: "Script Agent",
            role: "Script Writer",
            status: "ONLINE",
            currentTask: "Writing Live Script",
            progress: 58,
        },

        {
            name: "Trend Agent",
            role: "Trend Analyzer",
            status: "ONLINE",
            currentTask: "Finding Viral Trends",
            progress: 91,
        },

        {
            name: "Analytics Agent",
            role: "Analytics",
            status: "ONLINE",
            currentTask: "Analyzing Performance",
            progress: 83,
        },

        {
            name: "Report Agent",
            role: "Report Generator",
            status: "ONLINE",
            currentTask: "Generating Daily Report",
            progress: 45,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        TikTok Team Office

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        All TikTok AI Agents are working here.

                    </p>

                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

                    {agents.map((agent) => (

                        <AgentCard

                            key={agent.name}

                            name={agent.name}

                            role={agent.role}

                            status={agent.status}

                            currentTask={agent.currentTask}

                            progress={agent.progress}

                        />

                    ))}

                </div>

            </div>

        </DashboardLayout>

    );

}
