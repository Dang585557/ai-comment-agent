import DashboardLayout from "../components/DashboardLayout";

export default function TasksPage() {

    const tasks = [

        {
            id: "TASK-001",
            team: "TikTok",
            title: "Create 10 Product Videos",
            status: "Running",
            progress: 76,
        },

        {
            id: "TASK-002",
            team: "Video",
            title: "Render Live Promotion",
            status: "Rendering",
            progress: 48,
        },

        {
            id: "TASK-003",
            team: "Developer",
            title: "Build Dashboard",
            status: "Coding",
            progress: 62,
        },

        {
            id: "TASK-004",
            team: "Research",
            title: "Analyze Competitors",
            status: "Working",
            progress: 89,
        },

        {
            id: "TASK-005",
            team: "Website",
            title: "Deploy New Version",
            status: "Deploying",
            progress: 34,
        },

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Task Center

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        Manage all AI tasks running inside AI-COMPANY.

                    </p>

                </div>

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl overflow-hidden">

                    <table className="w-full">

                        <thead className="bg-zinc-950">

                            <tr>

                                <th className="text-left p-4">Task ID</th>

                                <th className="text-left p-4">Team</th>

                                <th className="text-left p-4">Task</th>

                                <th className="text-left p-4">Status</th>

                                <th className="text-left p-4">Progress</th>

                            </tr>

                        </thead>

                        <tbody>

                            {tasks.map((task) => (

                                <tr
                                    key={task.id}
                                    className="border-t border-zinc-800"
                                >

                                    <td className="p-4">

                                        {task.id}

                                    </td>

                                    <td className="p-4">

                                        {task.team}

                                    </td>

                                    <td className="p-4">

                                        {task.title}

                                    </td>

                                    <td className="p-4 text-green-400">

                                        {task.status}

                                    </td>

                                    <td className="p-4">

                                        <div className="w-full bg-zinc-800 rounded-full h-3">

                                            <div
                                                className="bg-cyan-500 h-3 rounded-full"
                                                style={{
                                                    width: `${task.progress}%`
                                                }}
                                            />

                                        </div>

                                        <span className="text-sm text-zinc-400">

                                            {task.progress}%

                                        </span>

                                    </td>

                                </tr>

                            ))}

                        </tbody>

                    </table>

                </div>

            </div>

        </DashboardLayout>

    );

}
