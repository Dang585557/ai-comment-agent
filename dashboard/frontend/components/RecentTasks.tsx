const tasks = [

    {
        task: "สร้างคลิป TikTok 10 คลิป",
        team: "TikTok",
        status: "Running",
        created: "10:30",
        progress: 65,
    },

    {
        task: "Render Video #52",
        team: "Video",
        status: "Rendering",
        created: "10:45",
        progress: 82,
    },

    {
        task: "Build Dashboard",
        team: "Developer",
        status: "Coding",
        created: "11:00",
        progress: 48,
    },

    {
        task: "Research Competitor",
        team: "Research",
        status: "Analyzing",
        created: "11:10",
        progress: 91,
    },

];

export default function RecentTasks() {

    return (

        <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">

            <h2 className="text-2xl font-bold mb-6">

                Recent Tasks

            </h2>

            <div className="overflow-x-auto">

                <table className="w-full">

                    <thead>

                        <tr className="border-b border-zinc-800">

                            <th className="text-left py-3">Task</th>

                            <th className="text-left py-3">Team</th>

                            <th className="text-left py-3">Status</th>

                            <th className="text-left py-3">Created</th>

                            <th className="text-left py-3">Progress</th>

                        </tr>

                    </thead>

                    <tbody>

                        {tasks.map((task, index) => (

                            <tr
                                key={index}
                                className="border-b border-zinc-800 hover:bg-zinc-800 transition"
                            >

                                <td className="py-4">

                                    {task.task}

                                </td>

                                <td>

                                    {task.team}

                                </td>

                                <td>

                                    <span className="text-green-400">

                                        {task.status}

                                    </span>

                                </td>

                                <td>

                                    {task.created}

                                </td>

                                <td className="w-64">

                                    <div className="w-full bg-zinc-800 rounded-full h-3">

                                        <div
                                            className="bg-cyan-400 h-3 rounded-full"
                                            style={{
                                                width: `${task.progress}%`
                                            }}
                                        />

                                    </div>

                                    <div className="text-sm text-zinc-400 mt-1">

                                        {task.progress}%

                                    </div>

                                </td>

                            </tr>

                        ))}

                    </tbody>

                </table>

            </div>

        </div>

    );

}
