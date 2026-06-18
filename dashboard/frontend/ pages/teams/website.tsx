import DashboardLayout from "../../components/DashboardLayout";
import AgentCard from "../../components/AgentCard";

export default function WebsiteTeamPage() {

    const agents = [

        {
            name: "Deploy Agent",
            role: "Deployment Engineer",
            status: "ONLINE",
            currentTask: "Deploying AI-COMPANY Dashboard",
            progress: 82,
        },

        {
            name: "SEO Agent",
            role: "SEO Specialist",
            status: "ONLINE",
            currentTask: "Optimizing Website SEO",
            progress: 68,
        },

        {
            name: "Monitor Agent",
            role: "Website Monitor",
            status: "ONLINE",
            currentTask: "Monitoring Server Health",
            progress: 100,
        },

        {
            name: "Performance Agent",
            role: "Performance Optimizer",
            status: "ONLINE",
            currentTask: "Optimizing Loading Speed",
            progress: 74,
        },

        {
            name: "Security Agent",
            role: "Security Monitor",
            status: "ONLINE",
            currentTask: "Scanning Security Issues",
            progress: 89,
        },

        {
            name: "Backup Agent",
            role: "Backup Manager",
            status: "ONLINE",
            currentTask: "Creating Daily Backup",
            progress: 41,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Website Team

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        AI Website Operations Center

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
