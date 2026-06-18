import DashboardLayout from "../components/DashboardLayout";

export default function WorkflowsPage() {

    const workflows = [

        {
            name: "Content Creation",
            description: "Generate script, video and thumbnail",
            status: "RUNNING",
            progress: 78,
        },

        {
            name: "Video Pipeline",
            description: "Edit, subtitle and render videos",
            status: "RUNNING",
            progress: 65,
        },

        {
            name: "Research Pipeline",
            description: "Collect trends and competitor data",
            status: "ONLINE",
            progress: 91,
        },

        {
            name: "Website Pipeline",
            description: "Build and deploy website",
            status: "ONLINE",
            progress: 54,
        },

        {
            name: "Expansion Pipeline",
            description: "Prepare future departments",
            status: "IDLE",
            progress: 22,
        }

    ];

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-8">

                    <h1 className="text-3xl font-bold text-white">

                        Workflow Center

                    </h1>

                    <p className="text-zinc-400 mt-2">

                        Manage every workflow inside AI-COMPANY.

                    </p>

                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

                    {workflows.map((workflow) => (

                        <div
                            key={workflow.name}
                            className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6"
                        >

                            <div className="flex justify-between items-center">

                                <h2 className="text-xl font-bold text-white">

                                    {workflow.name}

                                </h2>

                                <span className="text-green-400">

                                    {workflow.status}

                                </span>

                            </div>

                            <p className="text-zinc-400 mt-4">

                                {workflow.description}

                            </p>

                            <div className="mt-6">

                                <div className="flex justify-between text-sm">

                                    <span className="text-zinc-400">

                                        Progress

                                    </span>

                                    <span>

                                        {workflow.progress}%

                                    </span>

                                </div>

                                <div className="w-full bg-zinc-800 rounded-full h-3 mt-2">

                                    <div
                                        className="bg-cyan-500 h-3 rounded-full"
                                        style={{
                                            width: `${workflow.progress}%`
                                        }}
                                    />

                                </div>

                            </div>

                            <div className="mt-6 flex gap-3">

                                <button className="px-4 py-2 rounded-lg bg-cyan-600 hover:bg-cyan-500">

                                    Open

                                </button>

                                <button className="px-4 py-2 rounded-lg bg-green-600 hover:bg-green-500">

                                    Restart

                                </button>

                                <button className="px-4 py-2 rounded-lg bg-red-600 hover:bg-red-500">

                                    Stop

                                </button>

                            </div>

                        </div>

                    ))}

                </div>

            </div>

        </DashboardLayout>

    );

      }
