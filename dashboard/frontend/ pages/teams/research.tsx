import DashboardLayout from "../../components/DashboardLayout";
import AgentCard from "../../components/AgentCard";

export default function ResearchTeamPage() {

    const agents = [

        {
            name: "Research Manager",
            role: "Team Leader",
            status: "ONLINE",
            currentTask: "Managing Research Team",
            progress: 100,
        },

        {
            name: "Competitor Agent",
            role: "Competitor Analysis",
            status: "ONLINE",
            currentTask: "Analyzing Competitors",
            progress: 87,
        },

        {
            name: "Trend Agent",
            role: "Trend Research",
            status: "ONLINE",
            currentTask: "Finding Trending Products",
            progress: 76,
        },

        {
            name: "Keyword Agent",
            role: "Keyword Research",
            status: "ONLINE",
            currentTask: "Collecting Keywords",
            progress: 64,
        },

        {
            name: "Report Agent",
            role: "Report Generator",
            status: "ONLINE",
            currentTask: "Generating Research Report",
            progress: 52,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Research Team

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        AI Market Research Department

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
