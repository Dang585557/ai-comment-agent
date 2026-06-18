import DashboardLayout from "../../components/DashboardLayout";
import AgentCard from "../../components/AgentCard";

export default function VideoTeamPage() {

    const agents = [

        {
            name: "Video Manager",
            role: "Team Leader",
            status: "ONLINE",
            currentTask: "Managing Video Team",
            progress: 100,
        },

        {
            name: "Editor Agent",
            role: "Video Editor",
            status: "ONLINE",
            currentTask: "Editing Product Video",
            progress: 74,
        },

        {
            name: "Subtitle Agent",
            role: "Subtitle Generator",
            status: "ONLINE",
            currentTask: "Generating Subtitles",
            progress: 91,
        },

        {
            name: "Voice Agent",
            role: "AI Voice",
            status: "ONLINE",
            currentTask: "Generating Voice Over",
            progress: 58,
        },

        {
            name: "Thumbnail Agent",
            role: "Thumbnail Designer",
            status: "ONLINE",
            currentTask: "Creating Thumbnail",
            progress: 67,
        },

        {
            name: "Render Agent",
            role: "Rendering",
            status: "ONLINE",
            currentTask: "Rendering Final Video",
            progress: 46,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Video Editing Team

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        AI Video Production Office

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
