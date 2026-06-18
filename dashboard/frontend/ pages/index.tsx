import DashboardLayout from "../../components/DashboardLayout";
import TeamCard from "../../components/TeamCard";

export default function TeamsPage() {

    const teams = [

        {
            name: "TikTok Team",
            description: "Create and manage TikTok content.",
            members: 6,
            status: "ONLINE",
            path: "/teams/tiktok",
        },

        {
            name: "Video Team",
            description: "Video editing and rendering.",
            members: 5,
            status: "ONLINE",
            path: "/teams/video",
        },

        {
            name: "Developer Team",
            description: "Develop AI-COMPANY platform.",
            members: 4,
            status: "ONLINE",
            path: "/teams/developer",
        },

        {
            name: "Research Team",
            description: "Research trends and competitors.",
            members: 3,
            status: "ONLINE",
            path: "/teams/research",
        },

        {
            name: "Website Team",
            description: "Deploy and maintain websites.",
            members: 2,
            status: "ONLINE",
            path: "/teams/website",
        },

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div>

                    <h1 className="text-3xl font-bold text-white">

                        AI Teams

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        Manage every department inside AI-COMPANY.

                    </p>

                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

                    {teams.map((team) => (

                        <TeamCard
                            key={team.name}
                            name={team.name}
                            description={team.description}
                            members={team.members}
                            status={team.status}
                            path={team.path}
                        />

                    ))}

                </div>

            </div>

        </DashboardLayout>

    );

}
