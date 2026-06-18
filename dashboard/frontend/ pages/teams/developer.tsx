import DashboardLayout from "../../components/DashboardLayout";
import AgentCard from "../../components/AgentCard";

export default function DeveloperTeamPage() {

    const agents = [

        {
            name: "Architect Agent",
            role: "System Architect",
            status: "ONLINE",
            currentTask: "Designing AI System",
            progress: 94,
        },

        {
            name: "Coder Agent",
            role: "Software Engineer",
            status: "ONLINE",
            currentTask: "Writing Source Code",
            progress: 71,
        },

        {
            name: "Reviewer Agent",
            role: "Code Reviewer",
            status: "ONLINE",
            currentTask: "Reviewing Pull Requests",
            progress: 58,
        },

        {
            name: "Tester Agent",
            role: "QA Engineer",
            status: "ONLINE",
            currentTask: "Running Automated Tests",
            progress: 82,
        },

        {
            name: "Documentation Agent",
            role: "Technical Writer",
            status: "ONLINE",
            currentTask: "Updating Documentation",
            progress: 63,
        },

        {
            name: "GitHub Agent",
            role: "Repository Manager",
            status: "ONLINE",
            currentTask: "Managing GitHub Repository",
            progress: 76,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Developer Team

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        AI Software Engineering Department

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
